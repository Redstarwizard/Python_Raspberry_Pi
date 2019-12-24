#!/usr/bin/env python
try:
    # for Python2
    import Tkinter as tk
    from Tkinter import *
    import ttk
    import tkFont 
    import explorerhat
    import time
except ImportError:
    # for Python3
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk
    import tkinter.font as tkFont
    import explorerhat
    import time

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-zoomed',True)
        self.root.title("Explorerhat Pro Toggle4 GUI")
        self.root.geometry('800x480')
        self.root.configure(background = "aqua" )
        self.customFont = tkFont.Font(family="Halvetica bold", size=16)

        self.slider1 = tk.Scale(self.root, from_=0, to=100,label='Motor 1',tickinterval=5, length = 1280, width = 50,
                               orient="horizontal", font=self.customFont)
        self.slider1.configure(sliderlength =100,troughcolor = "aqua",activebackground = "green",background = "yellow" )
        self.slider1.bind("<ButtonRelease-1>", self.updateValue1)
        self.slider1.grid(row=1)

        self.slider2 = tk.Scale(self.root, from_=0, to=100,label='Motor 2',tickinterval=5, length = 1280, width = 50,
                               orient="horizontal", font=self.customFont)
        self.slider2.configure(sliderlength =100,troughcolor = "aqua",activebackground = "green",background = "yellow" )
        self.slider2.bind("<ButtonRelease-1>", self.updateValue2)
        self.slider2.grid(row=2)
          
        self.ledToggle = tk.Button(self.root, text = "Toggle", command = self.ledtoggle, height = 3, width = 20, font=self.customFont )
        self.ledToggle.configure(background = "light green" )
        self.ledToggle.configure(activebackground = "green", activeforeground = "light blue")
        self.ledToggle.grid(row=3,column=0,sticky=NW)

        self.ledPulse = tk.Button(self.root, text = "Pulse", command = self.ledpulse, height = 3, width = 20, font=self.customFont)
        self.ledPulse.configure(background = "light green" )
        self.ledPulse.configure(activebackground = "green", activeforeground = "light blue")
        self.ledPulse.grid(row=3,column=0,sticky=NE)

        self.output1toggle = tk.Button(self.root, text = "out1", command = self.output1toggle, height = 3, width = 20, font=self.customFont)
        self.output1toggle.configure(background = "light green" )
        self.output1toggle.configure(activebackground = "blue", activeforeground = "light blue")
        self.output1toggle.grid(row=4,column=0,sticky=NW)

        self.output2toggle = tk.Button(self.root, text = "out2", command = self.output2toggle, height = 3, width = 20, font=self.customFont)
        self.output2toggle.configure(background = "light green" )
        self.output2toggle.configure(activebackground = "blue", activeforeground = "light blue")
        self.output2toggle.grid(row=4,column=0,sticky=NE)

        self.output3toggle = tk.Button(self.root, text = "out3", command = self.output3toggle, height = 3, width = 20, font=self.customFont)
        self.output3toggle.configure(background = "light green" )
        self.output3toggle.configure(activebackground = "green", activeforeground = "light blue")
        self.output3toggle.grid(row=5,column=0,sticky=NW)

        self.output4toggle = tk.Button(self.root, text = "out4", command = self.output4toggle, height = 3, width = 20, font=self.customFont)
        self.output4toggle.configure(background = "light green" )
        self.output4toggle.configure(activebackground = "red", activeforeground = "light blue")
        self.output4toggle.grid(row=5,column=0,sticky=NE)

        self.ledoff = tk.Button(self.root, text = "ledoff", command = self.ledoff, height = 3, width = 20, font=self.customFont)
        self.ledoff.configure(background = "light green" )
        self.ledoff.configure(activebackground = "green", activeforeground = "light blue")
        self.ledoff.grid(row=6,column=0,sticky=NW)

        self.exitButton  = Button(self.root, text = "Exit",  command = self.exitProgram, height = 3 , width = 20, font=self.customFont) 
        self.exitButton.configure(background = "pink" )
        self.exitButton.configure(activebackground = "red", activeforeground = "light blue")
        self.exitButton.grid(row=6,column=0,sticky=NE)

        self.root.mainloop()
 
    def updateValue1(self, event):
        #print self.slider.get()
        explorerhat.motor.one.forwards(self.slider1.get())
 
    def updateValue2(self, event):
        #print self.slider.get()
        explorerhat.motor.two.forwards(self.slider2.get())
    
    def ledtoggle(self):
        explorerhat.light.toggle()

    def ledpulse(self):
        explorerhat.light.pulse()

    def output1toggle(self):
        explorerhat.output.one.toggle()

    def output2toggle(self):
        explorerhat.output.two.toggle()

    def output3toggle(self):
        explorerhat.output.three.toggle()

    def output4toggle(self):
        explorerhat.output.four.toggle()

    def ledoff(self):
        explorerhat.light.off() 
        explorerhat.output.one.off()
        explorerhat.output.two.off()
        explorerhat.output.three.off()
        explorerhat.output.four.off()
        
    def exitProgram(self):
        print("Exit Button pressed")
        self.root.destroy()	

app=App()
