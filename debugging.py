##In order complete this challenge you need to debug the following code.
##It may be easier to do so if you improve the code quality. 
##copy and paste this code into a new file named “debugging.py”

import turtle # imports the turtle library

t1 = turtle.clone() #this creates a new turtle and stores it in a variable
t = 200
b = -200

#draw the letter ‘A’

turtle.hideturtle() # this hides the arrow of the turtle called turtle


t1.penup()


t1.goto(0,300)


t1.pendown()
t1.right(70)
t1.fd(500)
t1.back(500)
t1.right(50)
t1.fd(500)
t1.back(250)
t1.left(120)
t1.fd(210)

a,c = t1.pos()




t1.pendown()





turtle.manloop() # all turtle commands must go before this line!!!
