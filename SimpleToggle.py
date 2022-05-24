from tkinter import *
import tkinter as tk
import time


class SimpleToggle:
    def __init__(self):
        self.window = Tk()
        self.window.title("Simple Toggles")
        self.window.geometry("250x500")

        self.window.protocol("WM_DELETE_WINDOW", self._onClosing)

        # Values
        self.reverseState = False

    # Color
        # row0 - Color Control (Hue) [0-360]
        Label(self.window, text="Color Control").grid(column=0, row=0)
        self.color = Scale(self.window, from_=0, to=360, orient=HORIZONTAL)
        self.color.grid(column=1, row=0)
        #row1 -Color Range Control (Hue Range) 
        Label(self.window, text="Color Range").grid(column=0, row=1)
        self.colorRange = Scale(self.window, from_=0, to=360, orient=HORIZONTAL)
        self.colorRange.grid(column=1, row=1)

    # Saturation
        #row2 - Saturation Control (Saturation) [0-255]
        Label(self.window, text="Saturation Control").grid(column=0, row=2)
        self.sat = Scale(self.window, from_=0, to=255, orient=HORIZONTAL)
        self.sat.grid(column=1, row=2)
        # row3 - Saturation Range Control (Saturation Range)
        Label(self.window, text="Saturation Range").grid(column=0, row=3)
        self.satRange = Scale(self.window, from_=0, to=255, orient=HORIZONTAL)
        self.satRange.grid(column=1, row=3)
        
    # Brightness
        #row4 - Brightness Control (Value) [0-255]
        Label(self.window, text="Brightness Control").grid(column=0, row=4)
        self.bright = Scale(self.window, from_=0, to=255, orient=HORIZONTAL)
        self.bright.grid(column=1, row=4)
        #row5 - Brightness Range Control (Value Range) 
        Label(self.window, text="Brightness Range").grid(column=0, row=5)
        self.brightRange = Scale(self.window, from_=0, to=255, orient=HORIZONTAL)
        self.brightRange.grid(column=1, row=5)


    # Buttons
        # Reverse
        Label(self.window, text="Reverse Filter").grid(column=0, row=10)
        self.reverse = Button(self.window, text="Reverse", command=self._ReverseStateChagne).grid(column=1, row=10)

        # Reset
        Label(self.window, text="Reset All Value").grid(column=0, row=11)
        self.reset = Button(self.window, text="Reset", command=self._initScaleVal).grid(column=1, row=11)

        self._initScaleVal()

    # set all scale to defult value
    def _initScaleVal(self):
        self.colorRange.set(50)
        self.sat.set(122)
        self.satRange.set(255)
        self.bright.set(122)
        self.brightRange.set(255)
    
    # Call by Reverse Button
    def _ReverseStateChagne(self):
        self.reverseState = True if self.reverseState == False else False


    # get upper and lower value for masking image
    def getValue(self):
        # get all Scale Value
        self.colorVal = self.color.get()
        self.colorRangeVal = self.colorRange.get()
        self.satVal = self.sat.get()
        self.satRangeVal = self.satRange.get()
        self.brightVal = self.bright.get()
        self.brightRangeVal = self.brightRange.get()


        value = [[0,0,0],[0,0,0]]
        # Color
            #lower
        if self.colorVal - self.colorRangeVal >= 0:
            value[0][0] = self.colorVal - self.colorRangeVal
        else:
            value[0][0] = 360 - abs(self.colorVal - self.colorRangeVal)
            # upper
        if self.colorVal + self.colorRangeVal <= 360:
            value[1][0] = self.colorVal + self.colorRangeVal
        else:
            value[1][0] = (self.colorVal + self.colorRangeVal)%360

        # Saturation
            # lower
        if self.satVal - self.satRangeVal >= 0:
            value[0][1] = self.satVal - self.satRangeVal
        else:
            value[0][1] = 255 - abs(self.satVal - self.satRangeVal)
            # upper
        if self.satVal + self.satRangeVal <=360:
            value[1][1] = self.satVal + self.satRangeVal
        else:
            value[1][1] = (self.satVal + self.satRangeVal)%255

        # Brightness
            # lower 
        if self.brightVal - self.brightRangeVal >= 0:
            value[0][2] = self.brightVal - self.brightRangeVal
        else:
            value[0][2] = 255 - abs(self.brightVal - self.brightRangeVal)
            # upper
        if self.brightVal + self.brightRangeVal <= 360:
            value[1][2] = self.brightVal + self.brightRangeVal
        else:
            value[1][2] = (self.brightVal + self.brightRangeVal)%255
        
        return value

    def update(self):
        self.window.update()

    def _onClosing(self):
            self.window.destroy()

    



#  udpate method with out using mainloop: https://gordonlesti.com/use-tkinter-without-mainloop/

# Tkwin = SimpleToggle()
# while True:
#     Tkwin.update()  
#     print(Tkwin.reverseState)
#     print(Tkwin.getValue())
#     time.sleep(0.05)
