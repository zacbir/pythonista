import canvas
import random
import math

random.seed()

# common devices
ipad = (1024.0, 1024.0)
ipad_r = (2048.0, 2048.0)
iphone = (320.0, 480.0)
iphone_r = (640.0, 960.0)
iphone_5 = (640.0, 1136.0)
mbp_r = (2880.0, 1800.0) # too big for Pythonista

width, height = ipad_r
circle_size = 192.0
step = math.sqrt(circle_size**2 - (circle_size / 2.0)**2)

def gen_color(r, g, b):
	return (r/255.0, g/255.0, b/255.0)

# palettes via Kuler: http://kuler.adobe.com/
    
mucha_winter = (
    gen_color(242, 212, 155),
    gen_color(242, 178, 102),
    gen_color(191, 111, 65),
    gen_color(89, 18, 2),
    gen_color(55, 69, 65),    
)

mabelis = (
    gen_color(88, 0, 34),
    gen_color(170, 44, 48),
    gen_color(255, 190, 141),
    gen_color(72, 123, 127),
    gen_color(1, 29, 36),
)

full_of_life = (
    gen_color(2, 115, 115),
    gen_color(3, 140, 127),
    gen_color(217, 179, 67),
    gen_color(242, 140, 58),
    gen_color(191, 63, 52),
)

let_the_rays_fall_on_the_earth = (
    gen_color(64, 39, 104),
    gen_color(127, 83, 112),
    gen_color(191, 117, 96),
    gen_color(229, 141, 0),
    gen_color(255, 183, 0),
)

robots_are_cool = (
    gen_color(30, 58, 64),
    gen_color(104, 140, 140),
    gen_color(217, 209, 186),
    gen_color(242, 209, 148),
    gen_color(242, 160, 87),
)

palette = robots_are_cool

canvas.begin_updates()

canvas.set_size(height, width)
canvas.set_fill_color(*random.choice(palette))
canvas.fill_rect(0,0,width, height)

for x in range(100):
	r, g, b = random.choice(palette)
	canvas.set_fill_color(r, g, b, random.random() * 0.5 + 0.25)
	csize = random.random() * (width / 8.0) + (width / 16.0)
	canvas.fill_ellipse(random.random() * width, random.random() * height, csize, csize)

def rstrokedline(start_x, start_y, end_x, end_y):
	canvas.set_line_width(random.random() * 0.75 + 0.25)
	canvas.set_stroke_color(1, 1, 1, random.random() * 0.25 + 0.05)
	canvas.draw_line(start_x, start_y, end_x, end_y)

def hexacircle(start_x, start_y):
	r, g, b = random.choice(palette)

	canvas.set_fill_color(r, g, b, random.random() * 0.75 + 0.25)
	canvas.set_stroke_color(1, 1, 1, random.random() * 0.50 + 0.50)
	canvas.set_line_width(random.random() * 0.75 + 0.25)
	canvas.draw_ellipse(start_x - (0.5 * circle_size), start_y - (0.5 * circle_size), circle_size, circle_size)
	canvas.fill_ellipse(start_x - (0.5 * circle_size), start_y - (0.5 * circle_size), circle_size, circle_size)

	# draw lines
	rstrokedline(start_x, start_y - circle_size, start_x, start_y + circle_size)
	rstrokedline(start_x - step, start_y, start_x + step, start_y)

	rstrokedline(start_x - step, start_y - (0.5 * circle_size), start_x + step, start_y + (0.5 * circle_size))
	rstrokedline(start_x - step, start_y + (0.5 * circle_size), start_x + step, start_y - (0.5 * circle_size))

	rstrokedline(start_x - step, start_y + (1.5 * circle_size), start_x + step, start_y - (1.5 * circle_size))
	rstrokedline(start_x - step, start_y - (1.5 * circle_size), start_x + step, start_y + (1.5 * circle_size))
    
	rstrokedline(start_x - step, start_y + (2.5 * circle_size), start_x + step, start_y - (2.5 * circle_size))
	rstrokedline(start_x - step, start_y - (2.5 * circle_size), start_x + step, start_y + (2.5 * circle_size))
    
	rstrokedline(start_x - (3.0 * step), start_y + (0.5 * circle_size), start_x + (3.0 * step), start_y - (0.5 * circle_size))
	rstrokedline(start_x - (3.0 * step), start_y - (0.5 * circle_size), start_x + (3.0 * step), start_y + (0.5 * circle_size))

for x in xrange(int(math.ceil(width/circle_size))+1):
	for y in xrange(int(math.ceil(height/circle_size))+1):
		center_x = x * (2.0 * step)
		center_y = y * circle_size
		hexacircle(center_x, center_y)
		hexacircle(center_x + step, center_y + (0.5 * circle_size))

# Mute with a 15% black overlay
canvas.set_fill_color(0,0,0,0.15)
canvas.draw_rect(0,0,width,height)

canvas.end_updates()
