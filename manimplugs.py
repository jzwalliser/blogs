from manim import *

#==自定义mobject===

class Glow(VGroup):
    def __init__(self,mobject,outer_radius=1,inner_radius=0.1,rings=10,color=YELLOW,*args,**kwargs):
        super().__init__(*args,**kwargs)
        d = (outer_radius - inner_radius) / rings
        if d < 0:
            raise ValueError("Outer radius greater than inner radius. Consider swapping the values.")
        for i in range(rings):
            layer = Circle(radius=outer_radius - i * d,stroke_width=0,fill_color=color,fill_opacity=0.08)
            layer.set_stroke(0,background=True)
            self += layer
        self.move_to(mobject)
        
#==改良mobject 注入区==

class MixGroup:
    def proportional_scale(self,factor,**kwargs):
        """
         等比缩放 VGroup：
        - 几何点位正常缩放
        - VMobject 的 stroke_width 按 factor 缩放
        - Text / MathTex 的 font_size 按 factor 缩放
        """
        
        self.scale(factor)

        # 1. 等比缩放矢量描边
        for mob in self.get_family():
            if not isinstance(mob,(Text,Tex,MathTex)):
                w = mob.get_stroke_width()
                if w > 0:
                    #mob.set_stroke(width=w * factor)
                    mob.set_stroke(width=abs(factor) * w)
                    mob.set_stroke(
                        width=abs(factor) * mob.get_stroke_width(background=True),
                        background=True,
                    )

        return self

#==改良mobject 修改区===

class VGroup(MixGroup,VGroup): pass

class VDict(MixGroup,VDict): pass
