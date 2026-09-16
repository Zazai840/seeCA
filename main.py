import sys
from automata import *
from screen import Screen

def main():
    input = sys.argv
    rule = int(input[1])
    timestep = int(input[2]) #Take intput from user
    automaton = Automaton(rule, timestep)
    cells = automaton.create()
    # automaton.animation() leave annimation out of terminal display for now
    screen = Screen(cells)
    screen.animate()
    # print(screen.render())
    

if __name__ == "__main__":
    main()