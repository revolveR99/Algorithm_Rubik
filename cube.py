import numpy as np
from random import randint

#                            U
#                    [['U0' 'U1' 'U2']]
#                    [['U3' 'U4' 'U5']]
#                    [['U6' 'U7' 'U8']]
#         L                  F                  R                  B
# [['L0' 'L1' 'L2']] [['F0' 'F1' 'F2']] [['R0' 'R1' 'R2']] [['B0' 'B1' 'B2']]    [[0 * 2]]                          <-┐  
# [['L3' 'L4' 'L5']] [['F3' 'F4' 'F5']] [['R3' 'R4' 'R5']] [['B3' 'B4' 'B5']]    [[3 4 5]]              rot90 * ->    |
# [['L6' 'L7' 'L8']] [['F6' 'F7' 'F8']] [['R6' 'R7' 'R8']] [['B6' 'B7' 'B8']]    [[6 7 8]]
#                            D
#                    [['D0' 'D1' 'D2']]
#                    [['D3' 'D4' 'D5']]
#                    [['D6' 'D7' 'D8']]
# Initialize the Cube and reset its faces to default positions
class Cube:
    def __init__(self):
        self.reset()
        self.faces = {"F" : self.FRONT, "R": self.RIGHT, "U": self.UP, "B": self.BACK, "L": self.LEFT, "D": self.DOWN}
# Resets the cube's faces to the default solved state
    def reset(self):
        self.face_left = np.matrix([["L0", "L1", "L2"], ["L3", "L4", "L5"], ["L6", "L7", "L8"]])
        self.face_right = np.matrix([["R0", "R1", "R2"], ["R3", "R4", "R5"], ["R6", "R7", "R8"]])
        self.face_front = np.matrix([["F0", "F1", "F2"], ["F3", "F4", "F5"], ["F6", "F7", "F8"]])
        self.face_up = np.matrix([["U0", "U1", "U2"], ["U3", "U4", "U5"], ["U6", "U7", "U8"]])
        self.face_down = np.matrix([["D0", "D1", "D2"], ["D3", "D4", "D5"], ["D6", "D7", "D8"]])
        self.face_back = np.matrix([["B0", "B1", "B2"], ["B3", "B4", "B5"], ["B6", "B7", "B8"]])
 # Returns a dictionary of all cube faces
    def sides(self):
        sides = {"F" : self.face_front, "R": self.face_right, "U": self.face_up, "B": self.face_back, "L": self.face_left, "D": self.face_down}
        return (sides)
 # Displays the cube's current state in a readable format
    def printCube(self):
        a = f"""
                                   U
                           {self.face_up[0]}
                           {self.face_up[1]}
                           {self.face_up[2]}
                L                  F                  R                  B
        {self.face_left[0]} {self.face_front[0]} {self.face_right[0]} {self.face_back[0]}
        {self.face_left[1]} {self.face_front[1]} {self.face_right[1]} {self.face_back[1]}
        {self.face_left[2]} {self.face_front[2]} {self.face_right[2]} {self.face_back[2]}
                                   D
                           {self.face_down[0]}
                           {self.face_down[1]}
                           {self.face_down[2]}
        """
        print(a)
        return
 # Copies the state of another cube into this one
    def copy(self, cube: 'Cube'):
        self.face_front = cube.face_front.copy()
        self.face_right = cube.face_right.copy()
        self.face_back = cube.face_back.copy()
        self.face_left = cube.face_left.copy()
        self.face_up = cube.face_up.copy()
        self.face_down = cube.face_down.copy()
        
 # Inverts positions of opposite faces for prime rotations
    def primeInvert(self, faces):
        f_tmp = faces[1]
        faces[1] = faces[3]
        faces[3] = f_tmp
        return (faces)
 # Rotates the U (Up) face clockwise or counterclockwise (prime)
    def UP(self, prime=False):
        face = self.face_up
        faces = [self.face_back, self.face_left, self.face_front, self.face_right]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][0] = faces[i+1][0]
        self.face_up = face
 # Rotates the D (Down) face clockwise or counterclockwise (prime)   
    def DOWN(self, prime=False):
        face = self.face_down
        faces = [self.face_back, self.face_right, self.face_front, self.face_left]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][2] = faces[i+1][2]
        self.face_down = face
# Rotates the R (Right) face clockwise or counterclockwise (prime)   
    def RIGHT(self, prime=False):
        face = self.face_right
        faces = [np.rot90(self.face_back, k=2), self.face_up, self.face_front, self.face_down]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 2] = faces[i+1][:, 2]
        self.face_right = face
 # Rotates the L (Left) face clockwise or counterclockwise (prime)
    def LEFT(self, prime=False):
        face = self.face_left
        faces = [np.rot90(self.face_back, k=2), self.face_down, self.face_front, self.face_up]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 0] = faces[i+1][:, 0]
        self.face_left = face
# Rotates the F (Front) face clockwise or counterclockwise (prime)
    def FRONT(self, prime=False):
        face = self.face_front
        faces = [np.rot90(self.face_left, k=2), np.rot90(self.face_down), self.face_right, np.rot90(self.face_up, k=-1)]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 0] = faces[i+1][:, 0]
        self.face_front = face
# Rotates the B (Back) face clockwise or counterclockwise (prime)   
    def BACK(self, prime=False):
        face = self.face_back
        faces = [np.rot90(self.face_left, k=2), np.rot90(self.face_up, k=-1), self.face_right, np.rot90(self.face_down)]
        tmp = faces[0].copy()
        faces.append(tmp)
        if prime == False:
            face = np.rot90(face, k=-1)
        else:
            faces = self.primeInvert(faces)
            face = np.rot90(face, k=1)
        for i in range(4):
            faces[i][:, 2] = faces[i+1][:, 2]
        self.face_back = face
# Reverses a scramble pattern of moves for the cube
    def reverseScramble(self, pattern):
        faces = ["F", "R", "U", "B", "L", "D"]
        moves = pattern.split()
        reversed = []
        l = len(moves)
        for i in range(l):
            move = moves[l - 1 - i]
            if len(move) > 2 or not move[0] in faces or (len(move) == 2 and (move[1] != "2" and move[1] != "'")):
                print(f"{move} not existing")
                return
            if len(move) == 1:
                move = move + "'"
            elif len(move) == 2 and move[1] == "'":
                move = move[0]
            reversed.append(move)
        return(" ".join(reversed))
 # Reduces unnecessary or repeated moves in a scramble pattern
    def reducePattern(self, pattern: str):
        if len(pattern.strip().split()) == 1:
            return (pattern)
        p = pattern.strip().split()
        change = 1
        reduced = []
        while change > 0 and len(p) > 1:
            change = 0
            reduced = []
            i = 0
            while i < len(p) - 1:
                if p[i][0] == p[i + 1][0]:
                    change = 1
                    if len(p[i]) == 1:
                        p[i] = p[i] + "0"
                    if len(p[i+1]) == 1:
                        p[i + 1] = p[i + 1] + "0"
                    if p[i][1] == "2" and p[i+1][1] == "2":
                        pass
                    elif p[i][1] == "0" and p[i+1][1] == "0":
                        reduced.append(p[i][0] + "2")
                    elif p[i][1] == "'" and p[i+1][1] == "'":
                        reduced.append(p[i][0] + "2")
                    elif (p[i][1] == "2" and p[i+1][1] == "'") or (p[i+1][1] == "2" and p[i][1] == "'"):
                        reduced.append(p[i][0])
                    elif (p[i][1] == "2" and p[i+1][1] == "0") or (p[i+1][1] == "2" and p[i][1] == "0"):
                        reduced.append(p[i][0] + "'")
                    elif (p[i][1] == "'" and p[i+1][1] == "0") or (p[i+1][1] == "'" and p[i][1] == "0"):
                        pass
                    i += 1
                else:
                    reduced.append(p[i])
                i += 1
            if i == len(p) - 1:
                reduced.append(p[i])
            p = reduced
                    
        return(" ".join(reduced).strip())
 # Generates a random scramble pattern of 'nb_moves' moves
    def random(self, nb_moves=randint(1, 40)):
        faces = ["F", "R", "U", "B", "L", "D"]
        extras = ["", "'", "2"]
        pattern = ""
        for i in range(nb_moves):
            pattern = pattern + " " + faces[randint(0, 5)] + extras[randint(0, 2)]
        return (pattern)
# Scrambles the cube with a random sequence of moves
    def scramble(self, pattern: str):
        moves = pattern.split()
        for move in moves:
            if len(move) > 2 or not move[0] in self.faces or (len(move) == 2 and (move[1] != "2" and move[1] != "'")):
                print(f"{move} not existing")
                return
            else:
                if len(move) == 2:
                    if move[1] == "'":
                        self.faces[move[0]](True)
                    elif move[1] == "2":
                        self.faces[move[0]]()
                        self.faces[move[0]]()
                else:
                    self.faces[move[0]]()
        return


    def solver():
        pass
    