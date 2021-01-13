class Maze:
    SIZE = 50
    M = 12
    N = 10
    MAZE = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
            1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1,
            1, 0, 1, 0, 0, 0, 3, 1, 0, 2, 0, 1,
            1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1,
            1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            ]

    # def __init__(self):
        # print("Maze.__init__...")
        # self.M = 12
        # self.N = 10

    def draw(self, display_surf, image_surf, door_surf, key_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.MAZE[bx + (by * self.M)] == 1:
                display_surf.blit(image_surf, (bx * self.SIZE, by * self.SIZE))
            if self.MAZE[bx + (by * self.M)] == 2:
                display_surf.blit(door_surf, (bx * self.SIZE, by * self.SIZE))
            if self.MAZE[bx + (by * self.M)] == 3:
                display_surf.blit(key_surf, (bx * self.SIZE, by * self.SIZE))
            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1
