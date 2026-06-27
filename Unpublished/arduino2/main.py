from manim import *
from manimplugs import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)


        
class Circuit(Scene):
    def construct(self):        
        board = VGroup()
    
        boardcolor = "#007773"
        block = Polygon([-4.5,3.93,0],[-4.5,-3.93,0],[5.23,-3.93,0],[5.28,-3.6,0],[5.56,-3.27,0],[5.62,-3.09,0],[5.62,1.68,0],[5.28,2.07,0],[5.28,3.77,0],[5.1,3.93,0],stroke_width=0,fill_opacity=0.9).set_color(color=boardcolor)
        board += block
        
        resetbutton = VGroup(
            Rectangle(width=0.87,height=0.87,fill_opacity=1).set_color(color=WHITE).move_to((-3.61,3.45,0)),
            Circle(radius=0.22,fill_opacity=1).set_color(color=YELLOW_B).move_to((-3.61,3.45,0)),
            Rectangle(width=0.23,height=0.23,fill_opacity=1).move_to((-4.2,3.09,0)),
            Rectangle(width=0.23,height=0.23,fill_opacity=1).move_to((-4.2,3.41,0)),
            Rectangle(width=0.23,height=0.23,fill_opacity=1).move_to((-4.2,3.73,0)),
            Rectangle(width=0.32,height=0.24,fill_opacity=1).move_to((-2.97,3.73,0)),
            Rectangle(width=0.32,height=0.24,fill_opacity=1).move_to((-2.99,3.09,0)),
            Text("RESET",font="Consolas").rotate(PI / 2).move_to((-4.43,3.4,0)).scale(0.33)
        )
        board += resetbutton
        
        power = Rectangle(width=2.39,height=1.77,fill_opacity=1,color=WHITE).move_to((-4.43,1.8,0))
        board += power
        
        
        part1 = VGroup(
            Rectangle(width=0.46,height=0.74,color=BLACK,fill_opacity=1).move_to((-3.95,0,0)),
            Rectangle(width=0.43,height=0.14,color=GOLD,fill_opacity=1).move_to((-3.95,0.25,0)),
            Rectangle(width=0.43,height=0.14,color=GOLD,fill_opacity=1).move_to((-3.95,-0.25,0)),
            MathTex(r"\infty",color=GOLD).scale(0.8).move_to((-3.95,0,0))
            )
        board += part1
        
        part2 = VGroup(
            Rectangle(width=0.49,height=0.9,color=BLACK,fill_opacity=1).move_to((-3.38,-1.36,0)),
            Rectangle(width=0.36,height=0.17,fill_opacity=1).move_to((-2.94,-1.01,0)),
            Rectangle(width=0.36,height=0.17,fill_opacity=1).move_to((-2.94,-1.36,0)),
            Rectangle(width=0.36,height=0.17,fill_opacity=1).move_to((-2.94,-1.71,0)),
            Rectangle(width=0.35,height=0.56,fill_opacity=1).move_to((-3.83,-1.36,0)))
        board += part2
        
        battery = VGroup(
            Rectangle(width=0.51,height=1.31,color=GREY,fill_opacity=1).move_to((-4.67,-2.74,0)),
            Rectangle(width=1.54,height=1.25,stroke_width=0).move_to((-3.64,-2.74,0)
        ).set_sheen_direction(DOWN).set_fill(color=[BLACK,WHITE,BLACK],opacity=1))
        board += battery
        
        rightpins = VGroup(
            Rectangle(width=7.20,height=0.36,color=GREY,fill_opacity=1).move_to((1.59,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-1.8,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-1.41,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-1.02,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-0.64,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-0.25,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0.14,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0.53,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0.91,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((1.3,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((1.69,3.69,0)),
            
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((2.3,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((2.68,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.07,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.45,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.84,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((4.22,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((4.6,3.69,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((4.99,3.69,0)),
            
            Rectangle(width=0.35,height=0.64,fill_opacity=1).move_to((-0.62,3.1,0)),
            Text("AREF",font="Consolas").rotate(PI / 2).move_to((-0.99,2.95,0)).scale(0.4),
            Text("GND",font="Consolas",color=boardcolor).rotate(PI / 2).move_to((-0.61,3.04,0)).scale(0.41),
            Text("13",font="Consolas").rotate(PI / 2).move_to((-0.22,3.09,0)).scale(0.52),
            Text("12",font="Consolas").rotate(PI / 2).move_to((0.15,3.09,0)).scale(0.52),
            Text("~11",font="Consolas").rotate(PI / 2).move_to((0.53,3,0)).scale(0.52),
            Text("~10",font="Consolas").rotate(PI / 2).move_to((0.90,3,0)).scale(0.52),
            Text("~9",font="Consolas").rotate(PI / 2).move_to((1.28,3.09,0)).scale(0.52),
            Text("8",font="Consolas").rotate(PI / 2).move_to((1.66,3.2,0)).scale(0.52),
            Text("7",font="Consolas").rotate(PI / 2).move_to((2.28,3.2,0)).scale(0.52),
            Text("~6",font="Consolas").rotate(PI / 2).move_to((2.65,3.09,0)).scale(0.52),
            Text("~5",font="Consolas").rotate(PI / 2).move_to((3.03,3.09,0)).scale(0.52),
            Text("4",font="Consolas").rotate(PI / 2).move_to((3.41,3.2,0)).scale(0.52),
            Text("~3",font="Consolas").rotate(PI / 2).move_to((3.78,3.09,0)).scale(0.52),
            Text("2",font="Consolas").rotate(PI / 2).move_to((4.16,3.2,0)).scale(0.52),
            Text("TX→1",font="Consolas").rotate(PI / 2).move_to((4.53,2.9,0)).scale(0.52),
            Text("RX←0",font="Consolas").rotate(PI / 2).move_to((4.92,2.9,0)).scale(0.52)
        )
        board += rightpins
        
        part3 = VGroup(
            RoundedRectangle(width=0.34,height=0.7,corner_radius=0.1,color=BLACK,fill_opacity=1).move_to((-2.18,2.94,0)),
            RoundedRectangle(width=0.34,height=0.7,corner_radius=0.1,color=BLACK,fill_opacity=1).move_to((-1.81,2.94,0)),
            RoundedRectangle(width=0.34,height=0.7,corner_radius=0.1,color=BLACK,fill_opacity=1).move_to((-1.44,2.94,0)),
            
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-2.18,3.13,0)),
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-2.18,2.75,0)),
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-1.81,3.13,0)),
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-1.81,2.75,0)),
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-1.44,3.13,0)),
            Rectangle(width=0.05,height=0.05,fill_opacity=1).move_to((-1.44,2.75,0))
        )
        board += part3
        
        part4 = VGroup(
            DashedVMobject(Rectangle(width=0.75,height=0.73).move_to((-1.63,2.16,0)),num_dashes=50,dashed_ratio=0.4),
            Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to((-1.81,2.37,0)),
            Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to((-1.81,1.99,0)),
            Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to((-1.43,2.37,0)),
            Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to((-1.43,1.99,0)),
            Text("JP2",font="Consolas").scale(0.32).rotate(PI / 2).move_to((-2.13,1.93,0))
        )
        board += part4
        
        digitalpwmlabel = VGroup(
            Rectangle(width=2.56,height=0.21,fill_opacity=1).move_to((0.93,2.57,0)),
            Text("DIGITAL",font="Consolas",weight=BOLD,color=boardcolor).scale(0.35).move_to((0.47,2.57,0)).stretch(1.35,dim=0),
            Text("-",font="Consolas",weight=BOLD,color=boardcolor).scale(0.35).move_to((1.28,2.57,0)),
            Text("PWM~",font="Consolas",color=boardcolor).scale(0.35).move_to((1.84,2.57,0)).stretch(1.35,dim=0),
            Line((-0.33,2.46,0),(4.99,2.46,0))
        )
        board += digitalpwmlabel
        
        part5 = VGroup(
            Rectangle(width=0.36,height=0.14,color=BLACK,fill_opacity=1).move_to((-0.37,2.67,0)),
            Rectangle(width=0.2,height=0.1,fill_opacity=1).move_to((-0.37,2.67,0))
        )
        board += part5
        
        builtin_led = VGroup(
            Rectangle(width=0.44,height=0.16,fill_opacity=1).move_to((-0.37,2.33,0)),
            Rectangle(width=0.14,height=0.14,color=YELLOW,fill_opacity=1).move_to((-0.37,2.33,0)),
            Text("L",font="Consolas").move_to((-0.77,2.32,0)).scale(0.40)
        )
        board += builtin_led
        
        part6 = VGroup(
            Rectangle(width=0.2,height=0.47,color=BLACK,fill_opacity=1).move_to((-0.37,1.91,0)),
            Text("102").scale(0.2).rotate(-PI / 2).move_to((-0.37,1.91,0))
        )
        board += part6
        
        tx_led = VGroup(
            Rectangle(width=0.44,height=0.16,fill_opacity=1).move_to((-0.37,1.5,0)),
            Rectangle(width=0.14,height=0.14,color=YELLOW,fill_opacity=1).move_to((-0.37,1.5,0)),
            Text("TX",font="Consolas").move_to((-0.85,1.48,0)).scale(0.40)
        )
        board += tx_led
        
        rx_led = VGroup(
            Rectangle(width=0.44,height=0.16,fill_opacity=1).move_to((-0.37,1.17,0)),
            Rectangle(width=0.14,height=0.14,color=YELLOW,fill_opacity=1).move_to((-0.37,1.17,0)),
            Text("RX",font="Consolas").move_to((-0.85,1.15,0)).scale(0.40)
        )
        board += rx_led
        
        part7 = Rectangle(width=0.36,height=0.13,fill_opacity=1).move_to((-0.37,0.73,0))
        board += part7
        
        part8 = Rectangle(width=0.36,height=0.13,fill_opacity=1).move_to((-0.37,0.47,0))
        board += part8
        
        part9 = VGroup(
            DashedVMobject(Rectangle(width=0.51,height=0.35).move_to((-0.38,0.11,0)),num_dashes=30,dashed_ratio=0.4),
            Rectangle(width=0.14,height=0.21,fill_opacity=1).move_to((-0.49,0.12,0)),
            Rectangle(width=0.14,height=0.21,fill_opacity=1).move_to((-0.26,0.12,0)),
            Text("EN",font="Consolas").rotate(PI / 2).move_to((-0.76,0.19,0)).scale(0.32),
            Text("RST",font="Consolas").rotate(PI / 2).move_to((-0.76,-0.22,0)).scale(0.32)
        )
        board += part9
        
        part10 = VGroup(
            Rectangle(width=0.2,height=0.47,color=BLACK,fill_opacity=1).move_to((-0.37,-0.39,0)),
            Text("103").scale(0.2).rotate(-PI / 2).move_to((-0.37,-0.39,0))
        )
        board += part10
        
        part11 = VGroup(
            Rectangle(width=0.23,height=0.67,fill_opacity=1).move_to((-2.57,2.92,0)),
            Rectangle(width=0.23,height=0.4,color=BLACK,fill_opacity=1).move_to((-2.57,2.92,0))
        )
        board += part11
        
        part12 = Rectangle(width=0.19,height=0.09,fill_opacity=1).move_to((-2.66,2.32,0))
        board += part12
        
        part13 = VGroup(
            Rectangle(width=0.21,height=0.11,fill_opacity=1).move_to((-2.64,1.91,0)),
            Rectangle(width=0.14,height=0.09,fill_opacity=1,color=BLACK).move_to((-2.64,1.91,0))
        )
        board += part13
        
        part14 = VGroup(
            Rectangle(width=0.2,height=0.47,color=BLACK,fill_opacity=1).move_to((-2.62,1.52,0)),
            Text("220",fill_opacity=1).scale(0.2).rotate(-PI / 2).move_to((-2.62,1.52,0))
        )
        board += part14
        
        part15 = VGroup(
            Rectangle(width=0.21,height=0.11).move_to((-2.66,1.06,0)),
            Rectangle(width=0.14,height=0.09,fill_opacity=1,color=BLACK).move_to((-2.66,1.06,0))
        )
        board += part15
        
        part16 = Rectangle(width=0.21,height=0.1,fill_opacity=1).move_to((-2.75,0.5,0))
        board += part16
        
        part17 = VGroup(
            Rectangle(width=0.21,height=0.1,fill_opacity=1).move_to((-2.15,0.47,0)),
            Rectangle(width=0.21,height=0.1,fill_opacity=1).move_to((-1.24,0.47,0)),
            Rectangle(width=0.1,height=0.1,fill_opacity=1).move_to((-1.81,0.44,0)),
            Rectangle(width=0.1,height=0.1,fill_opacity=1).move_to((-1.57,0.44,0))
        )
        board += part17
        
        part18 = VGroup(
            RoundedRectangle(width=1.59,height=0.61,corner_radius=0.3,fill_opacity=1).move_to((-1.7,-0.06,0)),
            Text("T16.000",color=GREY).rotate(PI).move_to((-1.7,-0.06,0)).scale(0.35)
        )
        board += part18
        
        part19 = VGroup(
            Rectangle(width=0.73,height=0.73,fill_opacity=1,color=BLACK).move_to((-1.56,1.21,0)),
            Line((-1.83,1.59,0),(-1.83,1.66,0),stroke_width=2),
            Line((-1.75,1.59,0),(-1.75,1.66,0),stroke_width=2),
            Line((-1.68,1.59,0),(-1.68,1.66,0),stroke_width=2),
            Line((-1.6,1.59,0),(-1.6,1.66,0),stroke_width=2),
            Line((-1.53,1.59,0),(-1.53,1.66,0),stroke_width=2),
            Line((-1.45,1.59,0),(-1.45,1.66,0),stroke_width=2),
            Line((-1.38,1.59,0),(-1.38,1.66,0),stroke_width=2),
            Line((-1.3,1.59,0),(-1.3,1.66,0),stroke_width=2),
            
            Line((-1.83,0.83,0),(-1.83,0.76,0),stroke_width=2),
            Line((-1.75,0.83,0),(-1.75,0.76,0),stroke_width=2),
            Line((-1.68,0.83,0),(-1.68,0.76,0),stroke_width=2),
            Line((-1.6,0.83,0),(-1.6,0.76,0),stroke_width=2),
            Line((-1.53,0.83,0),(-1.53,0.76,0),stroke_width=2),
            Line((-1.45,0.83,0),(-1.45,0.76,0),stroke_width=2),
            Line((-1.38,0.83,0),(-1.38,0.76,0),stroke_width=2),
            Line((-1.3,0.83,0),(-1.3,0.76,0),stroke_width=2),
            
            Line((-1.94,1.48,0),(-2.01,1.48,0),stroke_width=2),
            Line((-1.94,1.4,0),(-2.01,1.4,0),stroke_width=2),
            Line((-1.94,1.33,0),(-2.01,1.33,0),stroke_width=2),
            Line((-1.94,1.25,0),(-2.01,1.25,0),stroke_width=2),
            Line((-1.94,1.18,0),(-2.01,1.18,0),stroke_width=2),
            Line((-1.94,1.10,0),(-2.01,1.10,0),stroke_width=2),
            Line((-1.94,1.02,0),(-2.01,1.02,0),stroke_width=2),
            Line((-1.94,0.95,0),(-2.01,0.95,0),stroke_width=2),
            
            Line((-1.18,1.48,0),(-1.11,1.48,0),stroke_width=2),
            Line((-1.18,1.4,0),(-1.11,1.4,0),stroke_width=2),
            Line((-1.18,1.33,0),(-1.11,1.33,0),stroke_width=2),
            Line((-1.18,1.25,0),(-1.11,1.25,0),stroke_width=2),
            Line((-1.18,1.18,0),(-1.11,1.18,0),stroke_width=2),
            Line((-1.18,1.10,0),(-1.11,1.10,0),stroke_width=2),
            Line((-1.18,1.02,0),(-1.11,1.02,0),stroke_width=2),
            Line((-1.18,0.95,0),(-1.11,0.95,0),stroke_width=2)
        )
        board += part19
        
        part20 = VGroup(
            Rectangle(width=0.38,height=0.38,fill_opacity=1,color=BLACK).move_to((-1.7,-0.94,0)),
            
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-2.01,-0.79,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-2.01,-0.88,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-2.01,-0.97,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-2.01,-1.07,0)),
            
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-1.39,-0.79,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-1.39,-0.88,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-1.39,-0.97,0)),
            Rectangle(width=0.16,height=0.01,fill_opacity=1).move_to((-1.39,-1.07,0))
        )
        board += part20
        
        part21 = VGroup(
            Rectangle(width=0.1,height=0.1,fill_opacity=1).move_to((-3.48,0,0)),
            Rectangle(width=0.13,height=0.13,fill_opacity=1).move_to((-3.17,0.14,0)),
            Rectangle(width=0.13,height=0.13,fill_opacity=1).move_to((-3.17,-0.14,0)),
            Rectangle(width=0.14,height=0.41,fill_opacity=1,color=BLACK).move_to((-3.34,0,0)),
            
        )
        board += part21
        
        part22 = Rectangle(width=0.1,height=0.2,fill_opacity=1).move_to((-1.78,-1.66,0))
        board += part22
        
        part23 = Rectangle(width=0.1,height=0.2,fill_opacity=1).move_to((-0.73,-1.66,0))
        board += part23
        
        part24 = VGroup(
            Rectangle(width=0.18,height=0.39,fill_opacity=1,color=BLACK).move_to((-1.28,-1.68,0)),
            
            Rectangle(width=0.12,height=0.06,fill_opacity=1).move_to((-1.47,-1.54,0)),
            Rectangle(width=0.12,height=0.06,fill_opacity=1).move_to((-1.47,-1.69,0)),
            Rectangle(width=0.12,height=0.06,fill_opacity=1).move_to((-1.47,-1.83,0)),
            
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((-1.06,-1.53,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((-1.06,-1.82,0))
        )
        board += part24
        
        part25 = VGroup(
            Rectangle(width=1,height=0.33,fill_opacity=1).move_to((-1.32,-3.54,0)),
            Rectangle(width=0.5,height=0.33,fill_opacity=1,color=BLACK).move_to((-1.32,-3.54,0))
        )
        board += part25
        
        part26 = VGroup(
            Circle(radius=0.45,fill_opacity=1,color=WHITE).move_to((-1.8,-2.62,0)),
            Circle(radius=0.45,fill_opacity=1,color=WHITE).move_to((-0.75,-2.62,0)),
            
            Intersection(Circle(radius=0.45).move_to((-1.8,-2.62,0)),Rectangle(width=0.9,height=0.26).move_to((-1.8,-2.96,0)),color=BLACK,fill_opacity=1),
            Intersection(Circle(radius=0.45).move_to((-0.75,-2.62,0)),Rectangle(width=0.9,height=0.26).move_to((-0.75,-2.96,0)),color=BLACK,fill_opacity=1),
            
            Text("CS",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-1.99,-2.65,0)),
            Text("47",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-1.78,-2.65,0)),
            Text("25V",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-1.57,-2.56,0)),
            
            Text("CS",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-0.94,-2.65,0)),
            Text("47",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-0.73,-2.65,0)),
            Text("25V",font="Noto Sans Mono",color=BLACK).scale(0.35).rotate(PI / 2).move_to((-0.52,-2.56,0))
        )
        board += part26
        
        cpu = VGroup(
            Rectangle(width=5.28,height=1.45,color=BLACK,fill_opacity=1).move_to((2.39,-1.55,0)),
            Rectangle(width=5.28,height=1.05,color="#444444",fill_opacity=1).move_to((2.39,-1.55,0)),
            
            Rectangle(width=0.15,height=0.06,fill_opacity=1).move_to((-0.1,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((0.26,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((0.65,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.03,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.41,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.79,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.18,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.55,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.94,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((3.32,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((3.7,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((4.08,-0.96,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((4.47,-0.96,0)),
            Rectangle(width=0.15,height=0.06,fill_opacity=1).move_to((4.81,-0.96,0)),
            
            Rectangle(width=0.15,height=0.06,fill_opacity=1).move_to((-0.1,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((0.26,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((0.65,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.03,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.41,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((1.79,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.18,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.55,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((2.94,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((3.32,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((3.7,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((4.08,-2.14,0)),
            Rectangle(width=0.18,height=0.06,fill_opacity=1).move_to((4.47,-2.14,0)),
            Rectangle(width=0.15,height=0.06,fill_opacity=1).move_to((4.81,-2.14,0))

        )
        board += cpu
        
        part27 = VGroup(
            Rectangle(width=0.47,height=0.16,fill_opacity=1,color=GREY).move_to((1.61,-0.25,0)),
            Rectangle(width=0.08,height=0.11,fill_opacity=1).move_to((1.49,-0.54,0)),
            Rectangle(width=0.08,height=0.11,fill_opacity=1).move_to((1.72,-0.54,0))
        )
        board += part27
        
        part28 = Rectangle(width=0.19,height=0.1,fill_opacity=1).move_to((2.28,-0.55,0))
        board += part28
        
        part29 = VGroup(
            Rectangle(width=0.22,height=0.66,fill_opacity=1).move_to((4.32,0.21,0)),
            Rectangle(width=0.22,height=0.4,color=BLACK,fill_opacity=1).move_to((4.32,0.21,0))
        )
        board += part29
        
        part30 = VGroup(
            Rectangle(width=0.2,height=0.47,color=BLACK,fill_opacity=1).move_to((4.17,1.08,0)),
            Text("102").scale(0.2).rotate(-PI / 2).move_to((4.17,1.08,0))
        )
        board += part30
        
        on_led = VGroup(
            Rectangle(width=0.44,height=0.16,fill_opacity=1).move_to((4.17,1.5,0)),
            Rectangle(width=0.14,height=0.14,color=YELLOW,fill_opacity=1).move_to((4.17,1.5,0)),
            Text("ON",font="Consolas").move_to((4.6,1.5,0)).scale(0.40)
        )
        board += on_led
        
        leftpins = VGroup(
            Rectangle(width=0.7,height=0.91,fill_opacity=1).move_to((1.7,-3.45,0)),
            Rectangle(width=5.81,height=0.36,fill_opacity=1,color=GREY).move_to((2.31,-3.62,0)),
            
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((-0.39,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0.39,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((0.77,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((1.16,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((1.55,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((1.94,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((2.32,-3.62,0)),
            
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.08,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.47,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((3.86,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((4.24,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((4.63,-3.62,0)),
            Rectangle(width=0.21,height=0.21,color=BLACK,fill_opacity=1).move_to((5.02,-3.62,0)),
            
            Text("IOREF",font="Consolas").rotate(PI / 2).move_to((0,-2.95,0)).scale(0.38),
            Text("RESET",font="Consolas").rotate(PI / 2).move_to((0.39,-2.95,0)).scale(0.38),
            Text("3",font="Consolas").rotate(PI / 2).move_to((0.77,-3.22,0)).scale(0.38),
            Text(".",font="Consolas").rotate(PI / 2).move_to((0.81,-3.14,0)).scale(0.38),
            Text("3V",font="Consolas").rotate(PI / 2).move_to((0.77,-2.98,0)).scale(0.38),
            Text("5V",font="Consolas").rotate(PI / 2).move_to((1.14,-3.15,0)).scale(0.38),
            Text("GND",font="Consolas",color=boardcolor).move_to((1.7,-3.13,0)).scale(0.34),
            Text("Vin",font="Consolas").rotate(PI / 2).move_to((2.27,-3.1,0)).scale(0.38),
            Text("A0",font="Consolas").rotate(PI / 2).move_to((3.02,-3.1,0)).scale(0.52),
            Text("A1",font="Consolas").rotate(PI / 2).move_to((3.41,-3.1,0)).scale(0.52),
            Text("A2",font="Consolas").rotate(PI / 2).move_to((3.79,-3.1,0)).scale(0.52),
            Text("A3",font="Consolas").rotate(PI / 2).move_to((4.17,-3.1,0)).scale(0.52),
            Text("A4",font="Consolas").rotate(PI / 2).move_to((4.55,-3.1,0)).scale(0.52),
            Text("A5",font="Consolas").rotate(PI / 2).move_to((4.93,-3.1,0)).scale(0.52)
            
        )
        board += leftpins
        
        powerlabel = VGroup(
            Rectangle(width=0.87,height=0.21,fill_opacity=1).move_to((2.02,-2.69,0)),
            Text("POWER",font="Consolas",weight=BOLD,color=boardcolor).scale(0.35).move_to((2.02,-2.68,0)).stretch(1.31,dim=0),
            Line((0.59,-2.57,0),(2.47,-2.57,0))
        )
        board += powerlabel
        
        analoglabel = VGroup(
            Rectangle(width=1.45,height=0.21,fill_opacity=1).move_to((3.56,-2.69,0)),
            Text("ANALOG",font="Consolas",weight=BOLD,color=boardcolor).scale(0.35).move_to((3.33,-2.68,0)).stretch(1.31,dim=0),
            Text("IN",font="Consolas",weight=BOLD,color=boardcolor).scale(0.35).move_to((4.1,-2.68,0)).stretch(1.31,dim=0),
            Line((2.82,-2.57,0),(5,-2.57,0))
        )
        board += analoglabel
        
        part31 = VGroup(
            part3.copy().rotate(PI / 2).move_to((5.15,0.2,0)),
            Text("ICSP",font="Consolas").scale(0.3).move_to((5.24,0.87,0))
        )
        board += part31
        
        unor3label = VGroup(
            Rectangle(width=1.97,height=0.53).move_to((1.23,0.32,0)),
            Rectangle(width=1.15,height=0.53,fill_opacity=1).move_to((0.82,0.32,0)),
            Text("UNO",font="Noto Sans Mono",color=boardcolor).scale(0.52).move_to((0.84,0.32,0)).stretch(1.31,dim=0),
            Text("R3",font="Noto Sans Mono").scale(0.52).move_to((1.82,0.32,0)).stretch(1.31,dim=0),
        )
        board += unor3label
        
        arduinocclabel = Text("ARDUINO.CC",font="Consolas").scale(0.3).move_to((3.48,-0.35,0)).stretch(1.14,dim=0)
        board += arduinocclabel
        
        arduinolabel = VGroup(
            Text("∞",font="Noto Sans Mono").scale(4.2).move_to((1.24,1.73,0)).stretch(1.14,dim=0),
            Text("-",font="Noto Sans Mono").scale(1.4).move_to((0.79,1.73,0)),
            Text("+",font="Noto Sans Mono",weight=BOLD).move_to((1.69,1.73,0)),
            Text("®",font="Noto Sans Mono",weight=BOLD).scale(0.78).move_to((2.22,2.16,0)),
            Text("ARDUINO",font="Noto Sans Mono",weight=BOLD).scale(0.55).move_to((1.25,1.02,0)).stretch(1.14,dim=0),
        )
        board += arduinolabel
        
        d = {'A': (-4.2, -3.15, 0), 'B': (8.18, -3.15, 0), 'C': (0.44, -1.13, 0), 'D': (0.44, -1.2, 0), 'E': (0.22, -1.2, 0), 'F': (0.44, -0.82, 0), 'G': (0.6, -0.82, 0), 'H': (0.6, -1.2, 0), 'I': (0.5, -1.2, 0), 'J': (0.5, -0.92, 0), 'K': (0.38, -1.13, 0), 'L': (0.47, -0.75, 0), 'M': (0.54, -0.65, 0), 'N': (0.65, -0.75, 0), 'O': (0.65, -1.2, 0), 'P': (0.76, -1.2, 0), 'Q': (0.76, -0.75, 0), 'R': (1.93, -0.65, 0), 'S': (1.93, -0.75, 0), 'T': (0.83, -1.2, 0), 'U': (0.9, -1.2, 0), 'V': (0.83, -0.82, 0), 'W': (1.21, -0.82, 0), 'Z': (1.25, -0.86, 0), 'A1': (0.9, -0.92, 0), 'B1': (0.99, -0.92, 0), 'C1': (0.99, -1.2, 0), 'D1': (1.08, -1.2, 0), 'E1': (1.08, -0.92, 0), 'F1': (1.16, -0.92, 0), 'G1': (1.16, -1.2, 0), 'H1': (1.25, -1.2, 0), 'I1': (1.6, -0.82, 0), 'J1': (1.33, -0.82, 0), 'K1': (1.33, -1.2, 0), 'L1': (1.6, -1.2, 0), 'M1': (1.6, -1.13, 0), 'N1': (1.43, -1.13, 0), 'O1': (1.43, -1.06, 0), 'P1': (1.6, -1.06, 0), 'Q1': (1.6, -0.99, 0), 'R1': (1.43, -0.99, 0), 'S1': (1.43, -0.92, 0), 'T1': (1.6, -0.92, 0), 'U1': (1.68, -0.82, 0), 'V1': (1.76, -0.82, 0), 'W1': (1.76, -1.13, 0), 'Z1': (1.92, -1.13, 0), 'A2': (1.88, -1.2, 0), 'B2': (1.68, -1.2, 0), 'C2': (0.22, -1.26, 0), 'D2': (1.86, -1.26, 0), 'E2': (1.82, -1.35, 0), 'F2': (0.22, -1.35, 0)}
        atmel = VGroup(
            Polygon(d["D"],d["C"],d["K"],d["J"],d["I"],d["H"],d["G"],d["F"],d["E"],stroke_width=0,fill_opacity=1),
            Polygon(d["M"],d["R"],d["S"],d["Q"],d["P"],d["O"],d["N"],d["L"],stroke_width=0,fill_opacity=1),
            Polygon(d["T"],d["V"],d["W"],d["Z"],d["H1"],d["G1"],d["F1"],d["E1"],d["D1"],d["C1"],d["B1"],d["A1"],d["U"],stroke_width=0,fill_opacity=1),
            Polygon(d["J1"],d["I1"],d["T1"],d["S1"],d["R1"],d["Q1"],d["P1"],d["O1"],d["N1"],d["M1"],d["L1"],d["K1"],stroke_width=0,fill_opacity=1),
            Polygon(d["U1"],d["V1"],d["W1"],d["Z1"],d["A2"],d["B2"],stroke_width=0,fill_opacity=1),
            Polygon(d["C2"],d["D2"],d["E2"],d["F2"],stroke_width=0,fill_opacity=1)
        ).set_fill(color=YELLOW_A).scale(0.4).rotate(PI).move_to((2.87,-1.77,0))
        board += atmel
        
        cpulabel = VGroup(
            Text("35473D",font="Noto Sans Mono",color=YELLOW_A).scale(0.32).move_to((2,-1.72,0)).rotate(PI),
            Text("ATMEGA328P",font="Noto Sans Mono",color=YELLOW_A).scale(0.3).move_to((2.59,-1.49,0)).stretch(1.09,dim=0).rotate(PI),
            Text("U",font="Noto Sans Mono",color=YELLOW_A).scale(0.3).move_to((1.72,-1.49,0)).rotate(PI),
            Text("2039YE8",font="微软雅黑",color=YELLOW_A).scale(0.3).move_to((2.45,-1.26,0)).stretch(1.07,dim=0).rotate(PI),
            Circle(radius=0.2,color=BLACK,fill_opacity=1).move_to((0.84,-1.54,0)),
            Circle(radius=0.2,color=BLACK,fill_opacity=1).move_to((3.85,-1.54,0))
        )
        board += cpulabel
        
        board.scale(0.7).scale(1.1)
        
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("一块Arduino UNO R3")
        board.next_to(title,DOWN).shift(DOWN * 0.2)
        
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
        
        #self.play(board.animate.scale(0.3,scale_stroke=True))
        self.play(board.animate.proportional_scale(0.3))
        
        
        
