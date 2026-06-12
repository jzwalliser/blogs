from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Maze(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("迷宫")
        color = [BLACK,WHITE]
        group = VGroup()
        maze = "11111111111110000110001111101101111101011011110010110110000000001111111111111"
        for i in range(7):
            for j in range(11):
                rect = Rectangle(width=0.7,height=0.7,stroke_width=2,color=color[int(maze[i * 11 + j])]).set_fill(color=color[int(maze[i * 11 + j])],opacity=1).move_to((j*0.7,-i*0.7,0))
                
                group += rect
        group.next_to(title,DOWN).shift(DOWN * 0.5)
        
        inarrow = Arrow(group[55].get_center() - [1.5,0,0],group[55].get_center())
        outarrow = Arrow(group[21].get_center(),group[21].get_center() + [1.5,0,0])
        self.add(title,group,inarrow,outarrow,icon)
        
        line1 = Line(group[55].get_center(),group[57].get_center(),color=YELLOW,stroke_width=5)
        line2 = Line(group[57].get_center(),group[46].get_center(),color=YELLOW,stroke_width=5)
        line3 = Line(group[46].get_center(),group[47].get_center(),color=YELLOW,stroke_width=5)
        line4 = Line(group[47].get_center(),group[36].get_center(),color=YELLOW,stroke_width=5)
        line5 = Line(group[57].get_center(),group[60].get_center(),color=YELLOW,stroke_width=5)
        line6 = Line(group[60].get_center(),group[16].get_center(),color=YELLOW,stroke_width=5)
        line7 = Line(group[16].get_center(),group[13].get_center(),color=YELLOW,stroke_width=5)
        line8 = Line(group[60].get_center(),group[63].get_center(),color=YELLOW,stroke_width=5)
        line9 = Line(group[63].get_center(),group[19].get_center(),color=YELLOW,stroke_width=5)
        line10 = Line(group[19].get_center(),group[21].get_center(),color=YELLOW,stroke_width=5)

        cross1 = Cross().scale(0.2).move_to(group[46].get_center())
        cross2 = Cross().scale(0.2).move_to(group[47].get_center())
        cross3 = Cross().scale(0.2).move_to(group[36].get_center())
        cross4 = Cross().scale(0.2).move_to(group[49].get_center())
        cross5 = Cross().scale(0.2).move_to(group[38].get_center())
        cross6 = Cross().scale(0.2).move_to(group[27].get_center())
        cross7 = Cross().scale(0.2).move_to(group[16].get_center())
        cross8 = Cross().scale(0.2).move_to(group[15].get_center())
        cross9 = Cross().scale(0.2).move_to(group[14].get_center())
        cross10 = Cross().scale(0.2).move_to(group[13].get_center())
        self.play(Create(line1),run_time=0.3)
        self.play(Create(line2),run_time=0.3)
        self.play(Create(line3),run_time=0.3)
        self.play(Create(line4),run_time=0.3)
        self.play(FadeToColor(line2,RED),FadeToColor(line3,RED),FadeToColor(line4,RED),run_time=0.3)
        self.play(FadeOut(line2),FadeOut(line3),FadeOut(line4),run_time=0.3)
        self.play(LaggedStart(Write(cross3),Write(cross2),Write(cross1),lag_ratio=0.5),run_time=0.3)
        self.play(Create(line5),run_time=0.3)
        self.play(Create(line6),run_time=0.3)
        self.play(Create(line7),run_time=0.3)
        self.play(FadeToColor(line6,RED),FadeToColor(line7,RED),run_time=0.3)
        self.play(FadeOut(line6),FadeOut(line7),run_time=0.3)
        self.play(LaggedStart(Write(cross10),Write(cross9),Write(cross8),Write(cross7),Write(cross6),Write(cross5),Write(cross4),lag_ratio=0.5),run_time=0.7)
        self.play(Create(line8),run_time=0.3)
        self.play(Create(line9),run_time=0.3)
        self.play(Create(line10),run_time=0.3)
        self.play(FadeToColor(line1,"#00ff00"),FadeToColor(line5,"#00ff00"),FadeToColor(line8,"#00ff00"),FadeToColor(line9,"#00ff00"),FadeToColor(line10,"#00ff00"),run_time=0.3)
        self.wait(1)
        self.play(FadeOut(line1),FadeOut(line5),FadeOut(line8),FadeOut(line9),FadeOut(line10),Unwrite(cross1),Unwrite(cross2),Unwrite(cross3),Unwrite(cross4),Unwrite(cross5),Unwrite(cross6),Unwrite(cross7),Unwrite(cross8),Unwrite(cross9),Unwrite(cross10),run_time=0.5)
        

