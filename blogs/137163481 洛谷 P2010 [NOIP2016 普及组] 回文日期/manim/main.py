from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class FindingSolutions(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("寻找解") #寻找解
        eclipse = Ellipse(width=7,height=5,color=WHITE).next_to(title,DOWN).set_sheen_direction(RIGHT).set_fill(color=[GREEN,BLUE],opacity=1).shift(DOWN * 0.5)
        circ1 = Circle(radius=1.4,color=WHITE).shift(DL * 1).set_sheen_direction(RIGHT).set_fill(color=[GREEN,ORANGE],opacity=1)
        circ2 = Circle(radius=1.4,color=WHITE).shift(DR * 1).set_sheen_direction(RIGHT).set_fill(color=[ORANGE,BLUE],opacity=1)
        all = Text("所有八位数").move_to(eclipse.get_center()).shift(UP * 1.5).scale(0.8)
        legal = Text("合法\n日期").move_to(circ1.get_center()).shift(LEFT * 0.3).scale(0.8)
        palin = Text("回文\n八位数").move_to(circ2.get_center()).shift(RIGHT * 0.3).scale(0.8)
        inter = Intersection(circ1,circ2,color=RED,fill_opacity=1)
        solution = Text("本题的解").to_edge(DOWN,buff=0.2)
        arrow = Arrow(inter.get_center(),solution.get_top())
        self.add(title,eclipse,circ1,circ2,all,legal,palin,inter,solution,arrow,icon)
