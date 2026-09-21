import numpy as np

class Screen:
    def __init__(self, cells):
        self.cells = cells
        self.frames = []

    def turn_to_frames(self):
        number_of_rows = np.shape(self.cells)[0]
        for i in range(number_of_rows):
            self.frames.append(self.cells[i])
        return self.frames

    def display_frames_pretty(self):
        if len(self.frames) < 0:
            raise ValueError("Please create frames first by calling turn_to_frames function.")
        else:
            for i in range(len(self.frames) - 1):
                frame = self.frames[i]
                print(f"{self.render(frame)}\n")
        

    def render(self, cell): 
        number_of_rows = np.shape(self.cells)[0]
        pretty_cell = [0 for x in range(len(cell))]
        for i in range(len(cell)):
            if cell[i] == 1:
                pretty_cell[i] = "#"
            else:
                pretty_cell[i] = " "

        return " ".join(pretty_cell)

