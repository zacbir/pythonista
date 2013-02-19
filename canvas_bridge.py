try:
    from canvas import *
except ImportError:
    # We're in NodeBox
    def begin_updates():
        pass

    def end_updates():
        pass

    set_fill_color = fill
    fill_rect = rect
    fill_ellipse = oval
    set_stroke_color = stroke
    set_line_width = strokewidth
    
    def draw_rect(x, y, width, height):
        """capture and reset current fill color"""
        clr = fill()
        nofill()
        rect(x, y, width, height)
        fill(clr)

    def draw_ellipse(x, y, size_x, size_y):
        """capture and reset current fill color"""
        clr = fill()
        nofill()
        oval(x, y, size_x, size_y)
        fill(clr)

    set_size = size

set_size(1024.0, 1024.0)
set_fill_color(1.0, 0.0, 0.0, 1.0)
set_stroke_color(1.0, 0.0, 0.0, 1.0)
draw_rect(100.0, 100.0, 100.0, 100.0)
fill_rect(300.0, 100.0, 100.0, 100.0)
draw_ellipse(100.0, 300.0, 100.0, 100.0)
fill_ellipse(300.0, 300.0, 100.0, 100.0)
