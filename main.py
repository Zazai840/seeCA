import sys
from automata import *
from screen import Screen

def main():
    rule = int(sys.argv[1])
    automaton = Automaton(rule)
    cells = automaton.create()
    # automaton.animation() leave annimation out of terminal display for now
    screen = Screen(cells)
    print(screen.render())
    

if __name__ == "__main__":
    main()