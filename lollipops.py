import canvas
import random
import math

from urbanape import common_devices
from kuler import *

random.seed()

width, height = common_devices['ipad_r']
palette = robots_are_cool

canvas.begin_updates()

canvas.set_size(width, height)
canvas.set_fill_color(*palette['darkest'])
canvas.fill_rect(0, 0, width, height)

canvas.set_fill_color(*random.choice(palette['palette']))
canvas.set_stroke_color(*palette['lightest'])
start_x, start_y = (width / 2.0, height / 2.0)

lollipop_points = []

for x in xrange(64):
	end_x, end_y = (random.random() * (width * 0.8) + (width * 0.1), random.random() * (height * 0.8) + (height * 0.1))
	lollipop_points.append((end_x, end_y))
	canvas.set_line_width(random.random() * 0.75 + 0.25)
	canvas.draw_line(start_x, start_y, end_x, end_y)
	
for x in xrange(64):
	end_x, end_y = lollipop_points[x]
	size = random.random() * 128.0 + 32.0
	canvas.fill_ellipse(end_x - (size / 2.0), end_y - (size / 2.0), size, size)
	canvas.set_line_width(1.25)
	canvas.draw_ellipse(end_x - (size / 2.0), end_y - (size / 2.0), size, size)

size = random.random() * 128.0 + 32.0
canvas.fill_ellipse(start_x - (size / 2.0), start_y - (size / 2.0), size, size)
canvas.set_line_width(1.25)
canvas.draw_ellipse(start_x - (size / 2.0), start_y - (size / 2.0), size, size)

canvas.end_updates()