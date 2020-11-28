
import turtle

from utilities import ask_string
from utilities import get_random_position
from utilities import get_random_font_size
from utilities import draw_character
from utilities import get_random_color


def main():
	characters = ask_string()

	screen = turtle.Screen()

	for character in characters:
		font_size = get_random_font_size()
		position = get_random_position()
		color = get_random_color()

		draw_character(character, font_size, position, color)

	screen.mainloop()


if __name__ == '__main__':
	main()
