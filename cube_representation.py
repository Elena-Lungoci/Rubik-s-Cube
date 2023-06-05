import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch, Rectangle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import mpl_toolkits.mplot3d.art3d as art3d
from cube import *





    #there was probably a better way of doing this

colors = ['white', 'blue', 'red', 'green', 'orange', 'yellow']

fig = plt.figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(projection='3d')



def showCube(cube1):

   
    #white face
    square1 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[0][0][0]],ec="black")
    ax.add_patch(square1)
    art3d.pathpatch_2d_to_3d(square1, z=15, zdir="z")

    square2 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[0][0][1]],ec="black")
    ax.add_patch(square2)
    art3d.pathpatch_2d_to_3d(square2, z=15, zdir="z")

    square3 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[0][0][2]],ec="black")
    ax.add_patch(square3)
    art3d.pathpatch_2d_to_3d(square3, z=15, zdir="z")

    square4 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[0][1][0]],ec="black")
    ax.add_patch(square4)
    art3d.pathpatch_2d_to_3d(square4, z=15, zdir="z")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[0][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=15, zdir="z")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[0][1][2]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=15, zdir="z")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[0][2][0]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=15, zdir="z")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[0][2][1]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=15, zdir="z")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[0][2][2]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=15, zdir="z")



    # blue face


    square10 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[1][2][0]],ec="black")
    ax.add_patch(square10)
    art3d.pathpatch_2d_to_3d(square10, z=15, zdir="x")

    square11 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[1][1][0]],ec="black")
    ax.add_patch(square11)
    art3d.pathpatch_2d_to_3d(square11, z=15, zdir="x")

    square12 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[1][0][0]],ec="black")
    ax.add_patch(square12)
    art3d.pathpatch_2d_to_3d(square12, z=15, zdir="x")

    square13 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[1][2][1]],ec="black")
    ax.add_patch(square13)
    art3d.pathpatch_2d_to_3d(square13, z=15, zdir="x")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[1][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=15, zdir="x")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[1][0][1]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=15, zdir="x")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[1][2][2]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=15, zdir="x")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[1][1][2]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=15, zdir="x")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[1][0][2]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=15, zdir="x")

    #face 3 orange


    square10 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[4][2][2]],ec="black")
    ax.add_patch(square10)
    art3d.pathpatch_2d_to_3d(square10, z=15, zdir="y")

    square11 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[4][1][2]],ec="black")
    ax.add_patch(square11)
    art3d.pathpatch_2d_to_3d(square11, z=15, zdir="y")

    square12 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[4][0][2]],ec="black")
    ax.add_patch(square12)
    art3d.pathpatch_2d_to_3d(square12, z=15, zdir="y")

    square13 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[4][2][1]],ec="black")
    ax.add_patch(square13)
    art3d.pathpatch_2d_to_3d(square13, z=15, zdir="y")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[4][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=15, zdir="y")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[4][0][1]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=15, zdir="y")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[4][2][0]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=15, zdir="y")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[4][1][0]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=15, zdir="y")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[4][0][0]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=15, zdir="y")


    #yellow face


    square1 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[5][2][0]],ec="black")
    ax.add_patch(square1)
    art3d.pathpatch_2d_to_3d(square1, z=0, zdir="z")

    square2 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[5][2][1]],ec="black")
    ax.add_patch(square2)
    art3d.pathpatch_2d_to_3d(square2, z=0, zdir="z")

    square3 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[5][2][2]],ec="black")
    ax.add_patch(square3)
    art3d.pathpatch_2d_to_3d(square3, z=0, zdir="z")

    square4 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[5][1][0]],ec="black")
    ax.add_patch(square4)
    art3d.pathpatch_2d_to_3d(square4, z=0, zdir="z")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[5][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=0, zdir="z")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[5][1][2]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=0, zdir="z")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[5][0][0]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=0, zdir="z")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[5][0][1]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=0, zdir="z")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[5][0][2]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=0, zdir="z")


    #green

        
    square10 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[3][2][2]],ec="black")
    ax.add_patch(square10)
    art3d.pathpatch_2d_to_3d(square10, z=0, zdir="x")

    square11 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[3][1][2]],ec="black")
    ax.add_patch(square11)
    art3d.pathpatch_2d_to_3d(square11, z=0, zdir="x")

    square12 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[3][0][2]],ec="black")
    ax.add_patch(square12)
    art3d.pathpatch_2d_to_3d(square12, z=0, zdir="x")

    square13 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[3][2][1]],ec="black")
    ax.add_patch(square13)
    art3d.pathpatch_2d_to_3d(square13, z=0, zdir="x")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[3][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=0, zdir="x")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[3][0][1]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=0, zdir="x")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[3][2][0]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=0, zdir="x")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[3][1][0]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=0, zdir="x")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[3][0][0]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=0, zdir="x")

    #red

    square10 = Rectangle((0, 0), 5,5, fc= colors[cube1.cube[2][2][0]],ec="black")
    ax.add_patch(square10)
    art3d.pathpatch_2d_to_3d(square10, z=0, zdir="y")

    square11 = Rectangle((0, 5), 5,5, fc= colors[cube1.cube[2][1][0]],ec="black")
    ax.add_patch(square11)
    art3d.pathpatch_2d_to_3d(square11, z=0, zdir="y")

    square12 = Rectangle((0, 10), 5,5, fc= colors[cube1.cube[2][0][0]],ec="black")
    ax.add_patch(square12)
    art3d.pathpatch_2d_to_3d(square12, z=0, zdir="y")

    square13 = Rectangle((5, 0), 5,5, fc= colors[cube1.cube[2][2][1]],ec="black")
    ax.add_patch(square13)
    art3d.pathpatch_2d_to_3d(square13, z=0, zdir="y")

    square5 = Rectangle((5, 5), 5,5, fc= colors[cube1.cube[2][1][1]],ec="black")
    ax.add_patch(square5)
    art3d.pathpatch_2d_to_3d(square5, z=0, zdir="y")

    square6 = Rectangle((5, 10), 5,5, fc= colors[cube1.cube[2][0][1]],ec="black")
    ax.add_patch(square6)
    art3d.pathpatch_2d_to_3d(square6, z=0, zdir="y")

    square7 = Rectangle((10, 0), 5,5, fc= colors[cube1.cube[2][2][2]],ec="black")
    ax.add_patch(square7)
    art3d.pathpatch_2d_to_3d(square7, z=0, zdir="y")

    square8 = Rectangle((10, 5), 5,5, fc= colors[cube1.cube[2][1][2]],ec="black")
    ax.add_patch(square8)
    art3d.pathpatch_2d_to_3d(square8, z=0, zdir="y")

    square9 = Rectangle((10, 10), 5,5, fc= colors[cube1.cube[2][0][2]],ec="black")
    ax.add_patch(square9)
    art3d.pathpatch_2d_to_3d(square9, z=0, zdir="y")






    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_zlim(0, 15)
    plt.axis('off')





