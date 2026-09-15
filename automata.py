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

    def choose_automaton(self, rule):
        match rule:
            case 30: 
                return self.create(30)
            case 50:
                return self.create(50)
            case 70:
                return self.create(70)
            case _:
                raise ValueError("Input must be 30, 50, or 70.")

    
            