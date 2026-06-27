from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Breadboard(Scene):
    def construct(self):
        title = Title("面包板")
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        breadboard = VDict()
        lines = VDict()
        
        #self.add(ImageMobject("breadboard.jpg").scale(2).shift(UP * 0.1).shift(LEFT * 0.36))
        breadboard["board"] = Rectangle(width=4.82,height=7.39,fill_opacity=1,fill_color=WHITE,stroke_width=0).move_to((0,0,0))
        lines["leftred"] = Line((-2.3,3.3,0),(-2.3,-3.3,0),color=RED)
        lines["leftblue"] = Line((-1.6,3.3,0),(-1.6,-3.3,0),color=BLUE)
        lines["rightred"] = Line((2.3,3.3,0),(2.3,-3.3,0),color=BLUE)
        lines["rightblue"] = Line((1.6,3.3,0),(1.6,-3.3,0),color=RED)
        
        breadboard["lines"] = lines
        
        font = "Arimo"
        
        power = VDict()
        
        for i in range(5):
            for j in range(5):
                for idx,k in enumerate([-2.07,-1.83,1.83,2.07]):
                    power[str([1,2,3,4][idx]) + "," + f"{i * 5 + j + 1}"] = (Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((k,3.17 - 5.45 / 4 * i - 0.23 * j,0)))
        breadboard["power"] = power
        
        numbers = VDict()
        component = VDict()
        for i in range(30):
            numbers["1," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((-1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            numbers["2," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            for j in range(5):
                component[chr(97 + j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((-1.22 + 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
                component[chr(106 - j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((1.22 - 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
        
        breadboard["numbers"] = numbers
        breadboard["component"] = component
        
        chars1 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,3.5,0))
        
        alphabets = VDict()
        for i in range(5):
            chars1[i].move_to((-1.2 + 0.92 / 4 * i,chars1[i].get_y(),0))
            alphabets["1" + "abcdejihgf"[i]] = chars1[i]
        
        for i in range(5):
            chars1[i + 5].move_to((1.2 - 0.92 / 4 * i,chars1[i + 5].get_y(),0))
            alphabets["1" + "abcdejihgf"[i + 5]] = chars1[i + 5]
        
        chars2 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,-3.5,0))
        
        for i in range(5):
            chars2[i].move_to((-1.2 + 0.92 / 4 * i,chars2[i].get_y(),0))
            alphabets["2" + "abcdejihgf"[i]] = chars2[i]
        
        for i in range(5):
            chars2[i + 5].move_to((1.2 - 0.92 / 4 * i,chars2[i + 5].get_y(),0))
            alphabets["2" + "abcdejihgf"[i + 5]] = chars2[i + 5]
        
        breadboard["alphabets"] = alphabets
        breadboard["groove"] = Rectangle(width=0.17,height=7.39,fill_opacity=1,fill_color=GREY_A,stroke_width=0).move_to((0,0,0))
        powerlabel = VDict()
        
        powerlabel["ul+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,3.52,0))
        powerlabel["ul-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,3.52,0))
        powerlabel["ur+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,3.52,0))
        powerlabel["ur-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,3.52,0))
        powerlabel["dl+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,-3.52,0))
        powerlabel["dl-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,-3.52,0))
        powerlabel["dr+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,-3.52,0))
        powerlabel["dr-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,-3.52,0))
        breadboard["powerlabel"] = powerlabel
        
        breadboard.scale(0.8).next_to(title,DOWN)
        
        self.add(title,icon,breadboard)
        
class BreadboardLabel(Scene):
    def construct(self):
        title = Title("面包板详解：区域划分")
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        breadboard = VDict()
        lines = VDict()
        
        #self.add(ImageMobject("breadboard.jpg").scale(2).shift(UP * 0.1).shift(LEFT * 0.36))
        breadboard["board"] = Rectangle(width=4.82,height=7.39,fill_opacity=1,fill_color=WHITE,stroke_width=0).move_to((0,0,0))
        lines["leftred"] = Line((-2.3,3.3,0),(-2.3,-3.3,0),color=RED)
        lines["leftblue"] = Line((-1.6,3.3,0),(-1.6,-3.3,0),color=BLUE)
        lines["rightred"] = Line((2.3,3.3,0),(2.3,-3.3,0),color=BLUE)
        lines["rightblue"] = Line((1.6,3.3,0),(1.6,-3.3,0),color=RED)
        
        breadboard["lines"] = lines
        
        font = "Arimo"
        
        power = VDict()
        
        for i in range(5):
            for j in range(5):
                for idx,k in enumerate([-2.07,-1.83,1.83,2.07]):
                    power[str([1,2,3,4][idx]) + "," + f"{i * 5 + j + 1}"] = (Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((k,3.17 - 5.45 / 4 * i - 0.23 * j,0)))
        breadboard["power"] = power
        
        numbers = VDict()
        component = VDict()
        for i in range(30):
            numbers["1," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((-1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            numbers["2," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            for j in range(5):
                component[chr(97 + j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((-1.22 + 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
                component[chr(106 - j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((1.22 - 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
        
        breadboard["numbers"] = numbers
        breadboard["component"] = component
        
        chars1 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,3.5,0))
        
        alphabets = VDict()
        for i in range(5):
            chars1[i].move_to((-1.2 + 0.92 / 4 * i,chars1[i].get_y(),0))
            alphabets["1" + "abcdejihgf"[i]] = chars1[i]
        
        for i in range(5):
            chars1[i + 5].move_to((1.2 - 0.92 / 4 * i,chars1[i + 5].get_y(),0))
            alphabets["1" + "abcdejihgf"[i + 5]] = chars1[i + 5]
        
        chars2 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,-3.5,0))
        
        for i in range(5):
            chars2[i].move_to((-1.2 + 0.92 / 4 * i,chars2[i].get_y(),0))
            alphabets["2" + "abcdejihgf"[i]] = chars2[i]
        
        for i in range(5):
            chars2[i + 5].move_to((1.2 - 0.92 / 4 * i,chars2[i + 5].get_y(),0))
            alphabets["2" + "abcdejihgf"[i + 5]] = chars2[i + 5]
        
        breadboard["alphabets"] = alphabets
        breadboard["groove"] = Rectangle(width=0.17,height=7.39,fill_opacity=1,fill_color=GREY_A,stroke_width=0).move_to((0,0,0))
        powerlabel = VDict()
        
        powerlabel["ul+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,3.52,0))
        powerlabel["ul-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,3.52,0))
        powerlabel["ur+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,3.52,0))
        powerlabel["ur-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,3.52,0))
        powerlabel["dl+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,-3.52,0))
        powerlabel["dl-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,-3.52,0))
        powerlabel["dr+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,-3.52,0))
        powerlabel["dr-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,-3.52,0))
        breadboard["powerlabel"] = powerlabel
        
        breadboard.scale(0.8).next_to(title,DOWN)
        self.add(title,icon,breadboard)
        
        rect1 = SurroundingRectangle(VGroup(breadboard["power"]["3,1"],breadboard["power"]["4,25"]),color=GREEN).set_fill(opacity=0.4)
        rect2 = SurroundingRectangle(VGroup(breadboard["power"]["1,1"],breadboard["power"]["2,25"]),color=GREEN).set_fill(opacity=0.4)
        label1 = Text("电源轨",color=GREEN,weight=BOLD).scale(0.4).next_to(rect1,RIGHT * 4)
        line1 = Line(rect1.get_right(),label1.get_left(),color=GREEN)
        labels1 = Paragraph("用于引入电源，并接地；整个竖\n列相互连接",color=GREEN).scale(0.3).next_to(label1,DOWN,aligned_edge=LEFT,buff=0.05)
        self.add(rect1,rect2,label1,labels1,line1)
        
        rect6 = SurroundingRectangle(breadboard["component"],color=GOLD).set_fill(opacity=0.4)
        label6 = Text("接线区",color=GOLD,weight=BOLD).scale(0.4).next_to(rect6,LEFT * 6)
        labels6 = Paragraph("槽两侧的同一行相互连通，而行\n与行间互不连通，用于插接元器\n件、跳线",color=GOLD,alignment="right").scale(0.3).next_to(label6,DOWN,aligned_edge=RIGHT,buff=0.05)
        line6 = Line(rect6.get_left(),label6.get_right(),color=GOLD)
        self.add(rect6,label6,labels6,line6)
        
class BreadboardConnectivity(Scene):
    def construct(self):
        title = Title("面包板内部接线")
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        breadboard = VDict()
        lines = VDict()
        
        #self.add(ImageMobject("breadboard.jpg").scale(2).shift(UP * 0.1).shift(LEFT * 0.36))
        breadboard["board"] = Rectangle(width=4.82,height=7.39,fill_opacity=1,fill_color=WHITE,stroke_width=0).move_to((0,0,0))
        lines["leftred"] = Line((-2.3,3.3,0),(-2.3,-3.3,0),color=RED)
        lines["leftblue"] = Line((-1.6,3.3,0),(-1.6,-3.3,0),color=BLUE)
        lines["rightred"] = Line((2.3,3.3,0),(2.3,-3.3,0),color=BLUE)
        lines["rightblue"] = Line((1.6,3.3,0),(1.6,-3.3,0),color=RED)
        
        breadboard["lines"] = lines
        
        font = "Arimo"
        
        power = VDict()
        
        for i in range(5):
            for j in range(5):
                for idx,k in enumerate([-2.07,-1.83,1.83,2.07]):
                    power[str([1,2,3,4][idx]) + "," + f"{i * 5 + j + 1}"] = (Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((k,3.17 - 5.45 / 4 * i - 0.23 * j,0)))
        breadboard["power"] = power
        
        numbers = VDict()
        component = VDict()
        for i in range(30):
            numbers["1," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((-1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            numbers["2," + str(i + 1)] = Text(str(i + 1),color=BLACK,font=font).scale(0.23).move_to((1.39,3.27 - 6.54 / 29 * i - 0.01,0))
            for j in range(5):
                component[chr(97 + j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((-1.22 + 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
                component[chr(106 - j) + str(i + 1)] = Rectangle(width=0.07,height=0.07,fill_opacity=1,fill_color=BLACK,stroke_width=0).move_to((1.22 - 0.92 / 4 * j,3.27 - 6.54 / 29 * i,0))
        
        breadboard["numbers"] = numbers
        breadboard["component"] = component
        
        chars1 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,3.5,0))
        
        alphabets = VDict()
        for i in range(5):
            chars1[i].move_to((-1.2 + 0.92 / 4 * i,chars1[i].get_y(),0))
            alphabets["1" + "abcdejihgf"[i]] = chars1[i]
        
        for i in range(5):
            chars1[i + 5].move_to((1.2 - 0.92 / 4 * i,chars1[i + 5].get_y(),0))
            alphabets["1" + "abcdejihgf"[i + 5]] = chars1[i + 5]
        
        chars2 = Text("abcdejihgf",color=BLACK,font=font).scale(0.25).move_to((0,-3.5,0))
        
        for i in range(5):
            chars2[i].move_to((-1.2 + 0.92 / 4 * i,chars2[i].get_y(),0))
            alphabets["2" + "abcdejihgf"[i]] = chars2[i]
        
        for i in range(5):
            chars2[i + 5].move_to((1.2 - 0.92 / 4 * i,chars2[i + 5].get_y(),0))
            alphabets["2" + "abcdejihgf"[i + 5]] = chars2[i + 5]
        
        breadboard["alphabets"] = alphabets
        breadboard["groove"] = Rectangle(width=0.17,height=7.39,fill_opacity=1,fill_color=GREY_A,stroke_width=0).move_to((0,0,0))
        powerlabel = VDict()
        
        powerlabel["ul+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,3.52,0))
        powerlabel["ul-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,3.52,0))
        powerlabel["ur+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,3.52,0))
        powerlabel["ur-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,3.52,0))
        powerlabel["dl+"] = Text("+",color=RED,font="Noto Sans Mono").scale(0.5).move_to((-2.21,-3.52,0))
        powerlabel["dl-"] = Text("-",color=BLUE,font="Noto Sans Mono").scale(0.5).stretch(1.6,dim=0).move_to((-1.69,-3.52,0))
        powerlabel["dr+"] = Text("+",color=RED,font="Consolas").scale(0.5).move_to((1.69,-3.52,0))
        powerlabel["dr-"] = Text("-",color=BLUE,font="Consolas").scale(0.5).stretch(1.6,dim=0).move_to((2.21,-3.52,0))
        breadboard["powerlabel"] = powerlabel
        
        breadboard.scale(0.8).next_to(title,DOWN)
        self.add(title,icon,breadboard)
        
        for i in range(1,5):
            self.add(Line(breadboard["power"][f"{i},1"].get_top(),breadboard["power"][f"{i},25"].get_bottom(),color=GREEN))
        for i in range(1,31):
            self.add(Line(breadboard["component"][f"a{i}"].get_left(),breadboard["component"][f"e{i}"].get_right(),color=GREEN))
            self.add(Line(breadboard["component"][f"f{i}"].get_left(),breadboard["component"][f"j{i}"].get_right(),color=GREEN))
        
class LED(Scene):
    def construct(self):
        def light(color):
            led = VGroup(
            Union(
                Circle(radius=0.4).move_to((0,0,0)),
                Rectangle(width=0.8,height=1).move_to((0,-0.5,0)),
                Rectangle(width=1,height=0.1).move_to((0,-1,0))
            ).set_fill(opacity=0.8).set_sheen_direction(UP).set_color(color=color),
            Line((-0.2,-1.05,0),(-0.2,-4.5,0)),
            Line((0.2,-1.05,0),(0.2,-4,0))
            )
            return led
        
        def radial_glow(mobject,color=YELLOW):
            glow = VGroup()
            base_radius = 0.6
            for i in range(10):
                layer = Circle(radius=base_radius + i * 0.25,stroke_width=0,fill_color=color,fill_opacity=0.08)
                glow += layer
            glow.move_to(mobject).scale(0.15)
            return glow
            
        title = Title("LED详解：重要部件")
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        led = light(["#ffaaaa","#ff0000"])
        led.scale(0.7).next_to(title,DOWN)
        self.add(title,icon,led)
        
        rect1 = SurroundingRectangle(led[2],color=TEAL).set_fill(opacity=0.4)
        label1 = Text("短引脚",color=TEAL,weight=BOLD).scale(0.4).next_to(rect1,RIGHT * 4)
        line1 = Line(rect1.get_right(),label1.get_left(),color=TEAL)
        labels1 = Paragraph("较短的引脚接负极",color=TEAL).scale(0.3).next_to(label1,DOWN,aligned_edge=LEFT,buff=0.05)
        self.add(rect1,label1,labels1,line1)
        
        rect6 = SurroundingRectangle(led[1],color=YELLOW).set_fill(opacity=0.4)
        label6 = Text("长引脚",color=YELLOW,weight=BOLD).scale(0.4).next_to(rect6,LEFT * 4)
        labels6 = Paragraph("较长的引脚接正极",color=YELLOW,alignment="right").scale(0.3).next_to(label6,DOWN,aligned_edge=RIGHT,buff=0.05)
        line6 = Line(rect6.get_left(),label6.get_right(),color=YELLOW)
        self.add(rect6,label6,labels6,line6)
        
        leds = VGroup()
        for i in [["#ff6b6b","#ff3333"],["#39ff14","#11ff07"],["#00bfff","#1f51ff"],["#fefe22","#ffd700"],["#ff10f0","#ff1493"],["#00ffff","#00f5d4"],["#ffa500","#ff5f1f"],["#ffffff","#aaaaaa"]]:
            temp = light(i).scale(0.3)
            leds += VGroup(temp,radial_glow(temp[0],i[0]))
        leds.arrange().to_edge(DOWN).shift(UP * 0.5)
        self.add(leds)
        label = Text("（感觉画面上少了点啥，就放点各种颜色的LED吧~）").scale(0.5).to_edge(DOWN)
        self.add(label)
