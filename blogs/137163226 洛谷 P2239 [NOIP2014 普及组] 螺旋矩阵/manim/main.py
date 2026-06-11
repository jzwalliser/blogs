from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class SpiralMatrix(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("螺旋矩阵 ($n=8$)")
        group = VGroup()
        colors = [YELLOW] * 81
        textcol = [BLACK] * 81
        text = [r"{}_i\backslash^j",1,2,3,4,5,6,7,8,1,1,2,3,4,5,6,7,8,2,28,29,30,31,32,33,34,9,3,27,48,49,50,51,52,35,10,4,26,47,60,61,62,53,36,11,5,25,46,59,64,63,54,37,12,6,24,45,58,57,56,55,38,13,7,23,44,43,42,41,40,39,14,8,22,21,20,19,18,17,16,15]
        for i in range(8):
            for j in range(8):
                colors[(1 + i) * 9 + 1 + j] = GREEN
        for i in range(6):
            for j in range(6):
                colors[(2 + i) * 9 + 2 + j] = BLUE
        for i in range(4):
            for j in range(4):
                colors[(3 + i) * 9 + 3 + j] = RED
                textcol[(3 + i) * 9 + 3 + j] = WHITE
        for i in range(2):
            for j in range(2):
                colors[(4 + i) * 9 + 4 + j] = PINK
                textcol[(4 + i) * 9 + 4 + j] = WHITE
        for i in range(9):
            for j in range(9):
                rect = Rectangle(width=0.7,height=0.7,stroke_width=1).set_fill(color=colors[i * 9 + j],opacity=1).move_to((i * 0.7,-j * 0.7,0))
                latex = str(text[i + j * 9])
                if i == 0 or j == 0:
                    latex = r"\mathbf " + latex + ""
                num = MathTex(latex,color=textcol[i + j * 9]).move_to(rect.get_center())
                group += VGroup(rect,num)
        group.next_to(title,DOWN)
        self.add(title,group,icon)


class Area(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("面积法")
        bigsquare = Rectangle(width=5,height=5).set_fill(opacity=0.4).set_color([BLUE,GREEN]).next_to(title,DOWN).shift(DOWN).shift(LEFT * 3)
        smallsquare = Rectangle(width=2.5,height=2.5).set_fill(opacity=0.4).set_color([YELLOW,RED]).move_to(bigsquare.get_center())
        brace1 = Brace(bigsquare,UP)
        brace2 = Brace(smallsquare,UP)
        n_text = MathTex("n").next_to(brace1,UP)
        minus_text = MathTex("n-2m").next_to(brace2,UP)
        line1 = DoubleArrow(bigsquare.get_left(),smallsquare.get_left(),buff=0,tip_length=0.2)
        m1 = MathTex("m").next_to(line1,UP)

        line2 = DoubleArrow(bigsquare.get_right(),smallsquare.get_right(),buff=0,tip_length=0.2)
        m2 = MathTex("m").next_to(line2,UP)
        
        total = MathTex(r"S_{\text{总}}=n^2").shift(RIGHT * 2 + UP)
        red = MathTex(r"S_{\text{红}}=(n-2m)^2").next_to(total,DOWN,aligned_edge=LEFT)
        green = MathTex(r"S_{\text{绿}}=n^2-(n-2m)^2").next_to(red,DOWN,aligned_edge=LEFT)
        self.add(title,bigsquare,smallsquare.copy().set_fill(color=BLACK,opacity=1),smallsquare)
        self.add(brace1,brace2,n_text,minus_text,line1,m1,line2,m2,total,red,green,icon)
        
class Sections(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("区域与偏移")
        bigsquare = Rectangle(width=5,height=5).next_to(title,DOWN).shift(DOWN * 0.5)
        smallsquare = Rectangle(width=3.5,height=3.5).set_fill(opacity=1).set_color(WHITE).move_to(bigsquare.get_center())
        sec1 = Rectangle(width=5,height=0.75).move_to([0,(bigsquare.get_top()[1] + smallsquare.get_top()[1]) / 2,0]).set_fill(opacity=0.4).set_color([BLUE,GREEN])
        sec2 = Rectangle(width=0.75,height=4.25).move_to([(bigsquare.get_right()[0] + smallsquare.get_right()[0]) / 2,(sec1.get_bottom()[1] + bigsquare.get_bottom()[1]) / 2,0]).set_fill(opacity=0.4).set_color([RED,ORANGE])
        sec3 = Rectangle(width=4.25,height=0.75).move_to([(bigsquare.get_left()[0] + sec2.get_left()[0]) / 2,(bigsquare.get_bottom()[1] + smallsquare.get_bottom()[1]) / 2,0]).set_fill(opacity=0.4).set_color([PINK,PURPLE])
        sec4 = Rectangle(width=0.75,height=3.5).move_to([(bigsquare.get_left()[0] + smallsquare.get_left()[0]) / 2,(sec1.get_bottom()[1] + sec3.get_top()[1]) / 2,0]).set_fill(opacity=0.4).set_color([YELLOW,GOLD])
        sec1_text = Text("区域①").move_to(sec1.get_center()).scale(0.6)
        sec2_text = Text("区\n域\n②").move_to(sec2.get_center()).scale(0.6)
        sec3_text = Text("区域③").move_to(sec3.get_center()).scale(0.6)
        sec4_text = Text("区\n域\n④").move_to(sec4.get_center()).scale(0.6)
        self.add(title,icon,smallsquare,sec1,sec2,sec3,sec4,sec1_text,sec2_text,sec3_text,sec4_text)
        
