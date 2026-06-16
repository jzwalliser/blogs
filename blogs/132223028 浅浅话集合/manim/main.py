from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Intersect(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("交集")
        circ1 = Circle(radius=1.4).shift(DL * 1).set_sheen_direction(RIGHT).set_fill(color=[GREEN_A,RED_A],opacity=1)
        circ2 = Circle(radius=1.4).shift(DR * 1).set_sheen_direction(RIGHT).set_fill(color=[RED_A,BLUE_A],opacity=1)
        a = MathTex("A",color=BLACK).move_to(circ1.get_center()).shift(LEFT * 0.3)
        b = MathTex("B",color=BLACK).move_to(circ2.get_center()).shift(RIGHT * 0.3)
        inter = Intersection(circ1,circ2,color=RED,fill_opacity=1)
        inter_text = MathTex(r"A\cap B").next_to(title,DOWN).shift(DOWN)
        arrow = Arrow(inter.get_center(),inter_text.get_bottom())
        self.add(title,circ1,circ2,a,b,inter,inter_text,arrow,icon)
        
class Union(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("并集")
        circ1 = Circle(radius=1.4).shift(DL * 1).set_sheen_direction(RIGHT).set_fill(color=[GREEN_A,RED_A],opacity=1)
        circ1_n = Circle(radius=1.4).shift(DL * 1)
        circ2 = Circle(radius=1.4).shift(DR * 1).set_sheen_direction(RIGHT).set_fill(color=[RED_A,BLUE_A],opacity=1)
        a = MathTex("A",color=BLACK).move_to(circ1.get_center()).shift(LEFT * 0.3)
        b = MathTex("B",color=BLACK).move_to(circ2.get_center()).shift(RIGHT * 0.3)
        brace = Brace(VGroup(circ1,circ2),UP)
        brace_text = MathTex(r"A\cup B").next_to(title,DOWN).shift(DOWN)
        self.add(title,circ1,circ2,circ1_n,a,b,brace,brace_text,icon)
        
class Complement(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("补集")
        rect = Rectangle(width=7,height=4).set_fill(color=TEAL_B,opacity=1).next_to(title,DOWN).shift(DOWN * 1.5)
        circle = Circle(radius=1.5,color=BLACK).set_fill(color=WHITE,opacity=1).move_to(rect.get_center()).shift(LEFT * 1.2)
        brace = Brace(rect,UP)
        u = MathTex("U").next_to(brace,UP)
        a = MathTex("A",color=BLACK).move_to(circle.get_center())
        cua = MathTex(r"\complement_UA",color=BLACK).move_to(rect.get_center()).shift(RIGHT * 2)
        self.add(title,rect,circle,brace,u,a,cua,icon)


class CommonSets(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("常用数集的关系")
        c = Ellipse(width=10,height=4).set_fill(opacity=0.4).set_color(RED).next_to(title,DOWN).shift(DOWN * 0.5)
        r = Ellipse(width=8,height=3.5).set_fill(opacity=0.4).set_color(ORANGE).move_to(c.get_center()).shift(LEFT * 0.3)
        q = Ellipse(width=6,height=3).set_fill(opacity=0.4).set_color(YELLOW).move_to(r.get_center()).shift(LEFT * 0.3)
        z = Ellipse(width=4,height=2.5).set_fill(opacity=0.4).set_color(GREEN).move_to(q.get_center()).shift(LEFT * 0.3)
        n = Ellipse(width=2,height=2).set_fill(opacity=0.4).set_color(BLUE).move_to(z.get_center()).shift(LEFT * 0.3)
        self.add(title,c,r.copy().set_fill(color=BLACK,opacity=1),r,q.copy().set_fill(color=BLACK,opacity=1),q,z.copy().set_fill(color=BLACK,opacity=1),z,n.copy().set_fill(color=BLACK,opacity=1),n)
        
        c_text = MathTex(r"\mathbb C",color=RED).move_to(c.get_right()).shift(LEFT * 0.7)
        r_text = MathTex(r"\mathbb R",color=ORANGE).move_to(r.get_right()).shift(LEFT * 0.7)
        q_text = MathTex(r"\mathbb Q",color=YELLOW).move_to(q.get_right()).shift(LEFT * 0.7)
        z_text = MathTex(r"\mathbb Z",color=GREEN).move_to(z.get_right()).shift(LEFT * 0.7)
        n_text = MathTex(r"\mathbb N",color=BLUE).move_to(n.get_center())


        desc = MathTex(r"\mathbb N\subseteq \mathbb Z\subseteq \mathbb Q\subseteq \mathbb R\subseteq \mathbb C").next_to(c,DOWN)
        self.add(c_text,r_text,q_text,z_text,n_text,desc,icon)
        
class Range(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("区间")
        arrow1 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot_l1 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((1,0,0))
        dot_r1 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((4,0,0))
        up_l1 = Line((1,0,0),(1,0.3,0))
        up_r1 = Line((4,0,0),(4,0.3,0))
        line1 = Line((1,0.3,0),(4,0.3,0))
        area1 = Rectangle(width=3,height=0.3,stroke_width=0).move_to((2.5,0.15,0)).set_fill(color=YELLOW,opacity=1)
        group1 = VGroup(area1,line1,up_l1,up_r1,arrow1,dot_l1,dot_r1)
        
        arrow2 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot_l2 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((1,0,0))
        dot_r2 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((4,0,0))
        up_l2 = Line((1,0,0),(1,0.3,0))
        up_r2 = Line((4,0,0),(4,0.3,0))
        line2 = Line((1,0.3,0),(4,0.3,0))
        area2 = Rectangle(width=3,height=0.3,stroke_width=0).move_to((2.5,0.15,0)).set_fill(color=BLUE,opacity=1)
        group2 = VGroup(area2,line2,up_l2,up_r2,arrow2,dot_l2,dot_r2)
        
        arrow3 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot_l3 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((1,0,0))
        dot_r3 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((4,0,0))
        up_l3 = Line((1,0,0),(1,0.3,0))
        up_r3 = Line((4,0,0),(4,0.3,0))
        line3 = Line((1,0.3,0),(4,0.3,0))
        area3 = Rectangle(width=3,height=0.3,stroke_width=0).move_to((2.5,0.15,0)).set_fill(color=[BLUE,YELLOW],opacity=1)
        group3 = VGroup(area3,line3,up_l3,up_r3,arrow3,dot_l3,dot_r3)
        
        arrow4 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot_l4 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((1,0,0))
        dot_r4 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((4,0,0))
        up_l4 = Line((1,0,0),(1,0.3,0))
        up_r4 = Line((4,0,0),(4,0.3,0))
        line4 = Line((1,0.3,0),(4,0.3,0))
        area4 = Rectangle(width=3,height=0.3,stroke_width=0).move_to((2.5,0.15,0)).set_fill(color=[YELLOW,BLUE],opacity=1)
        group4 = VGroup(area4,line4,up_l4,up_r4,arrow4,dot_l4,dot_r4)
        
        arrow5 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot5 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((1,0,0))
        up_l5 = Line((1,0,0),(1,0.3,0))
        line5 = Line((1,0.3,0),(4.5,0.3,0))
        area5 = Rectangle(width=3.5,height=0.3,stroke_width=0).move_to((2.75,0.15,0)).set_fill(color=[BLACK,YELLOW],opacity=1)
        group5 = VGroup(area5,line5,up_l5,arrow5,dot5)
        
        arrow6 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot6 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((1,0,0))
        up_l6 = Line((1,0,0),(1,0.3,0))
        line6 = Line((1,0.3,0),(4.5,0.3,0))
        area6 = Rectangle(width=3.5,height=0.3,stroke_width=0).move_to((2.75,0.15,0)).set_fill(color=[BLACK,BLUE],opacity=1)
        group6 = VGroup(area6,line6,up_l6,arrow6,dot6)
        
        arrow7 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot7 = Circle(radius=0.1,color=WHITE).set_fill(color=WHITE,opacity=1).move_to((4,0,0))
        up_r7 = Line((4,0,0),(4,0.3,0))
        line7 = Line((0.25,0.3,0),(4,0.3,0))
        area7 = Rectangle(width=3.75,height=0.3,stroke_width=0).move_to((2.125,0.15,0)).set_fill(color=[YELLOW,BLACK],opacity=1)
        group7 = VGroup(area7,line7,up_r7,arrow7,dot7)
        
        arrow8 = Arrow((0,0,0),(5,0,0),tip_shape=StealthTip)
        dot8 = Circle(radius=0.1,color=WHITE).set_fill(color=BLACK,opacity=1).move_to((4,0,0))
        up_r8 = Line((4,0,0),(4,0.3,0))
        line8 = Line((0.25,0.3,0),(4,0.3,0))
        area8 = Rectangle(width=3.75,height=0.3,stroke_width=0).move_to((2.125,0.15,0)).set_fill(color=[BLUE,BLACK],opacity=1)
        group8 = VGroup(area8,line8,up_r8,arrow8,dot8)
        
        text1 = MathTex(r"[a,b]\{x|a\leq x \leq b\}").next_to(group1,LEFT,buff=1.5)
        text1[0][0].color = YELLOW
        text1[0][4].color = YELLOW
        text1[0][9].color = YELLOW
        text1[0][11].color = YELLOW
      
        text2 = MathTex(r"(a,b)\{x|a< x <b\}").next_to(group2,LEFT,buff=1.5)
        text2[0][0].color = BLUE
        text2[0][4].color = BLUE
        text2[0][9].color = BLUE
        text2[0][11].color = BLUE
        
        text3 = MathTex(r"[a,b)\{x|a\leq x <b\}").next_to(group3,LEFT,buff=1.5)
        text3[0][0].color = YELLOW
        text3[0][4].color = BLUE
        text3[0][9].color = YELLOW
        text3[0][11].color = BLUE
        
        text4 = MathTex(r"(a,b]\{x|a< x \leq b\}").next_to(group4,LEFT,buff=1.5)
        text4[0][0].color = BLUE
        text4[0][4].color = YELLOW
        text4[0][9].color = BLUE
        text4[0][11].color = YELLOW
        
        text5 = MathTex(r"[a,+\infty)\{x|a\leq x\}").next_to(group5,LEFT,buff=2.38)
        text5[0][0].color = YELLOW
        text5[0][5].color = BLUE
        text5[0][10].color = YELLOW
        
        text6 = MathTex(r"(a,+\infty)\{x|a< x\}").next_to(group5,LEFT,buff=2.38)
        text6[0][0].color = BLUE
        text6[0][5].color = BLUE
        text6[0][10].color = BLUE
        
        text7 = MathTex(r"(-\infty,b]\{x|x\leq b\}").next_to(group6,LEFT,buff=2.38)
        text7[0][0].color = BLUE
        text7[0][5].color = YELLOW
        text7[0][10].color = YELLOW
        
        text8 = MathTex(r"(-\infty,b)\{x|x< b\}").next_to(group6,LEFT,buff=2.38)
        text8[0][0].color = BLUE
        text8[0][5].color = BLUE
        text8[0][10].color = BLUE
        
        table = MobjectTable([[text1[0][0:5],text1[0][5:],group1],[text2[0][0:5],text2[0][5:],group2],[text3[0][0:5],text3[0][5:],group3],[text4[0][0:5],text4[0][5:],group4],[text5[0][0:6],text5[0][6:],group5],[text6[0][0:6],text6[0][6:],group6],[text7[0][0:6],text7[0][6:],group7],[text8[0][0:6],text8[0][6:],group8]],v_buff=0.2,line_config={"stroke_width":1,"color":GREY}).next_to(title,DOWN)
        table.remove(*table.get_vertical_lines())
        self.add(title,table,icon)
        
class Remember(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("巧记")
        chars = Text("交   并",weight='BOLD').scale(2).next_to(title,DOWN).shift(DOWN * 1)
        cap = MathTex(r"\cap",color=RED).move_to(chars[0]).scale(2)
        cup = MathTex(r"\cup",color=RED).move_to(chars[1].get_top()).scale(2)
        self.add(icon,title,chars,cap,cup,cap.copy().shift(DOWN * 2),cup.copy().move_to(chars[1]).shift(DOWN * 2))
        
