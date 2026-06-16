from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)    
  
class Hash(Scene):
    def construct(self):
        def hashing(text,hashvalue,hashmethod="MD5",color=YELLOW):
            hashtext = MathTex(r"\rm " + hashmethod,color=color)
            rect = SurroundingRectangle(hashtext).set_color(color).set_fill(opacity=0.4)
            cont = Text(text,font="Noto Sans Mono",color=GREEN).scale(0.5).next_to(rect,LEFT)
            hashout = Text(hashvalue,font="Noto Sans Mono").scale(0.5)
            hashoutrect = RoundedRectangle(width=hashout.get_width() + 0.3,height=hashout.get_height() + 0.1,corner_radius=0.1,stroke_width=0).set_fill(color=PINK,opacity=0.4)
            hashout.move_to(hashoutrect)
            return VGroup(cont,VGroup(rect,hashtext).scale(0.8),VGroup(hashout,hashoutrect)).center()    
        title = Title("哈希")
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        group1 = hashing(r"Hello World!","ED076287532E86365E841E92BFC50D8C").next_to(title,DOWN)
        group2 = hashing(r"Hello, World!","65A8E27D8879283831B664BD8B7F0AD4").next_to(group1,DOWN)
        group3 = hashing(r"Hello World!","2EF7BDE608CE5404E97D5F042F95F89F\n1C232871","SHA1",RED).next_to(group2,DOWN)
        group4 = hashing(r"Hello World!","4575BB4EC129DF6380CEDDE6D71217FE\n0536F8FFC4E18BCA530A7A1B","SHA224",GREEN).next_to(group3,DOWN)
        group5 = hashing(r"Hello World!","7F83B1657FF1FC53B92DC18148A1D65D\nFC2D4B1FA3D677284ADDD200126D9069","SHA256",BLUE).next_to(group4,DOWN)
        group6 = hashing(r"Hello World!","861844D6704E8573FEC34D967E20BCFE\nF3D424CF48BE04E6DC08F2BD58C72974\n3371015EAD891CC3CF1C9D34B49264B5\n10751B1FF9E537937BC46B5D6FF4ECC8","SHA512",PURPLE).next_to(group5,DOWN)
        everything = MobjectTable([[Tex("初始内容").scale(0.8),Tex("哈希算法").scale(0.8),Tex("哈希").scale(0.8)],[group1[0],group1[1],group1[2]],[group2[0],group2[1],group2[2]],[group3[0],group3[1],group3[2]],[group4[0],group4[1],group4[2]],[group5[0],group5[1],group5[2]],[group6[0],group6[1],group6[2]]],h_buff=0.3,v_buff=0.2,line_config={"stroke_width":1,"color":GREY}).next_to(title,DOWN)
        self.add(title,everything,icon)



