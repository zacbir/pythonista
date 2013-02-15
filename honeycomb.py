size(2048, 2048)

fill(0,0,0,1)
rect(0,0,2048,2048)

# palettes via Kuler: http://kuler.adobe.com/
    
def gen_color(r, g, b):
    return (r/255.0, g/255.0, b/255.0)

mucha_winter = (
    gen_color(242.0, 212.0, 155.0),
    gen_color(242.0, 178.0, 102.0),
    gen_color(191.0, 111.0, 65.0),
    gen_color(89.0, 18.0, 2.0),
    gen_color(55.0, 69.0, 65.0),    
)

mabelis = (
    gen_color(88.0, 0.0, 34.0),
    gen_color(170.0, 44.0, 48.0),
    gen_color(255.0, 190.0, 141.0),
    gen_color(72.0, 123.0, 127.0),
    gen_color(1.0, 29.0, 36.0),
)

full_of_life = (
    gen_color(2.0, 115.0, 115.0),
    gen_color(3.0, 140.0, 127.0),
    gen_color(217.0, 179.0, 67.0),
    gen_color(242.0, 140.0, 58.0),
    gen_color(191.0, 63.0, 52.0),
)

let_the_rays_fall_on_the_earth = (
    gen_color(64.0, 39.0, 104.0),
    gen_color(127.0, 83.0, 112.0),
    gen_color(191.0, 117.0, 96.0),
    gen_color(229.0, 141.0, 0.0),
    gen_color(255.0, 183.0, 0.0),
)

robots_are_cool = (
    gen_color(30.0, 58.0, 64.0),
    gen_color(104.0, 140.0, 140.0),
    gen_color(217.0, 209.0, 186.0),
    gen_color(242.0, 209.0, 148.0),
    gen_color(242.0, 160.0, 87.0),
)

palette = mucha_winter

for x in range(100):
    r, g, b = choice(palette)
    fill(r, g, b, random() * 0.5 + 0.25)
    csize = random() * 256 + 128
    oval(random() * 2048, random() * 2048, csize, csize)

def rstrokedline(start_x, start_y, end_x, end_y):
    stroke(1, 1, 1, random() * 0.25 + 0.05)
    line(start_x, start_y, end_x, end_y)

def hexacircle(start_x, start_y):
    r, g, b = choice(palette)

    nofill()
    stroke(1,1,1, random() * 0.15)
    star(start_x, start_y, 6, 32, 32 * 1.155)
    fill(r, g, b, random() * 0.75 + 0.25)
    stroke(1,1,1, random() * 0.50 + 0.50)
    oval(start_x - 32, start_y - 32, 64, 64)

    # draw lines
    rstrokedline(start_x, start_y - 64, start_x, start_y + 64)
    rstrokedline(start_x - 64, start_y - 36, start_x + 64, start_y + 36)
    rstrokedline(start_x - 64, start_y + 36, start_x + 64, start_y - 36)

    rstrokedline(start_x - 114, start_y + 197, start_x + 114, start_y - 195)
    rstrokedline(start_x - 114, start_y - 195, start_x + 114, start_y + 197)
    rstrokedline(start_x - 64, start_y, start_x + 64, start_y)

for x in range(19): # 19 for full-width
    for y in range(32): # 32 for full-height
        center_x = x * 112
        center_y = y * 64
        hexacircle(center_x, center_y)
        hexacircle(center_x + 56, center_y + 32)

# Mute with a 15% black overlay
fill(0,0,0,0.15)
rect(0,0,2048,2048)
