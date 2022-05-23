from tkinter import *
import tkinter as tk
from turtle import right

from matplotlib.pyplot import grid 


class SimpleToggle:
    def __init__(self):
        window = Tk()
        window.title("Simple Toggles")
        window.geometry("250x500")

    # Color
        # row0 - Color Control (Hue) [0-360]
        Label(window, text="Color Control").grid(column=0, row=0)
        self.color = Scale(window, from_=0, to=360, orient=HORIZONTAL)
        self.color.grid(column=1, row=0)
        #row1 -Color Range Control (Hue Range) 
        Label(window, text="Color Range").grid(column=0, row=1)
        self.colorRange = Scale(window, from_=0, to=360, orient=HORIZONTAL)
        self.colorRange.grid(column=1, row=1)

    # Saturation
        #row2 - Saturation Control (Saturation) [0-255]
        Label(window, text="Saturation Control").grid(column=0, row=2)
        self.sat = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.sat.grid(column=1, row=2)
        # row3 - Saturation Range Control (Saturation Range)
        Label(window, text="Saturation Range").grid(column=0, row=3)
        self.satRange = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.satRange.grid(column=1, row=3)
        
    # Brightness
        #row4 - Brightness Control (Value) [0-255]
        Label(window, text="Brightness Control").grid(column=0, row=4)
        self.bright = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.bright.grid(column=1, row=4)
        #row5 - Brightness Range Control (Value Range) 
        Label(window, text="Brightness Range").grid(column=0, row=5)
        self.brightRange = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.brightRange.grid(column=1, row=5)


    # Buttons
        # Reverse
        Label(window, text="Reverse Filter").grid(column=0, row=10)
        self.reverse = Button(window, text="Reverse").grid(column=1, row=10)

        # Reset
        Label(window, text="Reset All Value").grid(column=0, row=11)
        self.reset = Button(window, text="Reset").grid(column=1, row=11)


        self._initScaleVal()
        window.mainloop()

    def _initScaleVal(self):
        self.colorRange.set(50)
        self.sat.set(122)
        self.satRange.set(255)
        self.bright.set(122)
        self.brightRange.set(255)

    def getValue():
        pass

Tkwin = SimpleToggle()