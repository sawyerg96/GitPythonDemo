def draw_head(pen):
    pen.up()
    pen.forward(45)
    pen.right(90)
    pen.forward(90)
    pen.down()
    for i in range(4):
        pen.forward(50)
        pen.right(90)
    return
