from turtle import Turtle


class CpuPlank(Turtle):

    def __init__(self):
        super().__init__()
        self.create_plank()

    def create_plank(self):
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(350, 0)
        

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)
        else:
            self.goto(self.xcor(), self.ycor() + 0)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
        else:
            self.goto(self.xcor(), self.ycor() - 0)


            
    
        