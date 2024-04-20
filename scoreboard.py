from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-30, 230)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.write(f"score : {self.score}", font=('Arial', 15, 'normal'))


    def update_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", font=('Arial', 15, 'normal'))


