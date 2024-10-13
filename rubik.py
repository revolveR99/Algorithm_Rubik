from cube import Cube
from solver import solver
from rubik3D import Game
import time
import sys

def main():
    # Check if a scramble pattern was provided as a command-line argument
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    else:
        # If no pattern provided, prompt the user
        print("Please enter a scramble pattern")
        return
    
    # Create a new Cube instance and scramble it with the given pattern
    cube = Cube()
    print(f'input: {pattern}')
    cube.scramble(pattern)
    
    # Measure the time it takes to solve the cube
    start = time.time()
    solved = solver(cube)
    print(solved)
    print(f"len: {len(solved.split(' '))}")
    end = time.time()
    print(f"Time elapsed: {end - start}")
    # cube.printCube() # Optional cube state print
    
    # Ask the user if they want to display a 3D render of the solution
    graph = input("Do you want to display 3D render ? y/n\n")
    if graph == "y":
        game = Game()
        game.setScramble(pattern)
        game.setSolver(solved)
        game.game_mode = "solver"
        game.run()
    return

# If script is run directly, execute the main function
if __name__ == "__main__":
    main()
