from pprint import pprint as pp
import numpy as np

# white = 0, blue = 1, red = 2, green = 3, orange = 4, yellow = 5
# front = blue, back = green



class Cube:
    def __init__(self, cube_size):
        self.cube = []

        #initializing cube
        for i in range(6):
            self.cube.append([])

        for face in self.cube:
            for i in range(cube_size):
                face.append([])


        a = 0

        for face in self.cube:
            for row in face:
                for i in range(cube_size):
                    row.append(a)
            a += 1

        self.cube = np.array(self.cube)
        

    #wrong way tho...all of them I think
    def turn_UR(self):
        old_cube = self.cube.copy()
        self.cube[0] = np.rot90(old_cube[0])
        self.cube[4][0] = old_cube[1][0]
        self.cube[3][0] = old_cube[4][0]
        self.cube[2][0] = old_cube[3][0]
        self.cube[1][0] = old_cube[2][0]

    def turn_DR(self):
        old_cube = self.cube.copy()
        self.cube[5] = np.rot90(old_cube[5])
        self.cube[4][2] = old_cube[3][2]
        self.cube[3][2] = old_cube[2][2]
        self.cube[2][2] = old_cube[1][2]
        self.cube[1][2] = old_cube[4][2]

        #oh now it works
    def turn_FR(self):
        old_cube = self.cube.copy()
        self.cube[1] = np.rot90(old_cube[1])
        self.cube[2][:,2] = old_cube[0][2][::-1]
        self.cube[5][0] = old_cube[2][:,2]
        self.cube[4][:,0] = old_cube[5][0][::-1]
        self.cube[0][2] = old_cube[4][:,0]

    def turn_BR(self):
        old_cube = self.cube.copy()
        self.cube[3] = np.rot90(old_cube[3])
        self.cube[2][:,0] = old_cube[5][2]
        self.cube[5][2] = old_cube[4][:,2][::-1]
        self.cube[4][:,2] = old_cube[0][0]
        self.cube[0][0] = old_cube[2][:,0][::-1]

    def turn_RR(self):
        old_cube = self.cube.copy()
        self.cube[4] = np.rot90(old_cube[4])
        self.cube[1][:,2] = old_cube[0][:,2]
        self.cube[3][:,0] = old_cube[5][:,2][::-1]
        self.cube[5][:,2] = old_cube[1][:,2]
        self.cube[0][:,2] = old_cube[3][:,0][::-1]

    def turn_LR(self):
        old_cube = self.cube.copy()
        self.cube[2] = np.rot90(old_cube[2])
        self.cube[1][:,0] = old_cube[5][:,0]
        self.cube[5][:,0] = old_cube[3][:,2][::-1]
        self.cube[3][:,2] = old_cube[0][:,0][::-1]
        self.cube[0][:,0] = old_cube[1][:,0]
    #now actual moves

    def turn_U(self):
        self.turn_UR()
        self.turn_UR()
        self.turn_UR()
    def turn_D(self):
        self.turn_DR()
        self.turn_DR()
        self.turn_DR()
    def turn_F(self):
        self.turn_FR()
        self.turn_FR()
        self.turn_FR()
    def turn_B(self):
        self.turn_BR()
        self.turn_BR()
        self.turn_BR()
    def turn_L(self):
        for i in range(3):
            self.turn_LR()
        
    def turn_R(self):
        self.turn_RR()
        self.turn_RR()
        self.turn_RR()

    #ok and double moves
    def turn_U2(self):
        self.turn_UR()
        self.turn_UR()

    def turn_D2(self):
        self.turn_DR()
        self.turn_DR()
        
    def turn_F2(self):
        self.turn_FR()
        self.turn_FR()

    def turn_B2(self):
        self.turn_BR()
        self.turn_BR()

    def turn_L2(self):
        self.turn_LR()
        self.turn_LR()

    def turn_R2(self):
        self.turn_RR()
        self.turn_RR()



    


cube = Cube(3)

cube.turn_U()

print(cube.cube)




#turn cube
        
        