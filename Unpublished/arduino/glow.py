from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)


def radial_glow(mobject,color=YELLOW):
    glow = VGroup()
    base_radius = 0.6
    for i in range(10):
        layer = Circle(radius=base_radius + i * 0.25,stroke_width=0,fill_color=color,fill_opacity=0.08)
        glow += layer
    glow.move_to(mobject).scale(0.15)
    return glow

class Glow(VGroup):
    def __init__(self,mobject,outer_radius=1,inner_radius=0.1,rings=10,color=YELLOW,*args,**kwargs):
        super().__init__(*args,**kwargs)
        d = (outer_radius - inner_radius) / rings
        if d < 0:
            raise ValueError("Outer radius greater than inner radius. Consider swapping the values.")
        for i in range(rings):
            layer = Circle(radius=outer_radius - i * d,stroke_width=0,fill_color=color,fill_opacity=0.08)
            layer.set_stroke(0,background=True)
            self += layer
        self.move_to(mobject)
            
class NewScene(Scene):
    def construct(self):
        m = Circle(radius=1).shift(LEFT)
        g = Glow(m,inner_radius=5)
        self.add(g)
