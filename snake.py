from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)]

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            if position == (0, 0):
                self.part = Turtle("circle")
                self.part.color("black", "red")
                self.part.penup()
                self.part.goto(position)
                self.snake.append(self.part)
            else:
                self.add_part(position)


    def add_part(self, position):

        self.part = Turtle(shape="circle")
        self.part.color("red", "green")
        self.part.penup()
        self.part.goto(position)
        self.snake.append(self.part)

    def grow(self):
        self.add_part(self.snake[-1].position())

    def move(self):

        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].goto(new_x, new_y)

        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
