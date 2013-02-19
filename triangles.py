import canvas
import random
import math

from urbanape import common_devices
from kuler import *

random.seed()

width, height = common_devices['ipad_r']
triangle_side = 1024.0
palette = robots_are_cool

canvas.begin_updates()

canvas.set_size(width, height)
#canvas.set_fill_color(*random.choice(palette))
canvas.set_fill_color(.25, .25, .25)
canvas.fill_rect(0, 0, width, height)

def draw_triangle(x, y, size, num_remaining):
	r, g, b = random.choice(palette)
	canvas.set_fill_color(r, g, b, random.random() * 0.75 + 0.25)
	r, g, b = random.choice(palette)
	canvas.set_stroke_color(r, g, b, random.random() * 0.5 + 0.5)
	canvas.set_line_width(random.random() * 2.5 + 0.5)
	step = math.sqrt(size**2 - (size / 2.0)**2)
	canvas.move_to(x - step, y - (size / 2.0))
	canvas.add_line(x, y + size)
	canvas.add_line(x + step, y - (size / 2.0))
	canvas.add_line(x - step, y - (size / 2.0))
	canvas.fill_path()
	canvas.draw_line(x - step, y - (size / 2.0), x, y + size)
	canvas.draw_line(x, y + size, x + step, y - (size / 2.0))
	canvas.draw_line(x + step, y - (size / 2.0), x - step, y - (size / 2.0))
	canvas.draw_line(x, y, x - (step / 2.0), y + (size / 4.0))
	canvas.draw_line(x, y, x + (step / 2.0), y + (size / 4.0))
	canvas.draw_line(x, y, x, y - (size / 2.0))
	canvas.draw_line(x - (step / 2.0), y + (size / 4.0), x + (step / 2.0), y + (size / 4.0))
	canvas.draw_line(x + (step / 2.0), y + (size / 4.0), x, y - (size / 2.0))
	canvas.draw_line(x, y - (size / 2.0), x - (step / 2.0), y + (size / 4.0))

x = width / 2.0
y = height / 3.0 # figger
draw_triangle(x, y, triangle_side, 100)

canvas.end_updates()