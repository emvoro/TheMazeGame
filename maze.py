class Maze:
    SIZE = 50
    M = 16
    N = 16
    doors = []
    maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 1, 5, 5, 5, 7, 5, 5, 5, 7, 1, 6, 'F', 'e', 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 'H', 1, 0, 1,
            1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 'b', 1, 'c', 1, 0, 1,
            1, 0, 1, 0, 'a', 'D', 'h', 1, 0, 'A', 0, 1, 1, 0, 0, 1,
            1, 6, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1,
            1, 5, 1, 0, 1, 7, 'f', 'E', 0, 1, 0, 1, 1, 0, 0, 1,
            1, 8, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1,
            1, 5, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'B', 1, 1, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
            1, 0, 'd', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            ]

    def draw(self, display_surf, image_surf, door_surf, key_surf, exit_surf, star_surf, bomb_surf, shield_surf, crystal_surf, potion_surf, life_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * self.SIZE, by * self.SIZE))
            if type(self.maze[bx + (by * self.M)]) is not int and str(self.maze[bx + (by * self.M)]).isupper():
                display_surf.blit(door_surf, (bx * self.SIZE, by * self.SIZE))
            if type(self.maze[bx + (by * self.M)]) is not int and not str(self.maze[bx + (by * self.M)]).isupper():
                display_surf.blit(key_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 4:
                display_surf.blit(star_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 5:
                display_surf.blit(bomb_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 6:
                display_surf.blit(shield_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 7:
                display_surf.blit(crystal_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 8:
                display_surf.blit(potion_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == 9:
                display_surf.blit(life_surf, (bx * self.SIZE, by * self.SIZE))
            if self.maze[bx + (by * self.M)] == -1:
                display_surf.blit(exit_surf, (bx * self.SIZE, by * self.SIZE))
            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1
