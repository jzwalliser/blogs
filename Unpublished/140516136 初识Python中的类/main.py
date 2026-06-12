from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Derived(Scene):
    def construct(self):
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("类的继承中函数覆盖")
        base1 = Rectangle(width=5,height=2.5,color=YELLOW).set_fill(color=YELLOW,opacity=0.4).next_to(title,DOWN).shift(LEFT * 3)
        base2 = Rectangle(width=5,height=2.5,color=RED).set_fill(color=RED,opacity=0.4).next_to(title,DOWN).shift(RIGHT * 3)
        base1_text = MathTex(r"\rm Base1").move_to(base1.get_top()).shift(DOWN * 0.3)
        base2_text = MathTex(r"\rm Base2").move_to(base2.get_top()).shift(DOWN * 0.3)
        base1_func1_rect = Rectangle(width=3,height=0.6,color=YELLOW).set_fill(color=YELLOW,opacity=1).move_to(base1.get_center()).shift(UP * 0.3)
        base1_func2_rect = Rectangle(width=3,height=0.6,color=YELLOW).set_fill(color=YELLOW,opacity=1).move_to(base1.get_center()).shift(DOWN * 0.6)
        base1_func1_text = MathTex(r"\rm func1",color=BLACK).move_to(base1_func1_rect.get_center())
        base1_func2_text = MathTex(r"\rm func2",color=BLACK).move_to(base1_func2_rect.get_center())
        base2_func2_rect = Rectangle(width=3,height=0.6,color=RED).set_fill(color=RED,opacity=1).move_to(base2.get_center()).shift(UP * 0.3)
        base2_func3_rect = Rectangle(width=3,height=0.6,color=RED).set_fill(color=RED,opacity=1).move_to(base2.get_center()).shift(DOWN * 0.6)
        base2_func2_text = MathTex(r"\rm func2",color=BLACK).move_to(base2_func2_rect.get_center())
        base2_func3_text = MathTex(r"\rm func3",color=BLACK).move_to(base2_func3_rect.get_center())
        self.add(title,icon)
        derived = Rectangle(width=13,height=2,color=GREEN).set_fill(color=GREEN,opacity=0.4).next_to(title,DOWN).shift(DOWN * 3)
        derived_text = MathTex(r"\rm Derived(Base1,Base2)").move_to(derived.get_top()).shift(DOWN * 0.3)
        derived_text[0][7:13].color = YELLOW
        derived_text[0][14:19].color = RED
        
        b1f1group = VGroup(base1_func1_rect,base1_func1_text).copy()
        b1f2group = VGroup(base1_func2_rect,base1_func2_text).copy()
        b2f2group = VGroup(base2_func2_rect,base2_func2_text).copy()
        b2f3group = VGroup(base2_func3_rect,base2_func3_text).copy()

        overwrite_text = MathTex(r"\text{同名函数，前者被覆盖}").move_to(derived.get_bottom()).shift(UP * 0.4)
        
        self.play(FadeIn(base1),FadeIn(base2),FadeIn(base1_text),FadeIn(base2_text),FadeIn(base1_func1_rect),FadeIn(base1_func2_rect),FadeIn(base1_func1_text),FadeIn(base1_func2_text),FadeIn(base2_func2_rect),FadeIn(base2_func3_rect),FadeIn(base2_func2_text),FadeIn(base2_func3_text),FadeIn(derived),FadeIn(derived_text))
        self.play(Circumscribe(derived_text[0][7:13]))
        self.play(b1f1group.animate.move_to(derived.get_center()).shift(LEFT * 4))
        self.play(b1f2group.animate.move_to(derived.get_center()))
        
        self.play(Circumscribe(derived_text[0][14:19]))
        self.play(b2f2group.animate.move_to(derived.get_center()),Write(overwrite_text))
        self.play(b2f3group.animate.move_to(derived.get_center()).shift(RIGHT * 4),FadeOut(b1f2group))
        self.play(FadeOut(overwrite_text),FadeOut(base1),FadeOut(base2),FadeOut(base1_text),FadeOut(base2_text),FadeOut(base1_func1_rect),FadeOut(base1_func2_rect),FadeOut(base1_func1_text),FadeOut(base1_func2_text),FadeOut(base2_func2_rect),FadeOut(base2_func3_rect),FadeOut(base2_func2_text),FadeOut(base2_func3_text))

        derived2 = Rectangle(width=5,height=6,color=GREEN).set_fill(color=GREEN,opacity=0.4).next_to(title,DOWN).shift(LEFT * 3.5)
        self.play(ReplacementTransform(derived,derived2),derived_text.animate.move_to(derived2.get_top()).shift(DOWN * 0.3),b1f1group.animate.move_to(derived2.get_center()).shift(UP * 1.4),b2f2group.animate.move_to(derived2.get_center()),b2f3group.animate.move_to(derived2.get_center()).shift(DOWN * 1.4))
        text1 = MathTex(r"\text{来自}\rm Base1",color=YELLOW).next_to(b1f1group,RIGHT).shift(RIGHT * 2)
        arr1 = Arrow(b1f1group.get_right(),text1.get_left())
        text2 = MathTex(r"\text{来自}\rm Base2",color=RED).next_to(b2f2group,RIGHT).shift(RIGHT * 2)
        arr2 = Arrow(b2f2group.get_right(),text2.get_left())
        text3 = MathTex(r"\text{来自}\rm Base2",color=RED).next_to(b2f3group,RIGHT).shift(RIGHT * 2)
        arr3 = Arrow(b2f3group.get_right(),text3.get_left())
        self.play(LaggedStart(GrowArrow(arr1),Write(text1),GrowArrow(arr2),Write(text2),GrowArrow(arr3),Write(text3),lag_ratio=0.1))
        self.wait(1)
        self.play(FadeOut(arr1),FadeOut(arr2),FadeOut(arr3),FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(derived2),FadeOut(b1f1group),FadeOut(b2f2group),FadeOut(b2f3group),FadeOut(derived_text))
        

