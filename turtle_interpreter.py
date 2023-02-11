import turtle
import lsystem


class TurtleInterpreter:
    def __init__(self, width=800, height=800, bgColor='white'):
        self.turt = turtle.Turtle()
        '''screen'''
        self.screen = turtle.Screen()
        self.screen.setup(width = 800, height = 1000)
        self.screen.bgcolor(bgColor)

    def setColor(self, c):
        self.turt.color(c)
        
    def setWidth(self, w):
        self.turt.width(w)

    def goto(self, x, y, heading = None):
        self.turt.penup()
        self.turt.goto(x,y)
        self.turt.pendown()
        if heading != None:
            self.turt.setheading(heading)

    def getScreenWidth(self):
        return self.screen.window_width()

    def getScreenHeight(self):
        return self.screen.window_height()

    turtle.tracer(0)
    '''TurtleInterpreter constructor.
    Creates instance variables for a Turtle object and a Screen object with a particular window
    `width`, `height`, and background color `bgColor`.
    '''
    # Create a Turtle object, set it as an instance variable

    # Create a Screen object, set it as an instance variable.
    # Set the screen's height, width, and color based on the parameters

    # Turn the screen's tracer off.


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        self.turt.hideturtle()
        self.screen.update()

        # Close the window when users presses the 'q' key
        self.screen.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        self.screen.listen()

        # Have the turtle listen for a click
        self.screen.exitonclick()



    def drawString(self, lsysString, distance, angle):
        posList = []
        headList = []
        saveList = []
        for char in lsysString:
            if char == "F":
                self.turt.forward(distance)
            if char == "+":
                self.turt.left(angle)
            if char == "-":
                self.turt.right(angle)
            if char == "[":
                posList.insert(0,self.turt.position())
                headList.insert(0, self.turt.heading())
            if char == "]":
                position = posList.pop(0)
                self.goto(position[0], position[1], headList.pop(0))
            if char == "<":
                saveList.append(self.turt.color()[0])
            if char == ">":
                c = saveList.pop(-1)
                self.turt.pencolor(c)
            if char == "g":
                self.turt.pencolor(0.15, 0.5, 0.2)
            if char == "y":
                self.turt.pencolor(0.8, 0.8, 0.3)
            if char == "r":
                self.turt.pencolor(0.7, 0.2, 0.3)
            if char == "L":
                self.turt.circle(distance/2, 180)
                self.turt.left(90)
                self.turt.forward(distance/1)
            if char == "B":
                self.turt.circle(distance/4)



                '''Interpret each character in an L-system string as a turtle command.

    Here is the starting L-system alphabet:
        F is forward by a certain distance
        + is left by an angle
        - is right by an angleh

    Parameters:
    -----------
    lsysString: str. The L-system string with characters that will be interpreted as drawing
        commands.
    distance: distance to travel with F command.
    angle: turning angle (in deg) for each right/left command.
    '''

    # Walk through the lsysString character-by-character and
    # have the turtle object (instance variable) carry out the
    # appropriate commands

    # Call the update method on the screen object to make sure
    # everything drawn shows up at the very end of the method
    # (remember: you turned off animations in the constructor)