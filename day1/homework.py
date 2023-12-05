from turtle import*
#walls
width(5)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
end_fill()
#door
color("Black")
begin_fill()
forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()
 #roof
penup()
goto(200, 200)
pendown()
color("green")
begin_fill()
right(140)
forward(150)
left(97)
forward(155)
end_fill()
 #window 1
color("cyan")
begin_fill()
penup()
goto(13, 60)
pendown()
right(227)
forward(40)
left(90)
forward(40)
left(90) 
forward(40)
left(90)
forward(40)
end_fill()
 # window 2
 
color("cyan")
begin_fill()
penup()
goto(187, 60)
pendown()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()





exitonclick()   


