from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class EllipseFocusTriangle_1(Scene): #椭圆焦点三角形面积（坐标，角）
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("椭圆焦点三角形面积（坐标，角）")
        a = 3
        b = 3 ** 0.5
        c = (a ** 2 - b ** 2) ** 0.5
        x0 = 1
        
        axes = Axes(x_range=[-4,4],y_range=[-2,3],x_length=8,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        ellipse = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (1 - x0 ** 2 / a ** 2) ** 0.5]
        Q = axes @ [x0,0,0]
        m = Line(P,F1,color=YELLOW)
        n = Line(P,F2,color=BLUE)
        h = DashedLine(P,Q)
        theta = Angle(m,n)
        right = RightAngle(Line(F1,F2),h.copy().shift(DOWN),quadrant=(1,-1))

        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P").next_to(P,UR,buff=0.1)
        m_text = MathTex("m",color=YELLOW).next_to(m,UL,buff=-1)
        n_text = MathTex("n",color=BLUE).next_to(n,UR,buff=-0.7)
        h_text = MathTex("h").next_to(h,RIGHT,buff=0.1)
        theta_text = MathTex(r"\theta").next_to(theta,DL,buff=0.02)
        
        
        self.add(title,icon,axes,labels,ellipse,m,n,h,theta,O_text,F1_text,F2_text,P_text,m_text,n_text,h_text,theta_text,right)

class ParabolaFocusCircle1(Scene): #抛物线焦点弦圆（1）
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("抛物线焦点弦圆（1）")
        p = 1.6
        k = 3
        
        axes = Axes(x_range=[-2,4],y_range=[-2,3],x_length=6,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        parabola = axes.plot_implicit_curve(lambda x,y: y ** 2 - 2 * p * x)
        range = [-2 / k + p / 2,3 / k + p / 2]
        
        #print(range)
        line = axes.plot(lambda x: k * (x - p / 2),x_range=range)
        directrix = axes.plot_implicit_curve(lambda x,y: x + p / 2,color=YELLOW)


        #A = print((p / k - (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k - ((k ** 2 + 1) ** 0.5 * p / k) / k)
        O = axes @ (0,0,0)
        A = axes.c2p(((p / k + (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k + ((k ** 2 + 1) ** 0.5 * p) / k)
        B = axes.c2p(((p / k - (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k - ((k ** 2 + 1) ** 0.5 * p) / k)
        F = axes @ (p / 2,0)
        G = (A + B) / 2
        H = ((axes @ (-p / 2,0))[0],G[1],0)
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        A_text = MathTex("A").next_to(A,UL,buff=0.2)
        B_text = MathTex("B").next_to(B,DOWN,buff=0.3)
        G_text = MathTex("G").next_to(G,RIGHT,buff=0.1)
        H_text = MathTex("H").next_to(H,LEFT,buff=0.1)
        F_text = MathTex("F").next_to(F,DOWN,buff=0.2)
        m_text = MathTex(r"m",color=YELLOW).next_to(directrix.get_top(),LEFT,buff=0.1).shift(DOWN * 0.3)
        y = Line(O,axes @ (0,5,0))
        radius = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5 / 2
        circ = Circle(radius=radius,color=BLUE).move_to(G)
        GH = Line(G,H)
        angyHG = RightAngle(Line(((axes @ (-p / 2,0))[0],-1,0),((axes @ (-p / 2,0))[0],1,0)),GH.copy().shift(LEFT),quadrant=(1,-1))
        #print(A)
        self.add(title,icon,axes,parabola,line,circ,O_text,A_text,B_text,G_text,F_text,H_text,GH,angyHG,labels,Dot(G),directrix,m_text)

class ParabolaFocusCircle2(Scene): #抛物线焦点弦圆（2）
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("抛物线焦点弦圆（2）")
        p = 1.5
        k = 2
        
        axes = Axes(x_range=[-2,4],y_range=[-2,3],x_length=6,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        parabola = axes.plot_implicit_curve(lambda x,y: y ** 2 - 2 * p * x)
        range = [-2 / k + p / 2,3 / k + p / 2]
        
        #print(range)
        line = axes.plot(lambda x: k * (x - p / 2),x_range=range)
        directrix = axes.plot_implicit_curve(lambda x,y: x + p / 2)

        #A = print((p / k - (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k - ((k ** 2 + 1) ** 0.5 * p / k) / k)
        O = axes @ (0,0,0)
        A = axes.c2p(((p / k + (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k + ((k ** 2 + 1) ** 0.5 * p) / k)
        F = axes @ (p / 2,0)
        G = (A + F) / 2
        H = (O[0],G[1],0)
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        A_text = MathTex("A").next_to(A,UL,buff=0.2)
        G_text = MathTex("G").next_to(G,RIGHT,buff=0.1)
        H_text = MathTex("H").next_to(H,LEFT,buff=0.1)
        F_text = MathTex("F").next_to(F,DOWN,buff=0.2)
        y = Line(O,axes @ (0,5,0))
        radius = ((A[0] - F[0]) ** 2 + (A[1] - F[1]) ** 2) ** 0.5 / 2
        circ = Circle(radius=radius,color=BLUE).move_to(G)
        GH = Line(G,H)
        angyHG = RightAngle(y,GH.copy().shift(LEFT),quadrant=(1,-1))
        #print(A)
        self.add(title,icon,axes,parabola,line,circ,GH,O_text,A_text,G_text,H_text,F_text,labels,angyHG,Dot(G))
        
class HyperbolaFocusAsymptoteTriangleArea(Scene): #双曲线的焦点—渐近线三角形
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("双曲线的焦点—渐近线三角形")
        a = 1
        b = 1.5
        c = (a ** 2 + b ** 2) ** 0.5
        
        axes = Axes(x_range=[-2.5,2.5],y_range=[-2,2],x_length=7.5,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        hyperbola = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 - y ** 2 / b ** 2 - 1)
        asymptote = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 - y ** 2 / b ** 2)

        O = axes @ [0,0,0]
        F2 = axes @ [c,0,0]
        B = axes @ [a ** 2 / c,a * b / c]
        a = Line(B,O,color=YELLOW)
        b = Line(B,F2,color=BLUE)
        c = Line(O,F2,color=RED)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1).shift(LEFT * 0.2)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        B_text = MathTex("B").next_to(B,UL,buff=0.1)
        a_text = MathTex("a",color=YELLOW).next_to(a,UL,buff=-0.4)
        b_text = MathTex("b",color=BLUE).next_to(b,UR,buff=-0.7)
        c_text = MathTex("c",color=RED).next_to(c,DOWN,buff=0.1).shift(LEFT * 0.2)
        right = RightAngle(a,b)
        
        self.add(title,icon,axes,labels,hyperbola,asymptote,a,b,c,O_text,F2_text,B_text,a_text,b_text,c_text,right)

class ParabolaFocusChordLength(Scene): #抛物线焦点弦长（角）
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("抛物线焦点弦长（角）")
        p = 1.3
        k = 1
        
        axes = Axes(x_range=[-2,5],y_range=[-1.5,4],x_length=7,y_length=5.5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        parabola = axes.plot_implicit_curve(lambda x,y: y ** 2 - 2 * p * x)
        range = [-1 / k + p / 2,4 / k + p / 2]
        
        #print(range)
        line = axes.plot(lambda x: k * (x - p / 2),x_range=range)
        directrix = axes.plot_implicit_curve(lambda x,y: x + p / 2,color=YELLOW)

        #A = print((p / k - (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k - ((k ** 2 + 1) ** 0.5 * p / k) / k)
        O = axes @ (0,0,0)
        A = axes @ (((p / k + (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k + ((k ** 2 + 1) ** 0.5 * p) / k)
        B = axes @ (((p / k - (k ** 2 + 1) ** 0.5 * p / k) ** 2) / (2 * p),p / k - ((k ** 2 + 1) ** 0.5 * p) / k)
        F = axes @ (p / 2,0)
        D = ((axes @ (-p / 2,0))[0],A[1],0)
        C = (F[0],A[1],0)
        AD = Line(A,D)
        FC = Line(F,C)
        right = RightAngle(Line(C,A),Line(C,F))
        theta = Angle(Line(F,A),Line(F,axes @ (3,0,0)),other_angle=True)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        A_text = MathTex("A").next_to(A,UL,buff=0.1)
        B_text = MathTex("B").next_to(B,RIGHT,buff=0.1)
        F_text = MathTex("F").next_to(F,UL,buff=0.1)
        D_text = MathTex("D").next_to(D,UR,buff=0.1)
        C_text = MathTex("C").next_to(C,UP,buff=0.1)
        l_text = MathTex("l").next_to(A,UR,buff=0.2).shift(UP * 0.22 + RIGHT * 0.6)
        m_text = MathTex("m",color=YELLOW).next_to(directrix.get_top(),LEFT,buff=0.1).shift(DOWN * 0.3)
        theta_text = MathTex(r"\theta").next_to(theta,RIGHT,buff=0.1).shift(UP * 0.1)
        
        self.add(title,icon,axes,labels,parabola,line,directrix,AD,FC,O_text,A_text,B_text,F_text,D_text,C_text,m_text,right,theta,theta_text,l_text)

class EllipseFocusRadiusFormula(Scene): #椭圆焦点半径公式
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("椭圆焦点半径公式")
        a = 3
        b = 3 ** 0.5
        c = (a ** 2 - b ** 2) ** 0.5
        x0 = 1
        
        axes = Axes(x_range=[-4,4],y_range=[-2,3],x_length=8,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        ellipse = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (1 - x0 ** 2 / a ** 2) ** 0.5]
        m = Line(P,F1,color=YELLOW)
        n = Line(P,F2,color=BLUE)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P(x_0,y_0)").next_to(P,UR,buff=0.1)
        m_text = MathTex("a+ex_0",color=YELLOW).next_to(m,UL,buff=-1)
        n_text = MathTex("a-ex_0",color=BLUE).next_to(n,UR,buff=-0.7)
        self.add(title,icon,axes,labels,ellipse,SurroundingRectangle(m_text,stroke_width=0).set_fill(color=BLACK,opacity=0.6),SurroundingRectangle(n_text,stroke_width=0).set_fill(color=BLACK,opacity=0.6),m,n,O_text,F1_text,F2_text,P_text,m_text,n_text)

class EllipsePerpendicularDiameterTheroem(Scene): #椭圆的垂径定理
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("椭圆的垂径定理")
        a = 3
        b = 3 ** 0.5
        x_1 = 2.5
        y_1 = b * (1 - x_1 ** 2 / a ** 2) ** 0.5
        
        x_0 = 0.5
        y_0 = b * (1 - x_0 ** 2 / a ** 2) ** 0.5
        
        axes = Axes(x_range=[-4,4],y_range=[-2,3],x_length=8,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        ellipse = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        A = axes @ [-x_1,-y_1,0]
        B = axes @ [x_1,y_1,0]
        P = axes @ [x_0,y_0,0]
        AP = Line(A,P)
        AB = Line(A,B)
        BP = Line(B,P)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        A_text = MathTex("A(x_1,y_1)").next_to(A,DL,buff=0.1)
        B_text = MathTex("B(x_2,y_2)").next_to(B,UR,buff=0.1)
        P_text = MathTex("P(x_0,y_0)").next_to(P,UR,buff=0.1)
        
        
        self.add(title,icon,axes,labels,ellipse,AP,AB,BP,O_text,A_text,B_text,P_text)
        
class EllipseEccentricityTriangularForm(Scene): #椭圆离心三角式
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("椭圆离心三角式")
        a = 3
        b = 3 ** 0.5
        c = (a ** 2 - b ** 2) ** 0.5
        x0 = 1
        
        axes = Axes(x_range=[-4,4],y_range=[-2,3],x_length=8,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        ellipse = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (1 - x0 ** 2 / a ** 2) ** 0.5]
        m = Line(F1,P)
        n = Line(F2,P)
        alpha = Angle(m,Line(F1,F2),color=YELLOW,other_angle=True)
        beta = Angle(n,Line(F2,F1),color=BLUE)
        theta = Angle(Line(P,F1),Line(P,F2),color=RED)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P").next_to(P,UR,buff=0.1)
        alpha_text = MathTex(r"\alpha",color=YELLOW).next_to(alpha,RIGHT,buff=0.1).shift(UP * 0.05)
        beta_text = MathTex(r"\beta",color=BLUE).next_to(beta,LEFT,buff=0.1).shift(UP * 0.05)
        theta_text = MathTex(r"\theta",color=RED).next_to(theta,DOWN,buff=0.1)
        
        self.add(title,icon,axes,labels,ellipse,O_text,F1_text,F2_text,P_text,m,n,alpha,beta,theta,alpha_text,beta_text,theta_text)

class HyperbolaFocusRadiusFormula(Scene): #双曲线焦半径公式
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("双曲线焦半径公式")
        a = 1
        b = 1.5
        c = (a ** 2 + b ** 2) ** 0.5
        x0 = 1.5
        
        axes = Axes(x_range=[-2.5,2.5],y_range=[-2,2],x_length=7.5,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        hyperbola = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 - y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (x0 ** 2 / a ** 2 - 1) ** 0.5]
        m = Line(P,F1,color=YELLOW)
        n = Line(P,F2,color=BLUE)
        
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P(x_0,y_0)").next_to(P,RIGHT,buff=0.1)
        m_text = MathTex("|a+ex_0|",color=YELLOW).next_to(m,UL,buff=-1.5)
        n_text = MathTex("|a-ex_0|",color=BLUE).next_to(n,UR,buff=-0.3).shift(DOWN + RIGHT * 0.2)
        self.add(title,icon,axes,labels,hyperbola,SurroundingRectangle(m_text,stroke_width=0).set_fill(color=BLACK,opacity=0.6),SurroundingRectangle(n_text,stroke_width=0).set_fill(color=BLACK,opacity=0.6),m,n,O_text,F1_text,F2_text,P_text,m_text,n_text)

class HyperbolaPerpendicularDiameterTheroem(Scene): #双曲线的垂径定理
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("双曲线的垂径定理")
        a = 1
        b = 1.5
        x_1 = -1.05
        y_1 = b * (x_1 ** 2 / a ** 2 - 1) ** 0.5
        
        x_0 = 1.5
        y_0 = b * (x_0 ** 2 / a ** 2 - 1) ** 0.5
        
        axes = Axes(x_range=[-2.5,2.5],y_range=[-2,2],x_length=7.5,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        hyperbola = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 - y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        A = axes @ [x_1,y_1,0]
        B = axes @ [-x_1,-y_1,0]
        P = axes @ [x_0,y_0,0]
        AP = Line(A,P)
        AB = Line(A,B)
        BP = Line(B,P)
        
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        A_text = MathTex("A(x_1,y_1)").next_to(A,LEFT,buff=0.1)
        B_text = MathTex("B(x_2,y_2)").next_to(B,RIGHT,buff=0.1)
        P_text = MathTex("P(x_0,y_0)").next_to(P,RIGHT,buff=0.1)
        self.add(title,icon,axes,labels,hyperbola,AP,AB,BP,O_text,A_text,B_text,P_text)
        
        
class EllipseFocusTriangle_2(Scene): #椭圆焦点三角形面积（圆）
    def construct(self):
        def distance(a,b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("椭圆焦点三角形面积（圆）")
        a = 3
        b = 3 ** 0.5
        c = (a ** 2 - b ** 2) ** 0.5
        x0 = 1
        
        axes = Axes(x_range=[-4,4],y_range=[-2,3],x_length=8,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        ellipse = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 + y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (1 - x0 ** 2 / a ** 2) ** 0.5]
        Q = axes @ [x0,0,0]
        PF1 = Line(P,F1)
        PF2 = Line(P,F2)
        perimeter = distance(P,F2) + distance(F1,F2) + distance(P,F1)
        xi = (distance(P,F2) * F1[0] + distance(F1,F2) * P[0] + distance(P,F1) * F2[0]) / perimeter
        yi = (distance(P,F2) * F1[1] + distance(F1,F2) * P[1] + distance(P,F1) * F2[1]) / perimeter
        area = (perimeter / 2 * (perimeter / 2 - distance(P,F2)) * (perimeter / 2 - distance(P,F1)) * (perimeter / 2 - distance(F1,F2))) ** 0.5
        
        circle = Circle(radius=2 * area / perimeter,color=YELLOW).move_to((xi,yi,0))
        
        l1 = Line((xi,yi,0),PF1.get_projection((xi,yi,0)),color=BLUE)
        l2 = Line((xi,yi,0),PF2.get_projection((xi,yi,0)),color=BLUE)
        l3 = Line((xi,yi,0),Line(F1,F2).get_projection((xi,yi,0)),color=BLUE)
        r1 = MathTex("r",color=BLUE).next_to(l1,RIGHT,buff=-0.06)
        r2 = MathTex("r",color=BLUE).next_to(l2,DR,buff=-0.25)
        r3 = MathTex("r",color=BLUE).next_to(l3,LEFT,buff=0.05)
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P").next_to(P,UR,buff=0.1)
        
        self.add(title,icon,axes,labels,ellipse,O_text,F1_text,F2_text,P_text,PF1,PF2,l1,l2,l3,r1,r2,r3,circle)

class HyperbolaFocusTriangle(Scene): #双曲线焦点三角形面积（坐标，角）
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("双曲线焦点三角形面积（坐标，角）")
        
        a = 1
        b = 1.5
        c = (a ** 2 + b ** 2) ** 0.5
        x0 = 1.4
        
        axes = Axes(x_range=[-2.5,2.5],y_range=[-2,2],x_length=7.5,y_length=6,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        hyperbola = axes.plot_implicit_curve(lambda x,y: x ** 2 / a ** 2 - y ** 2 / b ** 2 - 1)

        O = axes @ [0,0,0]
        F1 = axes @ [-c,0,0]
        F2 = axes @ [c,0,0]
        P = axes @ [x0,b * (x0 ** 2 / a ** 2 - 1) ** 0.5]
        Q = axes @ [x0,0,0]
        m = Line(P,F1,color=YELLOW)
        n = Line(P,F2,color=BLUE)
        h = DashedLine(P,Q)
        theta = Angle(m,n)
        right = RightAngle(Line(F1,F2),h.copy().shift(DOWN),quadrant=(1,-1))

        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        F1_text = MathTex("F_1").next_to(F1,DOWN,buff=0.1)
        F2_text = MathTex("F_2").next_to(F2,DOWN,buff=0.1)
        P_text = MathTex("P").next_to(P,UR,buff=0.1)
        m_text = MathTex("m",color=YELLOW).next_to(m,UL,buff=-2).shift(UP)
        n_text = MathTex("n",color=BLUE).next_to(n,UR,buff=-0.2).shift(DOWN)
        h_text = MathTex("h").next_to(h,LEFT,buff=0.1)
        theta_text = MathTex(r"\theta").next_to(theta,DL,buff=0.02)
        
        
        self.add(title,icon,axes,labels,hyperbola,m,n,h,O_text,F1_text,F2_text,P_text,m_text,n_text,h_text,theta,theta_text,right)

