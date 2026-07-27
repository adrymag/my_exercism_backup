# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4

right_side = {
    EAST : SOUTH,
    NORTH : EAST,
    SOUTH : WEST,
    WEST : NORTH
}

left_side = {
    SOUTH : EAST,
    EAST : NORTH,
    WEST : SOUTH,
    NORTH : WEST
}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, instructions):
        for letter in instructions:
            if letter == 'R':
                self.direction = right_side[self.direction]
                # if self.direction == NORTH:
                    # self.direction = EAST
            if letter == 'L':
                self.direction = left_side[self.direction]
            if letter == "A":
                if self.direction == EAST:
                    self.x_pos += 1
                if self.direction == WEST:
                    self.x_pos -= 1
                if self.direction == NORTH:
                    self.y_pos += 1
                if self.direction == SOUTH:
                    self.y_pos -= 1
                self.coordinates = (self.x_pos, self.y_pos)