from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class SinCosTan(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("同角三角函数关系")
        axes = Axes(x_range=[-1.4,1.4],y_range=[-1.4,1.4],x_length=6,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        circle = axes.plot_implicit_curve(lambda x,y: x**2 + y**2 - 1)
        o = axes.c2p(0,0)
        o_text = MathTex("O").next_to(o,DL,buff=0.1)
        p = axes.c2p(0.6,0.8)
        p_text = MathTex("P").next_to(p,UR,buff=0.1)
        q = axes.c2p(0.6,0)
        q_text = MathTex("Q").next_to(q,DOWN,buff=0.1)
        OP = Line(o,p)
        PQ = Line(q,p)
        OQ = Line(o,q)
        x = MathTex("x").next_to(OQ,DOWN,buff=0.1)
        y = MathTex("y").next_to(PQ,RIGHT,buff=0.1)
        r = MathTex("r").next_to(OP,UL,buff=-0.7)
        angle = Angle(OQ,OP)
        alpha = MathTex(r"\alpha").next_to(angle,RIGHT,buff=0.1).shift(UP * 0.1)
        self.add(title,axes,circle,labels,o_text,p_text,q_text,OP,PQ,OQ,x,y,r,angle,alpha,icon)
        
class VectorAndCos(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("和差公式")
        axes = Axes(x_range=[-1.4,1.4],y_range=[-1.4,1.4],x_length=6,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        circle = axes.plot_implicit_curve(lambda x,y: x**2 + y**2 - 1)
        o = axes.c2p(0,0)
        o_text = MathTex("O").next_to(o,DL,buff=0.1)
        a = axes.c2p(-0.5,3**0.5/2)
        a_text = MathTex(r"A(\cos \alpha,\sin \alpha)").next_to(a,UL,buff=0.1)
        b = axes.c2p(0.6,0.8)
        b_text = MathTex(r"B(\cos \beta,\sin \beta)").next_to(b,UR,buff=0.1)
        a_text[0][5].color = YELLOW
        a_text[0][10].color = YELLOW
        b_text[0][5].color = BLUE
        b_text[0][10].color = BLUE
        x = axes.c2p(1,0)
        OA = Line(o,a)
        OB = Line(o,b)
        Ox = Line(o,x)
        anglea = Angle(Ox,OA,color=YELLOW)
        angleb = Angle(Ox,OB,radius=0.7,color=BLUE)
        alpha = MathTex(r"\alpha",color=YELLOW).next_to(anglea,UP,buff=0.1)
        beta = MathTex(r"\beta",color=BLUE).next_to(angleb,RIGHT,buff=0.1).shift(UP * 0.1)
        self.add(title,axes,circle,labels,o_text,a_text,b_text,OA,OB,anglea,angleb,alpha,beta,icon)
        

