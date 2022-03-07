from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.scoreboard

    def scoreboard(self):
        self.write(arg=f"{self.score}", align="center",font=("Arial", 40, "bold"))
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()
      