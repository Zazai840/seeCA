import matplotlib as plt 
import cellpylib as cpl 

class Automaton:
    def __init__(self, rule):
        self.rule = rule 

    def create(rule):
        automaton = cpl.init_simple(200)
        timesteps = 100
        automaton = cpl.evolve(automaton, timesteps, memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, rule))

        return automaton
