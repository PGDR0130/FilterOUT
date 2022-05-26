from tkinter import *
from tkinter import ttk
from colorConverting import RGBToHex

class SimpleToggle:
    def __init__(self):
        self.window = Tk()

        # Tabs
        tabControl = ttk.Notebook(self.window)
        self.toggleTab = ttk.Frame(tabControl)
        self.backGroundTab = ttk.Frame(tabControl)

        tabControl.add(self.toggleTab, text ='ToggleHSV')
        tabControl.add(self.backGroundTab, text ='BackGround')

        tabControl.pack(expand = 1, fill ="both")


        # window settings
        self.window.title("Simple Toggles")
        self.window.geometry("250x500")

        self.window.protocol("WM_DELETE_WINDOW", self._onClosing)

        # Values
        self.reverseState = False
        self._save = False

# Tab1 - ControlHSV
    # Color
        # row0 - Color Control (Hue) [0-179]
        Label(self.toggleTab, text="Color Control").grid(column=0, row=0)
        self.color = Scale(self.toggleTab, from_=0, to=180, orient=HORIZONTAL)
        self.color.grid(column=1, row=0)
        #row1 -Color Range Control (Hue Range) 
        Label(self.toggleTab, text="Color Range").grid(column=0, row=1)
        self.colorRange = Scale(self.toggleTab, from_=0, to=180, orient=HORIZONTAL)
        self.colorRange.grid(column=1, row=1)

    # Saturation
        #row2 - Saturation Control (Saturation) [0-255]
        Label(self.toggleTab, text="Saturation Control").grid(column=0, row=2)
        self.sat = Scale(self.toggleTab, from_=0, to=255, orient=HORIZONTAL)
        self.sat.grid(column=1, row=2)
        # row3 - Saturation Range Control (Saturation Range)
        Label(self.toggleTab, text="Saturation Range").grid(column=0, row=3)
        self.satRange = Scale(self.toggleTab, from_=0, to=255, orient=HORIZONTAL)
        self.satRange.grid(column=1, row=3)
        
    # Brightness
        #row4 - Brightness Control (Value) [0-255]
        Label(self.toggleTab, text="Brightness Control").grid(column=0, row=4)
        self.bright = Scale(self.toggleTab, from_=0, to=255, orient=HORIZONTAL)
        self.bright.grid(column=1, row=4)
        #row5 - Brightness Range Control (Value Range) 
        Label(self.toggleTab, text="Brightness Range").grid(column=0, row=5)
        self.brightRange = Scale(self.toggleTab, from_=0, to=255, orient=HORIZONTAL)
        self.brightRange.grid(column=1, row=5)

    # Buttons
        # Reverse
        Label(self.toggleTab, text="Reverse Filter").grid(column=0, row=10)
        self.reverse = Button(self.toggleTab, text="Reverse", command=self._ReverseStateChagne).grid(column=1, row=10)

        # Reset
        Label(self.toggleTab, text="Reset All Value").grid(column=0, row=11)
        self.reset = Button(self.toggleTab, text="Reset", command=self._initScaleVal).grid(column=1, row=11)

        # Save 
        Label(self.toggleTab, text="Save Image").grid(column=0, row=12)
        self.save = Button(self.toggleTab, text='Save', command=self.saveHandle).grid(column=1, row=12)        


# Tab2 - BackGround Color Control
        TAB2_COL = 0
        TAB2_ROW = 0

        # RED 
        Label(self.backGroundTab, text="RED").grid(column=TAB2_COL, row=TAB2_ROW)
        self.redValue = Scale(self.backGroundTab, from_=0, to=255, orient=HORIZONTAL, command=self._colorPreUpdate)
        self.redValue.grid(column=TAB2_COL + 1, row=TAB2_ROW)

        # Green 
        Label(self.backGroundTab, text="Green").grid(column=TAB2_COL, row=TAB2_ROW + 1)
        self.greenValue = Scale(self.backGroundTab, from_=0, to=255, orient=HORIZONTAL, command=self._colorPreUpdate)
        self.greenValue.grid(column=TAB2_COL + 1, row=TAB2_ROW + 1)        

        # Blue
        Label(self.backGroundTab, text="Blue").grid(column=TAB2_COL, row=TAB2_ROW + 2)
        self.blueValue = Scale(self.backGroundTab, from_=0, to=255, orient=HORIZONTAL, command=self._colorPreUpdate)
        self.blueValue.grid(column=TAB2_COL + 1, row=TAB2_ROW + 2)

        # Color Preview
        Label(self.backGroundTab, text='      ').grid(column=TAB2_COL + 2, row= TAB2_ROW + 1)
        self.colorPre = Button(self.backGroundTab)
        self._colorPreUpdate(0)


        self._initScaleVal()

    # set all scale to defult value
    def _initScaleVal(self):
        self.color.set(0)
        self.colorRange.set(50)
        self.colorRange.set(50)
        self.sat.set(122)
        self.satRange.set(255)
        self.bright.set(122)
        self.brightRange.set(255)

    def saveHandle(self, toFalse=False):
        # determine whether or not to change self._save
        if toFalse == True and self._save == True:
            self._save = False
            return True
        elif toFalse == False:
            self._save = True

    # Call by Reverse Button
    def _ReverseStateChagne(self):
        self.reverseState = True if self.reverseState == False else False

    # Update Color when toggle changed
    def _colorPreUpdate(self, _ ):
        self.colorPre.destroy()
        R, G, B = self.redValue.get(), self.greenValue.get(), self.blueValue.get()
        HEX = RGBToHex(R, G, B)
        self.colorPre = Button(self.backGroundTab, text='      ', bg=HEX, activebackground=HEX)
        self.colorPre.grid(column= 3, row= 1)

    # get upper and lower value for masking image
    def getHSVRangeValue(self):
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
            value[0][0] = 0
            # upper
        if self.colorVal + self.colorRangeVal <= 180:
            value[1][0] = self.colorVal + self.colorRangeVal
        else:
            value[1][0] = 180

        # Saturation
            # lower
        if self.satVal - self.satRangeVal >= 0:
            value[0][1] = self.satVal - self.satRangeVal
        else:
            value[0][1] = 0
            # upper
        if self.satVal + self.satRangeVal <=255:
            value[1][1] = self.satVal + self.satRangeVal
        else:
            value[1][1] = 255

        # Brightness
            # lower 
        if self.brightVal - self.brightRangeVal >= 0:
            value[0][2] = self.brightVal - self.brightRangeVal
        else:
            value[0][2] = 0
            # upper
        if self.brightVal + self.brightRangeVal <= 255:
            value[1][2] = self.brightVal + self.brightRangeVal
        else:
            value[1][2] = 255 
        
        return value

    def getColValue():
        
        return 

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
