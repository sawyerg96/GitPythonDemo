import turtle
import head_drawer
import torso_drawer
import arms_drawer
import legs_drawer

window = turtle.Screen() # Creates canvas to draw on

pen = turtle.Turtle() # Creates 'turtle' which will be the pen we draw with
pen.hideturtle() # Makes the pen cursor invisible

# Move pen to where head will be drawn
pen.penup()
pen.setposition(0,350)
pen.pendown()

head_drawer.draw_head(pen) # Call function to draw head

# Move pen to where torso will be drawn
pen.penup()
pen.setposition(0,150)
pen.pendown()

torso_drawer.draw_torso(pen) # Call function to draw torso

# Move pen to where arms will be drawn
pen.penup()
pen.setposition(-100,150)
pen.pendown()

arms_drawer.draw_arms(pen) # Call function to draw arms

# Move pen to where legs will be drawn
pen.penup()
pen.setposition(0,-50)
pen.pendown()

legs_drawer.draw_legs(pen) # Call function to draw legs

window.mainloop() # Allows the window to be closed properly
