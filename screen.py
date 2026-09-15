import numpy as np
class Screen:
    def __init__(self, cells):
        self.cells = cells

    def render(self): 
        rows = np.shape(self.cells)[0]
        columns = np.shape(self.cells)[1]
        pretty_cells = [[0 for x in range(columns)] for x in range(rows)]
        columns_index = columns
        rows_index = rows
        for j in range(columns_index):
            for i in range(rows_index):
                if self.cells[i][j] == 1:
                    pretty_cells[i][j] = "#"
                else:
                    pretty_cells[i][j] = " "

        return pretty_cells

            