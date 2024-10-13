from cube import Cube
from random import shuffle

class TreeCube:
    def __init__(self, cube: Cube, run, allowed=["F", "R", "U", "B", "L", "D"], move=""):
        # Initialize TreeCube object with a cube state, run condition, allowed moves, and the current move.
        # Restricts opposite face moves (e.g. F > B, U > D, R > L) and prevents double moves on the same face.
        self.run = run  # Thread condition to control search
        self.childs = []  # List of child nodes (next states)
        self.cube = cube  # Current cube state
        self.move = move  # Last move applied to the cube
        self.depth = 0  # Depth of the current node in the search tree
        self.max_depth = 0  # Maximum depth to explore
        self.all_allowed = allowed.copy()  # All possible allowed moves
        self.moves = {  # Dictionary linking moves to rotation methods
            "F": self.rotate, "R": self.rotate, "U": self.rotate, "B": self.rotate, "L": self.rotate, "D": self.rotate,
            "F'": self.prime, "R'": self.prime, "U'": self.prime, "B'": self.prime, "L'": self.prime, "D'": self.prime,
            "F2": self.double, "R2": self.double, "U2": self.double, "B2": self.double, "L2": self.double, "D2": self.double,
        }
        # Filter out moves that reverse the last move (e.g., don't move the same face twice consecutively).
        if self.move != "":
            allowed = [k for k in allowed if k[0] != self.move[0]]
            if self.move[0] == "B":
                allowed = [k for k in allowed if k[0] != "F"]
            elif self.move[0] == "D":
                allowed = [k for k in allowed if k[0] != "U"]
            elif self.move[0] == "L":
                allowed = [k for k in allowed if k[0] != "R"]
        self.allowed = allowed.copy()  # List of allowed moves after filtering
        for i in allowed:
            # Add prime and double moves for each allowed face
            if len(i) == 1:
                if i + "'" not in self.allowed:
                    self.allowed.append(i + "'")
                if i + "2" not in self.allowed:
                    self.allowed.append(i + "2")

    def appendChild(self, child):
        # Add a child node (next state) to the current node's children
        self.childs.append(child)

    def rotate(self, face, prime=False, double=False):
        # Perform rotation on the cube for a given face, handling prime (reverse) and double moves
        cube = Cube()  # Create a new cube instance
        cube.copy(self.cube)  # Copy the current cube's state
        if prime:
            cube.faces[face](True)  # Rotate the face in reverse if prime is True
        elif double:
            cube.faces[face]()  # Rotate the face twice for a double move
            cube.faces[face]()
        else:
            cube.faces[face]()  # Regular face rotation
        return cube

    def prime(self, face):
        # Rotate the cube face in reverse (prime)
        return self.rotate(face, prime=True)

    def double(self, face):
        # Rotate the cube face twice (double move)
        return self.rotate(face, double=True)

    def searchChilds(self, func, **kwargs):
        # Search for children by applying allowed moves and checking if the goal is met
        for move in self.allowed:
            cube = self.moves[move](move[0])  # Apply a move and generate the new cube state
            node = TreeCube(cube, self.run, allowed=self.all_allowed, move=move)  # Create a new child node
            node.depth = self.depth + 1  # Set the depth of the child node
            self.childs.append(node)  # Add the child to the current node's children
            # If the current cube state satisfies the goal condition, return the move
            if func(cube, **kwargs):
                return move

    def nextDepth(self, depth, func, **kwargs):
        # Recursively explore the search tree up to a specified depth
        while self.depth <= depth and self.run.is_set():  # Continue search as long as depth limit is not reached and run is set
            if self.depth < depth:
                for child in self.childs:
                    m = child.nextDepth(depth, func, **kwargs)  # Explore the next depth level
                    if m is not None:
                        return self.move + " " + m  # Return the move sequence if found
            else:
                m = self.searchChilds(func, **kwargs)  # Search at the current depth
                if m is not None:
                    return self.move + " " + m  # Return the move sequence if found
                return
            if self.depth == 0:
                depth += 1  # Increase depth for the next iteration if at root level
            else:
                return

    def search(self, func, **kwargs):
        # Initiate search for a solution by exploring children
        m = self.searchChilds(func, **kwargs)  # Search for a solution
        if m is not None:
            return self.move + " " + m  # Return the solution move sequence if found
        return self.nextDepth(1, func, **kwargs)  # If not found, continue exploring deeper
