import turtle
import lsystem
import turtle_interpreter as ti

def ground(terp):
    '''This function draw the ground in the scene.'''
    terp.goto(-500, -250, 0)
    terp.setColor('DarkOliveGreen4')
    terp.setWidth(300)
    terp.drawString('F', 1000, 0 )

def peacockTail(terp):
    '''This function draw a peacock tail using a string I made and iterating it four times.'''
    lsys = lsystem.Lsystem('lDesign.txt')
    terp.goto(0, -200, 100)
    lsysString = lsys.buildString(4)
    terp.setColor('blue')
    terp.setWidth(3)
    terp.drawString(lsysString, 10, 10)

def peacockBody1(terp):
    '''This function draws the peacock's body.'''
    terp.goto(-20, -220, 90)
    terp.setColor('blue')
    terp.setWidth(50)
    terp.drawString('F+F+F+F+F+F', 10, 60)

def peacockNeck1(terp):
    "This function draws the peacock's neck."
    terp.goto(-45, -190, 90)
    terp.setColor('blue')
    terp.setWidth(10)
    terp.drawString('FFF+F+FFF+F', 5, 90)

def peacockHead1(terp):
    '''This function draws the peacock's head.'''
    terp.goto(-50, -170, 90)
    terp.setColor('blue')
    terp.setWidth(18)
    terp.drawString('F+F+F+F', 5, 90)

def peacockTail2(terp):
    '''This function draws the peacock's tail using the text file I wrote iterating 3 times.'''
    lsys = lsystem.Lsystem('lDesign.txt')
    terp.goto(-300, -200, 90)
    lsysString = lsys.buildString(3)
    terp.setColor('blue')
    terp.setWidth(3)
    terp.drawString(lsysString, 10, 10)

def peacockBody2(terp):
    '''This function draws the peacock's body.'''
    terp.goto(-320, -220, 90)
    terp.setColor('blue')
    terp.setWidth(50)
    terp.drawString('F+F+F+F+F+F', 10, 60)

def peacockNeck2(terp):
    '''This function draws the peacock's neck.'''
    terp.goto(-345, -190, 90)
    terp.setColor('blue')
    terp.setWidth(10)
    terp.drawString('FFF+F+FFF+F', 5, 90)

def peacockHead2(terp):
    '''This function draws the peacock's head.'''
    terp.goto(-350, -170, 90)
    terp.setColor('blue')
    terp.setWidth(18)
    terp.drawString('F+F+F+F', 5, 90)

def peacockTail3(terp):
    '''This function draws the peacocks tail using the text file I wrote and iterating 3 times.'''
    lsys = lsystem.Lsystem('lDesign.txt')
    terp.goto(200, -200, 90)
    lsysString = lsys.buildString(3)
    terp.setColor('blue')
    terp.setWidth(3)
    terp.drawString(lsysString, 10, 10)

def peacockBody3(terp):
    '''This function draws the peacocks body.'''
    terp.goto(180, -220, 90)
    terp.setColor('blue')
    terp.setWidth(50)
    terp.drawString('F+F+F+F+F+F', 10, 60)

def peacockNeck3(terp):
    '''This function draws the peacocks neck.'''
    terp.goto(155, -190, 90)
    terp.setColor('blue')
    terp.setWidth(10)
    terp.drawString('FFF+F+FFF+F', 5, 90)

def peacockHead3(terp):
    '''This function draws the peacocks head.'''
    terp.goto(150, -170, 90)
    terp.setColor('blue')
    terp.setWidth(18)
    terp.drawString('F+F+F+F', 5, 90)

def tree1(terp):
    '''This function draws a tree using a text file I wrote that iterates one time.'''
    lsys = lsystem.Lsystem('lDesign2.txt')
    terp.goto(100, -100, 90)
    lsysString = lsys.buildString(1)
    terp.setColor('brown')
    terp.setWidth(3)
    terp.drawString(lsysString, 30, 15)

def tree2(terp):
    '''This funcion draws a tree using a text file I wrote that iterates two times.'''
    lsys = lsystem.Lsystem('lDesign2.txt')
    terp.goto(0, -100, 90)
    lsysString = lsys.buildString(2)
    terp.setColor('khaki4')
    terp.setWidth(3)
    terp.drawString(lsysString, 7, 33)

def tree3(terp):
    '''This funcion draws a tree using a text file I wrote that iterates three times.'''
    lsys = lsystem.Lsystem('lDesign2.txt')
    terp.goto(-200, -100, 90)
    lsysString = lsys.buildString(3)
    terp.setColor('lightsalmon4')
    terp.setWidth(3)
    terp.drawString(lsysString, 10, 10)

def tree4(terp):
    '''This funcion draws a tree using a text file I wrote that iterates two times.'''
    lsys = lsystem.Lsystem('lDesign3.txt')
    terp.goto(-100, -100, 90)
    lsysString = lsys.buildString(2)
    terp.setColor('lightgoldenrod2')
    terp.setWidth(3)
    terp.drawString(lsysString, 7, 20)

def tree5(terp):
    '''This function draws a tree using a text file I wrote that iterates one time.'''
    lsys = lsystem.Lsystem('lDesign3.txt')
    terp.goto(-300, -100, 90)
    lsysString = lsys.buildString(1)
    terp.setColor('lightgoldenrod2')
    terp.setWidth(10)
    terp.drawString(lsysString, 30, 13)

def tree6(terp):
    '''This funcion draws a tree using a text file I wrote that iterates three times.'''
    lsys = lsystem.Lsystem('lDesign3.txt')
    terp.goto(200, -100, 90)
    lsysString = lsys.buildString(3)
    terp.setColor('lightgoldenrod2')
    terp.setWidth(2)
    terp.drawString(lsysString, 8, 30)

def main():
    '''This function calls all other functions into a scene and draws them creating a coherent scene of trees and peacocks.'''
    terp = ti.TurtleInterpreter(800, 800, bgColor='CadetBlue3')
    ground(terp)
    peacockTail(terp)
    peacockBody1(terp)
    peacockNeck1(terp)
    peacockHead1(terp)
    peacockTail2(terp)
    peacockBody2(terp)
    peacockNeck2(terp)
    peacockHead2(terp)
    peacockTail3(terp)
    peacockBody3(terp)
    peacockNeck3(terp)
    peacockHead3(terp)
    tree1(terp)
    tree2(terp)
    tree3(terp)
    tree4(terp)
    tree5(terp)
    tree6(terp)
    terp.hold()


if __name__ == '__main__':
    main()