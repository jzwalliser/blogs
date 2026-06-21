from manim import *
import math

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class TimeComplexity(Scene):
    def construct(self):
        title = Title("时间复杂度")
        axes = Axes(x_range=[0,60],y_range=[0,100],x_length=10,y_length=5,axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False}).next_to(title,DOWN).shift(DOWN * 0.5)
        labels = axes.get_axis_labels(MathTex("x"),MathTex("y"))
        labels[0].shift(DOWN * 0.8)
        labels[1].shift(LEFT * 0.8).shift(DOWN * 0.5)
        log = axes.plot(lambda x: math.log(x,10),x_range=[1,60],color=RED_A)
        sqrt = square = axes.plot(lambda x: x ** 0.5,x_range=[0,60],color=BLUE_A)
        linear = axes.plot(lambda x: x,x_range=[0,60],color=GREEN_A)
        nlog = axes.plot(lambda x: x * math.log(x,10),x_range=[1,57],color=TEAL_A)
        square = axes.plot(lambda x: x ** 2,x_range=[0,100 ** 0.5],color=LIGHT_PINK)
        expo = axes.plot(lambda x: 2 ** x,x_range=[0,math.log(100,2)],color=PURPLE_A)
        fact = axes.plot_line_graph([0,1,2,3,4,4.3],[1,1,2,6,24,100],add_vertex_dots=False).set_color(YELLOW_A)
        self.add(title,axes,labels,log,sqrt,linear,nlog,square,expo,fact)


        logtext = MathTex(r"O({\rm log}n)",color=RED_A).next_to(log,RIGHT)
        sqrttext = MathTex(r"O(\sqrt n)",color=BLUE_A).next_to(sqrt,RIGHT).shift(UP * 0.4)
        lineartext = MathTex(r"O(n)",color=GREEN_A).next_to(linear,RIGHT).shift(UP * 1.5)
        nlogtext = MathTex(r"O(n{\rm log}n)",color=TEAL_A).next_to(nlog,RIGHT).shift(UP * 2.5)
        squaretext = MathTex(r"O(n^2)",color=LIGHT_PINK).next_to(square,UP).shift(RIGHT * 1.5).shift(DOWN)
        expotext = MathTex(r"O(2^n)",color=PURPLE_A).next_to(expo,UP).shift(RIGHT * 1.1).shift(DOWN * 0.3)
        facttext = MathTex(r"O(n!)",color=YELLOW_A).next_to(fact,UP).shift(DOWN * 0.3)
        
        O = axes @ [0,0,0]
        O_text = MathTex("O").next_to(O,DL,buff=0.1)
        self.add(logtext,sqrttext,lineartext,nlogtext,squaretext,expotext,facttext,O_text)


