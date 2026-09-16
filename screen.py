import numpy as np
class Screen:
    def __init__(self, cells):
        self.cells = cells

    def animate(self):
        frames = []
        number_of_rows = np.shape(self.cells)[0]
        for i in range(number_of_rows):
            frames.append(self.cells[i])
        for i in range(len(frames) - 1):
            frame = frames[i]
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
        # columns_index = columns
        # rows_index = number_of_rows
        # for j in range(columns_index):
        #     for i in range(rows_index):
        #         if cell[i][j] == 1:
        #             pretty_cells[i][j] = "#"
        #         else:
        #             pretty_cells[i][j] = " "
    
        


        
        
