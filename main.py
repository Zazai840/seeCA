import sys
from automata import *
import cellpylib as cpl

def main():
    rule = int(sys.argv[1])
    automaton = Automaton(rule)
    automaton = automaton.create()
    cpl.plot(automaton)

if __name__ == "__main__":
    main()