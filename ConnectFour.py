# Created by Carina Claassen

import turtle


class FullSpace:

    def __init__(self, x, y, player):
        self.empty = False
        self.player = player
        self.x = x
        self.y = y
        self.draw()

    def draw(self):

        t = turtle.Turtle()
        if self.player == 1:
            t.pencolor("green")
        if self.player == 2:
            t.pencolor("purple")
        t.penup()
            
        for verticalpos in range(self.y,self.y+25):
            t.setpos(self.x, verticalpos)
            t.pendown()
            t.setpos(self.x+25, verticalpos)
            t.penup()

    def __str__(self):
        return self.player

    def __repr__(self):
        return self.__str__()



class EmptySpace:

    def __init__(self):
        self.empty = True
        self.player = None

    def __str__(self):
        return "Empty"

    def __repr__(self):
        return self.__str__()



class ConnectFour:

    def __init__(self):
        self.player = 1
        # changes player every time a successful move has been made
        self.gridSetup()
        self.screenSetup()

    def gridSetup(self):
        self.grid = []
        for x in range(10):
            ylist = []
            for y in range(10):
                ylist.append(EmptySpace())
            self.grid.append(ylist)

    def screenSetup(self):

        self.drawer = turtle.Turtle()
        self.screen = turtle.getscreen()
        self.screen.reset()
        self.screen.setworldcoordinates(0,0,250,250)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.startX = self.drawer.setx(0)
        self.startY = self.drawer.sety(0)

        self.drawer.penup()
        self.drawer.pencolor("blue")

        i = 0
        while i <= 250:
            self.drawer.setpos(i,0)
            self.drawer.pendown()
            self.drawer.setpos(i, 250)
            self.drawer.penup()
            i += 25

        j = 0
        while j <= 250:
            self.drawer.setpos(0,j)
            self.drawer.pendown()
            self.drawer.setpos(250, j)
            self.drawer.penup()
            j += 25


        self.screen.onclick(self.clicked)
        self.screen.listen()


    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1


    def checkForWinner(self):
    
        for i in range(10):
            for j in range(10):

                #to check each tile vertically upwards
                try:
                    player1 = 0
                    player2 = 0
                    for k in range(4):
                        space = self.grid[i][j+k]
                        if space.__repr__() == 1:
                            player1 += 1
                        if space.__repr__() == 2:
                            player2 += 1
                    if player1 == 4:
                        print("Congrats! Player 1 -green- won in column {} :)".format(i+1))
                        turtle.exitonclick()
                    elif player2 == 4:
                        print("Congrats! Player 2 -purple- won in column {}! :)".format(i+1))
                        turtle.exitonclick()
                except:
                    pass

                #to check each tile horizontally to the right
                try:
                    player1 = 0
                    player2 = 0
                    for k in range(4):
                        space = self.grid[i+k][j]
                        if space.__repr__() == 1:
                            player1 += 1
                        if space.__repr__() == 2:
                            player2 += 1
                    if player1 == 4:
                        print("Congrats! Player 1 -green- won in row {}! :)".format(j+1))
                        turtle.exitonclick()
                    elif player2 == 4:
                        print("Congrats! Player 2 -purple- won in row {}! :)".format(j+1))
                        turtle.exitonclick()
                except:
                    pass

                #to check each tile diagonally up to the right
                try:
                    player1 = 0
                    player2 = 0
                    for k in range(4):
                        space = self.grid[i+k][j+k]
                        if space.__repr__() == 1:
                            player1 += 1
                        if space.__repr__() == 2:
                            player2 += 1
                    if player1 == 4:
                        print("Congrats! Player 1 -green- won with a diagonal! :)")
                        turtle.exitonclick()
                    elif player2 == 4:
                        print("Congrats! Player 2 -purple- won with a diagonal! :)")
                        turtle.exitonclick()
                except:
                    pass

                #to check each tile diagonally up to the left
                try:
                    player1 = 0
                    player2 = 0
                    for k in range(4):
                        space = self.grid[i-k][j+k]
                        if space.__repr__() == 1:
                            player1 += 1
                        if space.__repr__() == 2:
                            player2 += 1
                    if player1 == 4:
                        print("Congrats! Player 1 -green- won with a diagonal! :)")
                        turtle.exitonclick()
                    if player2 == 4:
                        print("Congrats! Player 2 -purple- won with a diagonal! :)")
                        turtle.exitonclick()
                except:
                    pass


    def checkIfFull(self):
        full = True
        for colnum in range(10):
            for rownum in range(10):
                if isinstance(self.grid[colnum][rownum], EmptySpace):
                    full = False
        if full == True:
            print("Board is full - no winner! You should play again :)")
                

    def clicked(self, x, y):
        self.x = x
        self.y = y

        if int(self.y) in range(0,250):
            if int(self.x) in range(0,25):
                self.column = 1
                self.spacex = 0
            elif int(self.x) in range(25, 50):
                self.column = 2
                self.spacex = 25
            elif int(self.x) in range(50, 75):
                self.column = 3
                self.spacex = 50
            elif int(self.x) in range(75,100):
                self.column = 4
                self.spacex = 75
            elif int(self.x) in range(100,125):
                self.column = 5
                self.spacex = 100
            elif int(self.x) in range(125,150):
                self.column = 6
                self.spacex = 125
            elif int(self.x) in range(150, 175):
                self.column = 7
                self.spacex = 150
            elif int(self.x) in range(175, 200):
                self.column = 8
                self.spacex = 175
            elif int(self.x) in range(200, 225):
                self.column = 9
                self.spacex = 200
            else:
                self.column = 10
                self.spacex = 225

        columnlist = self.grid[self.column-1]
        spaceylist = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225]
        notplaced = True
        full = False
        i = 0
    
        while not full and notplaced and i<10:
            if isinstance(columnlist[i], EmptySpace):
                self.spacey = spaceylist[i]
                columnlist[i] = FullSpace(self.spacex, self.spacey, self.player)
                notplaced = False
            else:
                i += 1
        if notplaced == False:
            self.switchPlayer()
        if notplaced == True:
            print("Column full - try another column.")

        self.checkForWinner()
        self.checkIfFull()

                
play = ConnectFour()
            
        
                
