import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import cellpylib as cpl 

class Automaton:
    def __init__(self, rule, timesteps):
        valid_input = 0 < rule < 256
        if not valid_input:
            raise ValueError("Only inputs between 0 and 256 accectable")
        self.rule = rule 
        self.timesteps = timesteps

    def create(self):
        self.automaton = cpl.init_simple(200)
        self.cells = cpl.evolve(self.automaton, self.timesteps, memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, self.rule))
        return self.cells
    