from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class FileFragments(Scene):
    def construct(self):
        def video_part(part):
            video = SVGMobject("video.svg").scale(0.3)
            dot = LabeledDot(MathTex(f"{part}"),color=RED).scale(0.6).next_to(video,DR,buff=-0.1)
            return VGroup(video,dot)
        title = Title("文件碎片化")
        sections1 = Rectangle(width=1.5,height=1.5)
        sections2 = Rectangle(width=1.5,height=1.5).next_to(sections1,RIGHT,buff=0)
        sections3 = Rectangle(width=1.5,height=1.5).next_to(sections2,RIGHT,buff=0)
        sections4 = Rectangle(width=1.5,height=1.5).next_to(sections3,RIGHT,buff=0)
        sections5 = Rectangle(width=1.5,height=1.5).next_to(sections4,RIGHT,buff=0)
        sections6 = Rectangle(width=1.5,height=1.5).next_to(sections5,RIGHT,buff=0)
        sectionsw = DashedVMobject(Rectangle(width=2,height=1.5)).next_to(sections6,RIGHT,buff=0)
        sectionsn = Rectangle(width=1.5,height=1.5).next_to(sectionsw,RIGHT,buff=0)
        disc = VGroup(sections1,sections2,sections3,sections4,sections5,sections6,sectionsw,sectionsn).center().shift(DOWN * 2)
        sec1text = Text("扇区1").scale(0.6).next_to(sections1,DOWN)
        sec2text = Text("扇区2").scale(0.6).next_to(sections2,DOWN)
        sec3text = Text("扇区3").scale(0.6).next_to(sections3,DOWN)
        sec4text = Text("扇区4").scale(0.6).next_to(sections4,DOWN)
        sec5text = Text("扇区5").scale(0.6).next_to(sections5,DOWN)
        sec6text = Text("扇区6").scale(0.6).next_to(sections6,DOWN)
        secwtext = Text("好多扇区").scale(0.6).next_to(sectionsw,DOWN)
        secntext = Text("扇区n").scale(0.6).next_to(sectionsn,DOWN)
        frame1 = Rectangle(width=1.5,height=3,stroke_width=0).next_to(title,DOWN,buff=0.5).shift(LEFT * 2).shift(UP * 0.2).set_fill(color=BLUE,opacity=0.4)
        frame2 = Rectangle(width=1.5,height=3,stroke_width=0).next_to(title,DOWN,buff=0.5).shift(RIGHT * 2).shift(UP * 0.2).set_fill(color=GREEN,opacity=0.4)
        download = SVGMobject("chrome.svg").scale(0.3).next_to(title,DOWN,buff=0.5).shift(LEFT * 2)
        copy = SVGMobject("file_explorer.svg").scale(0.3).next_to(title,DOWN,buff=0.5).shift(RIGHT * 2)
        self.add(title,frame1,frame2,disc,sec1text,sec2text,sec3text,sec4text,sec5text,sec6text,secwtext,secntext)
        self.add(download,copy)
        
        
        part1 = video_part(1).next_to(download,DOWN)
        downloadtext = Text("下载").scale(0.3).next_to(part1,DOWN)
        filenamevideo = MathTex(r"\rm video.mp4").scale(0.5).next_to(downloadtext,DOWN,buff=0.1)
        frag1 = MathTex(r"\rm Part 1").scale(0.5).next_to(filenamevideo,DOWN,buff=0.1)
        self.play(Write(part1),Write(downloadtext),Write(filenamevideo),Write(frag1))
        #self.play()
        self.play(part1.animate.move_to(sections1),sections1.animate.set_fill(opacity=0.4,color=BLUE),FadeOut(frag1))
        part2 = video_part(2).next_to(download,DOWN)
        frag2 = MathTex(r"\rm Part 2").scale(0.5).next_to(filenamevideo,DOWN,buff=0.1)
        self.play(Write(part2),Write(frag2))
        #self.play()
        self.play(part2.animate.move_to(sections2),sections2.animate.set_fill(opacity=0.4,color=BLUE),FadeOut(frag2))
        part3 = video_part(3).next_to(download,DOWN)
        frag3 = MathTex(r"\rm Part 3").scale(0.5).next_to(filenamevideo,DOWN,buff=0.1)
        self.play(Write(part3),Write(frag3))
        #self.play()
        pic0 = SVGMobject("image.svg").scale(0.3)
        one = MathTex("1").set_opacity(0)
        picd = LabeledDot(one,color=RED,fill_opacity=0,stroke_width=0).scale(0.6).next_to(pic0,DR,buff=-0.1)
        pic = VGroup(pic0,picd).next_to(copy,DOWN)
        copytext = Text("复制").scale(0.3).next_to(pic,DOWN)
        filenamepic = MathTex(r"\rm image.jpg").scale(0.5).next_to(copytext,DOWN,buff=0.1)
        #self.play()
        self.play(part3.animate.move_to(sections3),sections3.animate.set_fill(opacity=0.4,color=BLUE),Write(pic0),FadeOut(frag3),Write(copytext),Write(filenamepic))
        
        #self.play()
        part4 = video_part(4).next_to(download,DOWN)
        frag4 = MathTex(r"\rm Part 4").scale(0.5).next_to(filenamevideo,DOWN,buff=0.1)
        #self.play()
        #self.play()
        
        self.play(pic.animate.move_to(sections4),sections4.animate.set_fill(opacity=0.4,color=GREEN),Write(part4),FadeOut(copytext),FadeOut(filenamepic),Write(frag4))
        self.play(part4.animate.move_to(sections5),sections5.animate.set_fill(opacity=0.4,color=BLUE),FadeOut(downloadtext),FadeOut(filenamevideo),FadeOut(frag4))


        fragment1brace = Brace(VGroup(sections1,sections2,sections3),UP)
        fragment2brace = Brace(sections5,UP)


        fragment1text = Text("碎片").scale(0.8).next_to(fragment1brace,UP)
        fragment2text = Text("碎片").scale(0.8).next_to(fragment2brace,UP)
        self.play(Write(fragment1brace),Write(fragment1text))
        self.play(Write(fragment2brace),Write(fragment2text))
        self.wait(1)
        self.play(FadeOut(fragment1brace),FadeOut(fragment1text),FadeOut(fragment2brace),FadeOut(fragment2text),FadeOut(part1),FadeOut(part2),FadeOut(part3),FadeOut(part4),FadeOut(pic),sections1.animate.set_fill(opacity=0.4,color=BLACK),sections2.animate.set_fill(opacity=0.4,color=BLACK),sections3.animate.set_fill(opacity=0.4,color=BLACK),sections4.animate.set_fill(opacity=0.4,color=BLACK),sections5.animate.set_fill(opacity=0.4,color=BLACK))




