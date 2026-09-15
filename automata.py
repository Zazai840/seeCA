import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import cellpylib as cpl 

class Automaton:
    def __init__(self, rule):
        allowed_rules = [30, 50, 70, 90]
        if rule not in allowed_rules:
            raise ValueError("Only 30, 50, 70, and 90 are appropriate inputs.")

        self.rule = rule 

    def create(self):
        self.automaton = cpl.init_simple(200)
        self.timesteps = 30
        self.cells = cpl.evolve(self.automaton, self.timesteps, memoize=True,
                                apply_rule=lambda n, c, t: cpl.nks_rule(n, self.rule))
        return self.cells

    # def plot(self.cells) -> None:
    #     cpl.plot(self.cells)
    def animation(self):
        fig, ax = plt.subplots()
        mat = ax.matshow(self.cells, cmap='binary')
        plt.axis('off')

        def animate(i):
            mat.set_data(self.cells[:i+1])
            return [mat]
        ani = animation.FuncAnimation(fig, animate, frames = 30, interval = 50,
                                      blit = True, repeat=False)
        plt.show()
    