
import turtle
import random


def ask_string():
	string = input('Inserte la cadena de texto: ')
	return string


def get_random_position():
	x = random.choice(range(-250, 250))
	y = random.choice(range(-250, 250))
	return (x, y)


def get_random_font_size():
	font_sizes = range(10, 30)
	return random.choice(font_sizes)


def get_random_color():
	colors = ['red', 'blue', 'green', 'orange', 'yellow']
	return random.choice(colors)


def draw_character(character, font_size, position, color):
	style = ('Arial', font_size, 'italic')

	turtle.color(color)
	turtle.penup()
	turtle.hideturtle() 

	turtle.goto(position[0], position[1])
	
	turtle.pendown()
	turtle.showturtle()
	turtle.write(character, font=style, align='left')
