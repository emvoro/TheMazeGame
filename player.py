from maze import Maze
import math


class Player:
    SIZE = 30
    DELTA = .3

    x = Maze.SIZE
    y = Maze.SIZE

    def move_right(self):
        current_col = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        left_pos_of_right_col = (current_col + 1) * Maze.SIZE
        occupied_row1 = int(math.floor(self.y) / Maze.SIZE)
        occupied_row2 = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        dest_x = self.x + self.SIZE + self.DELTA
        for row in range(occupied_row1, occupied_row2 + 1):
            if current_col < Maze.M - 1 and Maze.MAZE[row * 12 + current_col + 1] == 1 or current_col == Maze.M - 1:
                dest_x = min(dest_x, left_pos_of_right_col)
        self.x = dest_x - self.SIZE

    def move_left(self):
        current_col = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        right_pos_of_left_col = current_col * Maze.SIZE
        occupied_row1 = int(math.floor(self.y) / Maze.SIZE)
        occupied_row2 = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        dest_x = self.x - self.DELTA
        for row in range(occupied_row1, occupied_row2 + 1):
            if current_col > 0 and Maze.MAZE[row * 12 + current_col - 1] == 1 or current_col == 0:
                dest_x = max(dest_x, right_pos_of_left_col)
        self.x = dest_x

    def move_up(self):
        current_row = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        bottom_pos_of_upper_row = current_row * Maze.SIZE
        occupied_col1 = int(math.floor(self.x) / Maze.SIZE)
        occupied_col2 = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        dest_y = self.y - self.DELTA
        for col in range(occupied_col1, occupied_col2 + 1):
            if current_row > 0 and Maze.MAZE[(current_row - 1) * 12 + col] == 1 or current_row == 0:
                dest_y = max(dest_y, bottom_pos_of_upper_row)
        self.y = dest_y

    def move_down(self):
        current_row = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        top_pos_of_lower_row = (current_row + 1) * Maze.SIZE
        occupied_col1 = int(math.floor(self.x) / Maze.SIZE)
        occupied_col2 = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        dest_y = self.y + self.SIZE + self.DELTA
        for col in range(occupied_col1, occupied_col2 + 1):
            if current_row < Maze.N - 1 and Maze.MAZE[(current_row + 1) * 12 + col] == 1 or current_row == Maze.N - 1:
                dest_y = min(dest_y, top_pos_of_lower_row)
        self.y = dest_y - self.SIZE

        # print(str(self.x + self.SIZE) + ":" + str(math.floor(self.y)) + " - " + str(math.ceil(self.y + self.SIZE)))
        # print("Col: " + str(current_col) + " ->| " + str(left_pos_of_right_col))
        # print("Height: " + str(math.floor(self.y)) + " -> " + str(math.ceil(self.y + Maze.SIZE - 1)))
        # print("Rows: " + str(occupied_row1) + " -> " + str(occupied_row2))
        # print("Dest X: " + str(dest_x) + " (" + str(self.x + self.SIZE) + ")")
        # print("Maze:" + str(row * 12 + current_col + 1) + ": " + str(Maze.MAZE[row * 12 + current_col + 1]))
        # print("Maze[" + str(row) + "," + str(current_col + 1) + "]: " + str(Maze.MAZE[row * 12 + current_col + 1]))
        # print("New dest X: " + str(dest_x))
        # print("Dest X: " + str(dest_x))
        # print(self.x)
        # ---
        # print(str(self.x) + ":" + str(math.floor(self.y)) + " - " + str(math.ceil(self.y + Maze.SIZE)))
        # print("Col: " + str(current_col) + " |-> " + str(right_pos_of_left_col))
        # print("Height: " + str(math.floor(self.y)) + " -> " + str(math.ceil(self.y + Maze.SIZE - 1)))
        # print("Rows: " + str(occupied_row1) + " -> " + str(occupied_row2))
        # print("Dest X: " + str(dest_x) + " " + str(self.x - self.DELTA))
        # print("Maze:" + str(row * 12 + current_col + 1) + ": " + str(Maze.MAZE[row * 12 + current_col + 1]))
        # print("Maze[" + str(row) + "," + str(current_col - 1) + "]: " + str(Maze.MAZE[row * 12 + current_col - 1]))
        # print("New dest X: " + str(dest_x))
        # print("Dest X: " + str(dest_x))
        # ---
        # print(str(self.x) + ":" + str(math.floor(self.y)) + " - " + str(math.ceil(self.y + Maze.SIZE)))
        # print("Col: " + str(current_row) + " T " + str(bottom_pos_of_upper_row))
        # print("Height: " + str(math.floor(self.y)) + " -> " + str(math.ceil(self.y + Maze.SIZE - 1)))
        # print("Cols: " + str(occupied_col1) + " -> " + str(occupied_col2))
        # print("Dest Y: " + str(dest_y))
        # print("Maze:" + str(row * 12 + current_col + 1) + ": " + str(Maze.MAZE[row * 12 + current_col + 1]))
        # print("Maze[" + str(row) + "," + str(current_col - 1) + "]: " + str(Maze.MAZE[row * 12 + current_col - 1]))
        # print("New dest Y: " + str(dest_y))
        # print("Dest Y: " + str(dest_y))
        # ---
        # self.y = self.y + self.DELTA
        # print(str(self.x + self.SIZE) + ":" + str(math.floor(self.y)) + " - " + str(math.ceil(self.y + self.SIZE)))
        # print("Row: " + str(current_row) + " _ " + str(top_pos_of_lower_row))
        # print("Height: " + str(math.floor(self.y)) + " -> " + str(math.ceil(self.y + Maze.SIZE - 1)))
        # print("Cols: " + str(occupied_col1) + " -> " + str(occupied_col2))
        # print("Dest Y: " + str(dest_y))
        # print("Maze:" + str((current_row + 1) * 12 + col) + ": " + str(Maze.MAZE[(current_row + 1) * 12 + col]))
        # print("Maze[" + str(current_row + 1) + "," + str(col) + "]: " + str(Maze.MAZE[(current_row + 1) * 12 + col]))
        # print("New dest Y: " + str(dest_y))
        # print("Dest Y: " + str(dest_y))
