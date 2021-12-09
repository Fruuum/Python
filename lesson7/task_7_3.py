class Cell:
    def __init__(self, quantity_cell):
        self.num_cells = quantity_cell

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        if other.num_cells <= self.num_cells:
            return self.num_cells - other.num_cells
        else:
            return "Error in the action. Quantity of cell couldn't be less than zero"

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def __floordiv__(self, other):
        if other.num_cells > 0:
            return self.num_cells // other.num_cells
        else:
            return "Zero division Error"

    def make_order(self, rows):
        return "\n".join(("@" * rows for _ in range(self.num_cells // rows))) + "\n" + "@" * (self.num_cells % rows)


cell_1 = Cell(23)
cell_2 = Cell(19)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(6))
