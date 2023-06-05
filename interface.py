from tkinter import*
from PIL import ImageTk, Image
from cube import Cube
from cube_representation import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random



def runFile():
    global cube1

    root = Tk()
    root.title('Create cube')
   # root.iconbitmap('C:\Elena\Programming\Python')


    Chosen_Cube = StringVar()

    options = ["3X3 rubik's cube"] #deleted 2x2 cube

    Chosen_Cube.set(options[0])

    select = OptionMenu(root, Chosen_Cube, *options)
    select.pack()

    def createCube():
        
        if Chosen_Cube.get() == options[0]:
            cube1 = Cube(3)
        """elif Chosen_Cube.get() == options[1]:
            cube1 = Cube(2)"""
        return cube1
    
    def solve():
        global cube1
        cube1 = Cube(3)
        showCube(cube1)
        chart = FigureCanvasTkAgg(fig, top)
        chart.get_tk_widget().grid(row = 0, column = 0)

        lbl = Label(top, text= cube1.cube)
        lbl.grid(row=0,column = 1)
 
        """scamlbl = Label(top, text= f'Number of moves: {random.randint(5,20)}')
        scamlbl.grid(row = 3, column = 0)
        scamtime= Label(top, text= f'Time to solve: {random.uniform(0,1)} seconds')
        scamtime.grid(row=4, column=0)"""
    


    def openWindow():
        global top
        global chart
        global cube1
        cube1 = createCube()
        top = Toplevel()
        top.title("Rubik's Cube")
        lbl = Label(top, text= cube1.cube)
        lbl.grid(row=0,column = 1)
        btn2 = Button(top, text='Solve', command=solve).grid(row=2, column=0) #.quit would close both, destroy only closes that window 
        top.bind('<KeyPress>', Turn)
        showCube(cube1)
        chart = FigureCanvasTkAgg(fig, top)
        chart.get_tk_widget().grid(row = 0, column = 0)



    btn = Button(root, text='Create Cube', command=openWindow).pack()


    def Turn(x):
        if x.char == '':
            pass
        else:
            if x.char == 'u':
                cube1.turn_U()
            elif x.char == 'd':
                cube1.turn_D()
            elif x.char == 'f':
                cube1.turn_F()
            elif x.char == 'b':
                cube1.turn_B()
            elif x.char == 'r':
                cube1.turn_R()
            elif x.char == 'g': #for some reason l and k make it really weird...still don't know why
                cube1.turn_L()

            elif x.char == 'U':
                cube1.turn_UR()
            elif x.char == 'D':
                cube1.turn_DR()
            elif x.char == 'F':
                cube1.turn_FR()
            elif x.char == 'B':
                cube1.turn_BR()
            elif x.char == 'R':
                cube1.turn_RR()
            elif x.char == 'G':
                cube1.turn_LR()
            showCube(cube1)
            chart = FigureCanvasTkAgg(fig, top)
            chart.get_tk_widget().grid(row = 0, column = 0)

            lbl = Label(top, text= cube1.cube)
            lbl.grid(row=0,column = 1)
        
    
        
        





    mainloop()


if __name__ == '__main__':
    runFile()



