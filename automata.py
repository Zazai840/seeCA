import matplotlib as plt 
import cellpylib as cpl 

class Automaton:
    def __init__(self, rule):
        # invalid_input = rule != 30 or rule != 50 or rule != 70 or rule != 90
        # if invalid_input:
        #     raise ValueError("Input limited to following rules: 30, 50, 70, 90")
        # Not sure why this check does not work. Even after entering the correct
        # values, the ValueError is raised. 
        self.rule = rule 

    def create(self):
        automaton = cpl.init_simple(200)
        timesteps = 100
        automaton = cpl.evolve(automaton, timesteps, memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, self.rule))
        return automaton

    def create_plot(self):
        return cpl.plot(self)

            