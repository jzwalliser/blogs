from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class ElementaryColors(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("颜料三原色和色光三原色")
        circ1 = Circle(radius=1.8,color=RED).set_fill(color=RED,opacity=1).move_to([-3.5,0.8,0])
        circ2 = Circle(radius=1.8,color=YELLOW).set_fill(color=YELLOW,opacity=1).move_to([-3.5-2/3**0.5,-1.2,0])
        circ3 = Circle(radius=1.8,color=BLUE).set_fill(color=BLUE,opacity=1).move_to([-3.5+2/3**0.5,-1.2,0])
        circ4 = Circle(radius=1.8,color="#ff0000").set_fill(color="#ff0000",opacity=1).move_to([3.5,0.8,0])
        circ5 = Circle(radius=1.8,color="#00ff00").set_fill(color="#00ff00",opacity=1).move_to([3.5-2/3**0.5,-1.2,0])
        circ6 = Circle(radius=1.8,color="#0000ff").set_fill(color="#0000ff",opacity=1).move_to([3.5+2/3**0.5,-1.2,0])
       
        paint_orange = Intersection(circ1,circ2,color=ORANGE).set_fill(color=ORANGE,opacity=1)
        paint_purple = Intersection(circ1,circ3,color=PURPLE).set_fill(color=PURPLE,opacity=1)
        paint_green = Intersection(circ3,circ2,color=GREEN).set_fill(color=GREEN,opacity=1)
        paint_black = Intersection(paint_green,paint_purple,color=BLACK).set_fill(color=BLACK,opacity=1)
        
        RGB_yellow = Intersection(circ4,circ5,color="#ffff00").set_fill(color="#ffff00",opacity=1)
        RGB_pink = Intersection(circ4,circ6,color="#ff00ff").set_fill(color="#ff00ff",opacity=1)
        RGB_cyan = Intersection(circ5,circ6,color="#00ffff").set_fill(color="#00ffff",opacity=1)
        RGB_white = Intersection(RGB_pink,RGB_yellow,color="#ffffff").set_fill(color="#ffffff",opacity=1)

        text_paint_red = Text("红").move_to(circ1.get_center()).shift(UP*0.4)
        text_paint_yellow = Text("黄",color=BLACK).move_to(circ2.get_center()).shift(DL*0.4)
        text_paint_blue = Text("蓝").move_to(circ3.get_center()).shift(DR*0.4)
        text_paint_orange = Text("橙").move_to(paint_orange.get_center()).shift(UL*0.4)
        text_paint_purple = Text("紫").move_to(paint_purple.get_center()).shift(UR*0.4)
        text_paint_green = Text("绿").move_to(paint_green.get_center()).shift(DOWN*0.4)
        text_paint_black = Text("黑").move_to(paint_black.get_center())

        RGB_paint_red = Text("红").move_to(circ4.get_center()).shift(UP*0.4)
        RGB_paint_green = Text("绿",color=BLACK).move_to(circ5.get_center()).shift(DL*0.4)
        RGB_paint_blue = Text("蓝").move_to(circ6.get_center()).shift(DR*0.4)
        RGB_paint_yellow = Text("黄",color=BLACK).move_to(RGB_yellow.get_center()).shift(UL*0.4)
        RGB_paint_pink = Text("粉").move_to(RGB_pink.get_center()).shift(UR*0.4)
        RGB_paint_cyan = Text("青",color=BLACK).move_to(RGB_cyan.get_center()).shift(DOWN*0.4)
        RGB_paint_white = Text("白",color=BLACK).move_to(RGB_white.get_center())

        text_paint = Text("颜料三原色").move_to(circ1).shift(DOWN*4.2)
        text_RGB = Text("色光三原色").move_to(circ4).shift(DOWN*4.2)

        self.add(title)
        self.add(circ1,circ2,circ3,circ4,circ5,circ6)
        self.add(paint_orange,paint_purple,paint_green,paint_black)
        self.add(RGB_cyan,RGB_yellow,RGB_pink,RGB_white)
        self.add(text_paint_red,text_paint_yellow,text_paint_blue,text_paint_orange,text_paint_purple,text_paint_green,text_paint_black)
        self.add(RGB_paint_red,RGB_paint_green,RGB_paint_blue,RGB_paint_cyan,RGB_paint_yellow,RGB_paint_pink,RGB_paint_white)
        self.add(text_paint,text_RGB,icon)
        
class RGBTuple(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("RGB 三元组")
        RGB_tuple = MathTex(r"\rm(\ \ R\ \ ,\ \ G\ \ ,\ \ B\ \ )").scale(2).next_to(title,DOWN * 2)
        RGB_tuple[0][1].color = "#ff0000"
        RGB_tuple[0][3].color = "#00ff00"
        RGB_tuple[0][5].color = "#3333ff"
        red = Text("红",color="#ff0000").scale(1.5).next_to(RGB_tuple[0][1],DOWN * 8)
        green = Text("绿",color="#00ff00").scale(1.5).next_to(RGB_tuple[0][3],DOWN * 8)
        blue = Text("蓝",color="#3333ff").scale(1.5).next_to(RGB_tuple[0][5],DOWN * 8)
        arr1 = Arrow(RGB_tuple[0][1].get_bottom(),red.get_top(),color="#ff0000")
        arr2 = Arrow(RGB_tuple[0][3].get_bottom(),green.get_top(),color="#00ff00")
        arr3 = Arrow(RGB_tuple[0][5].get_bottom(),blue.get_top(),color="#3333ff")
        colorbar = Rectangle(width=RGB_tuple.get_width(),height=1,stroke_width=0).to_edge(DOWN).shift(UP * 0.5).set_sheen_direction(RIGHT).set_fill(color=[BLACK,"#ff0000","#00ff00","#0000ff",BLACK],opacity=1)
        self.add(title,RGB_tuple,red,arr1,green,arr2,blue,arr3,icon,colorbar)

class RGBValues(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("RGB 值")
        rsquare = Rectangle(width=6,height=0.5,color="#ff0000").set_fill(color=["#ff0000",BLACK],opacity=1).shift(RIGHT + UP * 1.3)
        r0 = Text("0").move_to(rsquare.get_left()).shift(UP*0.6).scale(0.6)
        r255 = Text("255").move_to(rsquare.get_right()).shift(UP*0.6).scale(0.6)
        red = Text("Red",color="#ff4444").next_to(rsquare,LEFT).shift(LEFT)

        gsquare = Rectangle(width=6,height=0.5,color="#00ff00").set_fill(color=["#00ff00",BLACK],opacity=1).next_to(rsquare,DOWN).shift(DOWN)
        g0 = Text("0").move_to(gsquare.get_left()).shift(UP*0.6).scale(0.6)
        g255 = Text("255").move_to(gsquare.get_right()).shift(UP*0.6).scale(0.6)
        green = Text("Green",color="#44ff44").next_to(gsquare,LEFT).shift(LEFT)

        bsquare = Rectangle(width=6,height=0.5,color="#0000ff").set_fill(color=["#0000ff",BLACK],opacity=1).next_to(gsquare,DOWN).shift(DOWN)
        b0 = Text("0").move_to(bsquare.get_left()).shift(UP*0.6).scale(0.6)
        b255 = Text("255").move_to(bsquare.get_right()).shift(UP*0.6).scale(0.6)
        blue = Text("Blue",color="#4444ff").next_to(bsquare,LEFT).shift(LEFT)
        self.add(title,rsquare,r0,r255,red,gsquare,g0,g255,green,bsquare,b0,b255,blue,icon)

class CommonRGB(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("一些常见颜色")
        hex_colors = [('#FF3333', '信号红'), ('#FF6B6B', '珊瑚色'), ('#FF8C00', '深橙色'), ('#FFA500', '橙色'), ('#FFD700', '金色'), ('#FFFF66', '浅黄色'), ('#CCFF00', '酸橙色'), ('#39FF14', '霓虹绿'), ('#00FF00', '酸橙'), ('#00FF7F', '中春绿'), ('#40E0D0', '绿松石'), ('#00F5D4', '薄荷绿'), ('#00BFFF', '深天蓝'), ('#1F51FF', '电蓝'), ('#00FFFF', '青色'), ('#0047AB', '钴色'), ('#BF00FF', '电紫'), ('#FF10F0', '霓虹粉'), ('#FF1493', '深粉色'), ('#FF69B4', '热粉'), ('#FEFE22', '激光黄'), ('#FF5F1F', '安全橙'), ('#FFDA03', '向日葵'), ('#7DF9FF', '冰蓝')]
        rgb_colors = [((255, 51, 51), '信号红'), ((255, 107, 107), '珊瑚色'), ((255, 140, 0), '深橙色'), ((255, 165, 0), '橙色'), ((255, 215, 0), '金色'), ((255, 255, 102), '浅黄色'), ((204, 255, 0), '酸橙色'), ((57, 255, 20), '霓虹绿'), ((0, 255, 0), '酸橙'), ((0, 255, 127), '中春绿'), ((64, 224, 208), '绿松石'), ((0, 245, 212), '薄荷绿'), ((0, 191, 255), '深天蓝'), ((31, 81, 255), '电蓝'), ((0, 255, 255), '青色'), ((0, 71, 171), '钴色'), ((191, 0, 255), '电紫'), ((255, 16, 240), '霓虹粉'), ((255, 20, 147), '深粉色'), ((255, 105, 180), '热粉'), ((254, 254, 34), '激光黄'), ((255, 95, 31), '安全橙'), ((255, 218, 3), '向日葵'), ((125, 249, 255), '冰蓝')]
        colors = VGroup()
        for index,i in enumerate(hex_colors):
            rect = Rectangle(width=3,height=0.62,color=i[0]).set_fill(color=i[0],opacity=0.5)
            rectcol = Rectangle(width=3,height=0.62,color=i[0]).set_fill(color=i[0],opacity=1).move_to(rect.get_center()).scale(0.8)
            rgb = rgb_colors[index][0]
            
            if rgb[0] + rgb[1] + rgb[2] > 382.5 or rgb[1] > 200:
                textcolor = BLACK
            else:
                textcolor = WHITE
            colorname = Text(i[1] + " (" + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + ")",color=textcolor).move_to(rect.get_center()).scale(0.4)
            color = VGroup(rect,rectcol,colorname)
            colors += color
        colors.arrange_in_grid(cols=4,buff=0.3).next_to(title,DOWN)
        self.add(title,colors,icon)

class CommonHEX(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("一些常见颜色的HEX格式")
        hex_colors = [('#FF3333', '信号红'), ('#FF6B6B', '珊瑚色'), ('#FF8C00', '深橙色'), ('#FFA500', '橙色'), ('#FFD700', '金色'), ('#FFFF66', '浅黄色'), ('#CCFF00', '酸橙色'), ('#39FF14', '霓虹绿'), ('#00FF00', '酸橙'), ('#00FF7F', '中春绿'), ('#40E0D0', '绿松石'), ('#00F5D4', '薄荷绿'), ('#00BFFF', '深天蓝'), ('#1F51FF', '电蓝'), ('#00FFFF', '青色'), ('#0047AB', '钴色'), ('#BF00FF', '电紫'), ('#FF10F0', '霓虹粉'), ('#FF1493', '深粉色'), ('#FF69B4', '热粉'), ('#FEFE22', '激光黄'), ('#FF5F1F', '安全橙'), ('#FFDA03', '向日葵'), ('#7DF9FF', '冰蓝')]
        rgb_colors = [((255, 51, 51), '信号红'), ((255, 107, 107), '珊瑚色'), ((255, 140, 0), '深橙色'), ((255, 165, 0), '橙色'), ((255, 215, 0), '金色'), ((255, 255, 102), '浅黄色'), ((204, 255, 0), '酸橙色'), ((57, 255, 20), '霓虹绿'), ((0, 255, 0), '酸橙'), ((0, 255, 127), '中春绿'), ((64, 224, 208), '绿松石'), ((0, 245, 212), '薄荷绿'), ((0, 191, 255), '深天蓝'), ((31, 81, 255), '电蓝'), ((0, 255, 255), '青色'), ((0, 71, 171), '钴色'), ((191, 0, 255), '电紫'), ((255, 16, 240), '霓虹粉'), ((255, 20, 147), '深粉色'), ((255, 105, 180), '热粉'), ((254, 254, 34), '激光黄'), ((255, 95, 31), '安全橙'), ((255, 218, 3), '向日葵'), ((125, 249, 255), '冰蓝')]
        colors = VGroup()
        for index,i in enumerate(hex_colors):
            rect = Rectangle(width=3,height=0.62,color=i[0]).set_fill(color=i[0],opacity=0.5)
            rectcol = Rectangle(width=3,height=0.62,color=i[0]).set_fill(color=i[0],opacity=1).move_to(rect.get_center()).scale(0.8)
            rgb = rgb_colors[index][0]
            
            if rgb[0] + rgb[1] + rgb[2] > 382.5 or rgb[1] > 200:
                textcolor = BLACK
            else:
                textcolor = WHITE
            colorname = Text(i[1] + " " + i[0],color=textcolor).move_to(rect.get_center()).scale(0.4)
            color = VGroup(rect,rectcol,colorname)
            colors += color
        colors.arrange_in_grid(cols=4,buff=0.3).next_to(title,DOWN)
        self.add(title,colors,icon)

class HEXConvert(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("HEX格式的转化")
        rect = Rectangle(width=8,height=2,color="#ff69b4").set_fill(color="#ff69b4",opacity=0.5).next_to(title,DOWN).shift(LEFT*0.36)
        rectcol = Rectangle(width=8,height=2,color="#ff69b4").set_fill(color="#ff69b4",opacity=1).move_to(rect.get_center()).scale(0.8)
        colortext = Text("#FF69B4").move_to(rect.get_center()).scale(2)
      
        redsquare = Rectangle(width=3,height=1,color="#ff0000").set_fill(color="#ff0000",opacity=0.5)
        reddec = MathTex(r"\rm (FF)_{16}=255").move_to(redsquare.center())
        redcalc = VGroup(redsquare,reddec).to_edge(LEFT).shift(RIGHT * 1.5 + DOWN)
      
        greensquare = Rectangle(width=3,height=1,color="#00ff00").set_fill(color="#00ff00",opacity=0.5)
        greendec = MathTex(r"\rm (69)_{16}=105").move_to(greensquare.center())
        greencalc = VGroup(greensquare,greendec).shift(DOWN)

        bluesquare = Rectangle(width=3,height=1,color="#0000ff").set_fill(color="#0000ff",opacity=0.5)
        bluedec = MathTex(r"\rm (B4)_{16}=180").move_to(bluesquare.center())
        bluecalc = VGroup(bluesquare,bluedec).to_edge(RIGHT).shift(LEFT * 1.5 + DOWN)

        arrred = Arrow(colortext[1:3].get_bottom(),redsquare.get_top(),color="#ff4444")
        arrgreen = Arrow(colortext[3:5].get_bottom(),greensquare.get_top(),color="#44ff44")
        arrblue = Arrow(colortext[5:7].get_bottom(),bluesquare.get_top(),color="#4444ff")

        calcgroup = VGroup(redcalc,greencalc,bluecalc)
        brace = Brace(calcgroup,sharpness=1)

        rgbcolor = Text("(255,105,180)",color="#ff69b4").next_to(brace,DOWN)
        self.add(title,rect,rectcol,colortext,calcgroup,arrred,arrgreen,arrblue,brace,rgbcolor,icon)
        
class RGBA(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("RGBA")
        group = VGroup()
        transcolor = ["#e4e4e4","#ffffff"]
        for i in range(40):
            for j in range(40):
                rect = Rectangle(width=0.15,height=0.15,color=transcolor[(i + j) % 2]).set_fill(color=transcolor[(i + j) % 2],opacity=1).move_to([i*0.15,j*0.15,0])
                group += rect
        group.next_to(title,DOWN).shift(RIGHT)
        rainbow = VGroup()
        color = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff","#ff00ff","#ffffff"]
        for i in range(7):
            rect = Rectangle(width=0.857142,height=6,stroke_width=0).set_sheen_direction(UP).set_fill(color=color[i],opacity=[0,1]).move_to([i * 0.857142,0,0])
            rainbow += rect
        rainbow.move_to(group.get_center())
        opaque = MathTex(r"\rm A=1").next_to(group.get_left(),LEFT).shift(UP*2.7)
        translucent = MathTex(r"\rm A=0.5").next_to(group.get_left(),LEFT)
        transparent = MathTex(r"\rm A=0").next_to(group.get_left(),LEFT).shift(DOWN*2.7)
        self.add(title,group,rainbow,opaque,translucent,transparent,icon)
