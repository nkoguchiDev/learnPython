class Node:
    def __init__(self, data):
        self.age = 0
        self.x_axis = 0
        self.y_axis = 0

    def move(self, x, y):
        self.x_axis = x
        self.y_axis = y
