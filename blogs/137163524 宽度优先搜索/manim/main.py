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
        
        line1 = Line(group[55].get_center(),group[56].get_center(),color=YELLOW,stroke_width=5)
        line2 = Line(group[56].get_center(),group[57].get_center(),color=YELLOW,stroke_width=5)
        line3 = Line(group[57].get_center(),group[46].get_center(),color=YELLOW,stroke_width=5)
        line4 = Line(group[57].get_center(),group[58].get_center(),color=YELLOW,stroke_width=5)
        line5 = Line(group[46].get_center(),group[47].get_center(),color=YELLOW,stroke_width=5)
        line6 = Line(group[58].get_center(),group[59].get_center(),color=YELLOW,stroke_width=5)
        line7 = Line(group[47].get_center(),group[36].get_center(),color=YELLOW,stroke_width=5)
        line8 = Line(group[59].get_center(),group[60].get_center(),color=YELLOW,stroke_width=5)
        line9 = Line(group[60].get_center(),group[49].get_center(),color=YELLOW,stroke_width=5)
        line10 = Line(group[60].get_center(),group[61].get_center(),color=YELLOW,stroke_width=5)
        line11 = Line(group[49].get_center(),group[38].get_center(),color=YELLOW,stroke_width=5)
        line12 = Line(group[61].get_center(),group[62].get_center(),color=YELLOW,stroke_width=5)
        line13 = Line(group[38].get_center(),group[27].get_center(),color=YELLOW,stroke_width=5)
        line14 = Line(group[62].get_center(),group[63].get_center(),color=YELLOW,stroke_width=5)
        line15 = Line(group[27].get_center(),group[16].get_center(),color=YELLOW,stroke_width=5)
        line16 = Line(group[63].get_center(),group[52].get_center(),color=YELLOW,stroke_width=5)
        line17 = Line(group[16].get_center(),group[15].get_center(),color=YELLOW,stroke_width=5)
        line18 = Line(group[52].get_center(),group[41].get_center(),color=YELLOW,stroke_width=5)
        line19 = Line(group[15].get_center(),group[14].get_center(),color=YELLOW,stroke_width=5)
        line20 = Line(group[41].get_center(),group[30].get_center(),color=YELLOW,stroke_width=5)
        line21 = Line(group[14].get_center(),group[13].get_center(),color=YELLOW,stroke_width=5)
        line22 = Line(group[30].get_center(),group[19].get_center(),color=YELLOW,stroke_width=5)
        line23 = Line(group[19].get_center(),group[20].get_center(),color=YELLOW,stroke_width=5)
        line24 = Line(group[20].get_center(),group[21].get_center(),color=YELLOW,stroke_width=5)

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
        self.play(Create(line5),run_time=0.3)
        self.play(Create(line6),run_time=0.3)
        self.play(Create(line7),run_time=0.3)
        self.play(Create(line8),run_time=0.3)
        self.play(FadeToColor(line3,RED),FadeToColor(line5,RED),FadeToColor(line7,RED),run_time=0.3)
        self.play(FadeOut(line3),FadeOut(line5),FadeOut(line7),run_time=0.3)
        self.play(LaggedStart(Write(cross3),Write(cross2),Write(cross1),lag_ratio=0.5),run_time=0.3)
        self.play(Create(line9),run_time=0.3)
        self.play(Create(line10),run_time=0.3)
        self.play(Create(line11),run_time=0.3)
        self.play(Create(line12),run_time=0.3)
        self.play(Create(line13),run_time=0.3)
        self.play(Create(line14),run_time=0.3)
        self.play(Create(line15),run_time=0.3)
        self.play(Create(line16),run_time=0.3)
        self.play(Create(line17),run_time=0.3)
        self.play(Create(line18),run_time=0.3)
        self.play(Create(line19),run_time=0.3)
        self.play(Create(line20),run_time=0.3)
        self.play(Create(line21),run_time=0.3)
        self.play(FadeToColor(line9,RED),FadeToColor(line11,RED),FadeToColor(line13,RED),FadeToColor(line15,RED),FadeToColor(line17,RED),FadeToColor(line19,RED),FadeToColor(line21,RED),run_time=0.3)
        self.play(FadeOut(line9),FadeOut(line11),FadeOut(line13),FadeOut(line15),FadeOut(line17),FadeOut(line19),FadeOut(line21),run_time=0.3)
        self.play(LaggedStart(Write(cross10),Write(cross9),Write(cross8),Write(cross7),Write(cross6),Write(cross5),Write(cross4),lag_ratio=0.5),run_time=0.7)
        self.play(Create(line22),run_time=0.3)
        self.play(Create(line23),run_time=0.3)
        self.play(Create(line24),run_time=0.3)
        self.play(FadeToColor(line1,"#00ff00"),FadeToColor(line2,"#00ff00"),FadeToColor(line4,"#00ff00"),FadeToColor(line6,"#00ff00"),FadeToColor(line8,"#00ff00"),FadeToColor(line10,"#00ff00"),FadeToColor(line12,"#00ff00"),FadeToColor(line14,"#00ff00"),FadeToColor(line16,"#00ff00"),FadeToColor(line18,"#00ff00"),FadeToColor(line20,"#00ff00"),FadeToColor(line22,"#00ff00"),FadeToColor(line23,"#00ff00"),FadeToColor(line24,"#00ff00"),run_time=0.3)
        self.wait(1)
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(line4),FadeOut(line6),FadeOut(line8),FadeOut(line10),FadeOut(line12),FadeOut(line14),FadeOut(line16),FadeOut(line18),FadeOut(line20),FadeOut(line22),FadeOut(line23),FadeOut(line24),Unwrite(cross1),Unwrite(cross2),Unwrite(cross3),Unwrite(cross4),Unwrite(cross5),Unwrite(cross6),Unwrite(cross7),Unwrite(cross8),Unwrite(cross9),Unwrite(cross10),run_time=0.5)
        

class MazePic(Scene):
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
