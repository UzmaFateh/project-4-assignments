# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
# We then create an eraser rectangle which, when dragged around the canvas, 
# sets all of the rectangles it is in contact with to white.

import tkinter as tk

class EraserCanvas:
    def __init__(self, master, rows, cols, cell_size):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.canvas = tk.Canvas(master, width=cols * cell_size, height=rows * cell_size, bg='white')
        self.canvas.pack()

        # Create a grid of blue cells
        self.cells = []
        for row in range(rows):
            row_cells = []
            for col in range(cols):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Create the eraser rectangle
        self.eraser_size = cell_size * 2  # Size of the eraser
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, fill='red', outline='black')

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        # Move the eraser rectangle
        x = event.x - self.eraser_size // 2
        y = event.y - self.eraser_size // 2
        self.canvas.coords(self.eraser, x, y, x + self.eraser_size, y + self.eraser_size)

        # Erase cells that the eraser is in contact with
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        # Calculate the range of cells to erase
        start_col = max(0, x // self.cell_size)
        end_col = min(self.cols, (x + self.eraser_size) // self.cell_size)
        start_row = max(0, y // self.cell_size)
        end_row = min(self.rows, (y + self.eraser_size) // self.cell_size)

        # Change the color of the cells to white
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                self.canvas.itemconfig(self.cells[row][col], fill='white')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Eraser on Canvas")
    eraser_canvas = EraserCanvas(root, rows=10, cols=10, cell_size=40)
    root.mainloop()