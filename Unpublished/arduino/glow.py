from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

def radial_glow(color=YELLOW):
    glow = VGroup()
    base_radius = 0.6
    for i in range(10):
        layer = Circle(radius=base_radius + i * 0.25,stroke_width=0,fill_color=color,fill_opacity=0.08)
        glow += layer
    return glow

class NewScene(Scene):
    def construct(self):
        self.add(radial_glow("#aaff00").scale(0.5))
        #self.play(glow.animate.scale(1.5), run_time=2)
