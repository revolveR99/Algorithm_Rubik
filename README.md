# Rubik
## 42 project - rubik's cube solver
---

## Sources and solution steps:
    F: Front, L: Left, B: Back, R: Right, U: Up, D: Down
    One letter : 1/4 rotation clockwise on that face
    One letter + ': 1/4 rotation counterclockwise
    One letter + 2: 1/2 rotation
    eg: F2 R L' F U B2 D' 
    (E: Edge, C: Corner)


https://www.speedsolving.com/wiki/index.php/Thistlethwaite%27s_algorithm
https://math.stackexchange.com/questions/1362471/rubiks-cube-thistlethwaite-four-phase-algorithm


## Phase 1 <U,D,L,R,F2,B2> F and B to switch BAD to GOOD and GOOD to BAD
    EO (edge orientation) : all edge to good pos, (ZZ method) 7 moves worst case
https://www.speedsolving.com/wiki/index.php/Edge_Orientation#ZZ


## Phase 2 <U,D,L,R,F2,B2> 
    Corner orientation :  10 moves worst case
### 2.1 placement of U/D edges in U/D faces (whatever if it's U or D just place it on U or D)
### 2.2 Corner Orientation
https://www.cuberoot.me/dr-trigger/

## Phase 3 <U,D,L2,R2,F2,B2>
    Every colors are on there face or the opposit, 13 moves worst case
https://www.ryanheise.com/cube/human_thistlethwaite_algorithm.html
### 3.1 Corners
### 3.2 Edges


## Phase 4 <U2,D2,L2,R2,F2,B2> 
    Final resolution : 15 moves worst case

---
# Usage

    $ python3 rubik.py <str>
Place the scramble pattern as argument

The solution will be printed in the shell and you'll be able to open the 3D modelization

Press 'S' to Scramble, then 'R' to Solve the 3D cube.

You can use '+/-' keys to change animation speed

    $ python3 rubik3D.py
It will open the 3D visualizer without pattern.
Press 'F/L/B/R/U/D' to move the faces ('shift + key' for reverse)