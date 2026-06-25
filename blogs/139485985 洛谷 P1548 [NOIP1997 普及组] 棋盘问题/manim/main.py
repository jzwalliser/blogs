from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Cond1(Scene):
    def construct(self):
        title = Title("讨论一")
        matrix = VDict()
        for i in range(4):
            for j in range(3):
                matrix[f"{i + 1},{j + 1}"] = Rectangle(width=1,height=1).move_to((i,-j,0))
        self.add(title,matrix.next_to(title,DOWN).shift(DOWN))
        self.add(Circle(radius=0.2).move_to(matrix["1,1"].get_corner(UL)))
        for i in range(4):
            for j in range(3):
                self.add(Cross().scale(0.2).move_to(matrix[f"{i + 1},{j + 1}"].get_corner(DR)))
        brace1 = Brace(VGroup(matrix["2,3"],matrix["4,3"]))
        num1 = Tex("4").next_to(brace1,DOWN)
        brace2 = Brace(VGroup(matrix["4,3"],matrix["4,2"]),RIGHT)
        num2 = Tex("3").next_to(brace2,RIGHT)
        self.add(brace1,num1,brace2,num2)
        self.add(MathTex(r"3\times4=12").next_to(matrix,DOWN).shift(DOWN * 1.5))

class Cond2(Scene):
    def construct(self):
        title = Title("讨论二")
        matrix = VDict()
        for i in range(4):
            for j in range(3):
                matrix[f"{i + 1},{j + 1}"] = Rectangle(width=1,height=1).move_to((i,-j,0))
        self.add(title,matrix.next_to(title,DOWN).shift(DOWN))
        self.add(Circle(radius=0.2).move_to(matrix["1,2"].get_corner(UL)))
        for i in range(4):
            for j in range(2):
                self.add(Cross().scale(0.2).move_to(matrix[f"{i + 1},{j + 2}"].get_corner(DR)))
        brace1 = Brace(VGroup(matrix["2,3"],matrix["4,3"]))
        num1 = Tex("4").next_to(brace1,DOWN)
        brace2 = Brace(matrix["4,3"],RIGHT)
        num2 = Tex("2").next_to(brace2,RIGHT)
        self.add(brace1,num1,brace2,num2)
        self.add(MathTex(r"2\times4=8").next_to(matrix,DOWN).shift(DOWN * 1.5))

class Cond3(Scene):
    def construct(self):
        title = Title("讨论三")
        matrix = VDict()
        for i in range(4):
            for j in range(3):
                matrix[f"{i + 1},{j + 1}"] = Rectangle(width=1,height=1).move_to((i,-j,0))
        self.add(title,matrix.next_to(title,DOWN).shift(DOWN))
        self.add(Circle(radius=0.2).move_to(matrix["1,3"].get_corner(UL)))
        for i in range(4):
            for j in range(1):
                self.add(Cross().scale(0.2).move_to(matrix[f"{i + 1},{j + 3}"].get_corner(DR)))
        brace1 = Brace(VGroup(matrix["2,3"],matrix["4,3"]))
        num1 = Tex("4").next_to(brace1,DOWN)
        brace2 = Arrow(matrix["4,3"].get_corner(DR),matrix["4,3"].get_corner(DR) + [1,0,0])
        num2 = Tex("1").next_to(brace2,RIGHT)
        self.add(brace1,num1,brace2,num2)
        self.add(MathTex(r"1\times4=4").next_to(matrix,DOWN).shift(DOWN * 1.5))

class Cond4(Scene):
    def construct(self):
        title = Title("讨论四")
        matrix = VDict()
        for i in range(4):
            for j in range(3):
                matrix[f"{i + 1},{j + 1}"] = Rectangle(width=1,height=1).move_to((i,-j,0))
        self.add(title,matrix.next_to(title,DOWN).shift(DOWN))
        self.add(Circle(radius=0.2).move_to(matrix["2,1"].get_corner(UL)))
        for i in range(3):
            for j in range(3):
                self.add(Cross().scale(0.2).move_to(matrix[f"{i + 2},{j + 1}"].get_corner(DR)))
        brace1 = Brace(VGroup(matrix["3,3"],matrix["4,3"]))
        num1 = Tex("3").next_to(brace1,DOWN)
        brace2 = Brace(VGroup(matrix["4,3"],matrix["4,2"]),RIGHT)
        num2 = Tex("3").next_to(brace2,RIGHT)
        self.add(brace1,num1,brace2,num2)
        self.add(MathTex(r"3\times3=9").next_to(matrix,DOWN).shift(DOWN * 1.5))

class Cond5(Scene):
    def construct(self):
        title = Title("讨论五")
        matrix = VDict()
        for i in range(4):
            for j in range(3):
                matrix[f"{i + 1},{j + 1}"] = Rectangle(width=1,height=1).move_to((i,-j,0))
        self.add(title,matrix.next_to(title,DOWN).shift(DOWN))
        self.add(Circle(radius=0.2).move_to(matrix["3,1"].get_corner(UL)))
        for i in range(2):
            for j in range(3):
                self.add(Cross().scale(0.2).move_to(matrix[f"{i + 3},{j + 1}"].get_corner(DR)))
        brace1 = Brace(VGroup(matrix["4,3"]))
        num1 = Tex("2").next_to(brace1,DOWN)
        brace2 = Brace(VGroup(matrix["4,3"],matrix["4,2"]),RIGHT)
        num2 = Tex("3").next_to(brace2,RIGHT)
        self.add(brace1,num1,brace2,num2)
        self.add(MathTex(r"3\times2=6").next_to(matrix,DOWN).shift(DOWN * 1.5))
