from maze import Maze
import math


class Player:
    SIZE = 30
    delta = .8
    game_over = False
    key = None
    stars = 0
    isWon = False
    lives = 1
    shields = 0
    crystals = 0

    x = Maze.SIZE
    y = Maze.SIZE

    def move_right(self):
        new_block_index = -1
        current_col = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        left_pos_of_right_col = (current_col + 1) * Maze.SIZE
        occupied_row1 = int(math.floor(self.y) / Maze.SIZE)
        occupied_row2 = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        dest_x = self.x + self.SIZE + self.delta
        for row in range(occupied_row1, occupied_row2 + 1):
            if current_col < Maze.M - 1 and Maze.maze[row * 16 + current_col + 1] == 1 or current_col == Maze.M - 1:
                dest_x = min(dest_x, left_pos_of_right_col)
            if current_col < Maze.M - 1 and (type(Maze.maze[row * 16 + current_col + 1]) is not int and str(Maze.maze[row * 16 + current_col + 1]).isupper()) or current_col == Maze.M - 1:
                dest_x = min(dest_x, left_pos_of_right_col)
            new_block_index = row * 16 + current_col
        self.x = dest_x - self.SIZE
        return new_block_index

    def move_left(self):
        new_block_index = -1
        current_col = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        right_pos_of_left_col = current_col * Maze.SIZE
        occupied_row1 = int(math.floor(self.y) / Maze.SIZE)
        occupied_row2 = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        dest_x = self.x - self.delta
        for row in range(occupied_row1, occupied_row2 + 1):
            if current_col > 0 and Maze.maze[row * 16 + current_col - 1] == 1 or current_col == 0:
                dest_x = max(dest_x, right_pos_of_left_col)
            if current_col > 0 and (type(Maze.maze[row * 16 + current_col - 1]) is not int and str(Maze.maze[row * 16 + current_col - 1]).isupper()) or current_col == 0:
                dest_x = max(dest_x, right_pos_of_left_col)
            new_block_index = row * 16 + current_col
        self.x = dest_x
        return new_block_index

    def move_up(self):
        new_block_index = -1
        current_row = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        bottom_pos_of_upper_row = current_row * Maze.SIZE
        occupied_col1 = int(math.floor(self.x) / Maze.SIZE)
        occupied_col2 = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        dest_y = self.y - self.delta
        for col in range(occupied_col1, occupied_col2 + 1):
            if current_row > 0 and Maze.maze[(current_row - 1) * 16 + col] == 1 or current_row == 0:
                dest_y = max(dest_y, bottom_pos_of_upper_row)
            if current_row > 0 and (type(Maze.maze[(current_row - 1) * 16 + col]) is not int and str(Maze.maze[(current_row - 1) * 16 + col]).isupper()) or current_row == 0:
                dest_y = max(dest_y, bottom_pos_of_upper_row)
            new_block_index = current_row * 16 + col
        self.y = dest_y
        return new_block_index

    def move_down(self):
        new_block_index = -1
        current_row = int(math.ceil(self.y + self.SIZE - 1) / Maze.SIZE)
        top_pos_of_lower_row = (current_row + 1) * Maze.SIZE
        occupied_col1 = int(math.floor(self.x) / Maze.SIZE)
        occupied_col2 = int(math.ceil(self.x + self.SIZE - 1) / Maze.SIZE)
        dest_y = self.y + self.SIZE + self.delta
        for col in range(occupied_col1, occupied_col2 + 1):
            if current_row < Maze.N - 1 and Maze.maze[(current_row + 1) * 16 + col] == 1 or current_row == Maze.N - 1:
                dest_y = min(dest_y, top_pos_of_lower_row)
            if current_row < Maze.N - 1 and (type(Maze.maze[(current_row + 1) * 16 + col]) and str(Maze.maze[(current_row + 1) * 16 + col]).isupper()) or current_row == Maze.N - 1:
                dest_y = min(dest_y, top_pos_of_lower_row)
            new_block_index = current_row * 16 + col
        self.y = dest_y - self.SIZE
        return new_block_index
