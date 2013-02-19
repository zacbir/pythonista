import canvas

def gen_color(r, g, b):
    return (r/255.0, g/255.0, b/255.0)

def avg(color):
	return float(sum(color) / len(color))

class Theme(obj):
	
	def __init__(self, name, colors):
		self.name = name
		self.colors = [gen_color(*color) for color in colors]
		self.lightest = self.determine_lightest()
		self.darkest = self.detemine_darkest()
		
	def determine_lightest(self):
		avgs = [avg(color) for color in self.colors]
		return max(avgs)
		
	def determine_darkest(self):
		avgs = [avg(color) for color in self.colors]
		return min(avgs)

mucha_winter = Theme('Mucha Winter', )
    'name': 'mucha winter',
    'palette': (
        gen_color(242.0, 212.0, 155.0),
        gen_color(242.0, 178.0, 102.0),
        gen_color(191.0, 111.0, 65.0),
        gen_color(89.0, 18.0, 2.0),
        gen_color(55.0, 69.0, 65.0),
    ),
    'darkest': None,
    'lightest': None,
}

mabelis = {
    'name': 'mabelis',
    'palette': (
        gen_color(88.0, 0.0, 34.0),
        gen_color(170.0, 44.0, 48.0),
        gen_color(255.0, 190.0, 141.0),
        gen_color(72.0, 123.0, 127.0),
        gen_color(1.0, 29.0, 36.0),
    ),
    'darkest': None,
    'lightest': None,
}

full_of_life = {
    'name': 'full of life',
    'palette': (
        gen_color(2.0, 115.0, 115.0),
        gen_color(3.0, 140.0, 127.0),
        gen_color(217.0, 179.0, 67.0),
        gen_color(242.0, 140.0, 58.0),
        gen_color(191.0, 63.0, 52.0),
    ),
    'darkest': None,
    'lightest': None,
}

let_the_rays_fall_on_the_earth = {
    'name': 'let the rays fall on the earth',
    'palette': (
        gen_color(64.0, 39.0, 104.0),
        gen_color(127.0, 83.0, 112.0),
        gen_color(191.0, 117.0, 96.0),
        gen_color(229.0, 141.0, 0.0),
        gen_color(255.0, 183.0, 0.0),
    ),
    'darkest': None,
    'lightest': None,
}

robots_are_cool = {
    'name': 'robots are cool',
    'palette': (
        gen_color(30.0, 58.0, 64.0),
        gen_color(104.0, 140.0, 140.0),
        gen_color(217.0, 209.0, 186.0),
        gen_color(242.0, 209.0, 148.0),
        gen_color(242.0, 160.0, 87.0),
    ),
    'darkest': None,
    'lightest': None,
}

def draw_block(x, y, theme):
    start_x, start_y = x, y
    darkest_avg = 1.0
    lightest_avg = 0.0
    darkest = (1.0, 1.0, 1.0)
    lightest = (0.0, 0.0, 0.0)
    for palette_color in theme['palette']:
        canvas.set_fill_color(*palette_color)
        palette_avg = ((palette_color[0] + palette_color[1] + palette_color[2]) / 3.0)
        if palette_avg < darkest_avg:
            darkest_avg = palette_avg
            darkest = palette_color
        if palette_avg > lightest_avg:
            lightest_avg = palette_avg
            lightest = palette_color
        canvas.fill_rect(start_x, start_y, 25.0, 50.0)
        start_x += 25.0
    
    start_x += 10.0
    canvas.set_fill_color(*darkest)
    canvas.fill_rect(start_x, start_y, 25.0, 50.0)
    theme['darkest'] = darkest

    start_x += 35.0
    canvas.set_fill_color(*lightest)
    canvas.fill_rect(start_x, start_y, 25.0, 50.0)
    theme['lightest'] = lightest

themes = (mucha_winter, mabelis, full_of_life, let_the_rays_fall_on_the_earth, robots_are_cool)

if __name__ == '__main__':
	canvas.set_size(1024.0, 1024.0)

	start_x = 10.0
	start_y = 10.0

	for theme in themes:
		draw_block(start_x, start_y, theme)
		start_y += 60.0
