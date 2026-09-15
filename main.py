import sys
from automata import *
import cellpylib as cpl

def main():
    rule = int(sys.argv[1])
    automaton = Automaton(rule)
    automaton.create()
    automaton.animation()
    

if __name__ == "__main__":
    main()