from manim import *

class MixScale:
    def scale_about(self,factor,point,scale_stroke=True):
        if isinstance(point,Mobject):
            point = tuple(point.get_center())
        x_new = point[0] + factor * (self.get_center()[0] - point[0])
        y_new = point[1] + factor * (self.get_center()[1] - point[1])
        self.move_to((x_new,y_new,0))
        print((x_new,y_new,0),self.get_center())
        self.scale(factor,scale_stroke=scale_stroke)
        return self

class MixTextScale:
    def scale_about(self,factor,point,scale_stroke=False):
        if isinstance(point,Mobject):
            point = tuple(point.get_center())
        x_new = point[0] + factor * (self.get_center()[0] - point[0])
        y_new = point[1] + factor * (self.get_center()[1] - point[1])
        self.move_to((x_new,y_new,0))
        self.scale(factor,scale_stroke=scale_stroke)
        return self

class MixGroup:
    def smart_scale(self,factor):
        for m in self.get_family():
            if hasattr(m,"scale_about"):
                m.scale_about(factor,self.get_center())
        return self

class Square(MixScale,Square): pass

class Polygon(MixScale,Polygon): pass

class Rectangle(MixScale,Rectangle): pass

class RoundedRectangle(MixScale,RoundedRectangle): pass

class Circle(MixScale,Circle): pass

class Line(MixScale,Line): pass

class Dot(MixScale,Dot): pass

class Intersection(MixScale,Intersection): pass

class Union(MixScale,Union): pass

class Text(MixTextScale,Text): pass

class Tex(MixTextScale,Tex): pass

class MathTex(MixTextScale,MathTex): pass

class VGroup(MixGroup,VGroup): pass

class ScaleAboutPoint(Scene):
    def construct(self):
        
        vg = VGroup(
            VGroup(Circle().move_to((0,5,0)), Rectangle()),
            Dot(),
            Text("Hi")
        ).shift(LEFT)
        self.add(SurroundingRectangle(vg[0][1]))
        
        self.add(Dot(vg.get_center()))
                
        self.play(vg.animate.smart_scale(0.3))
        
        '''s = Square().shift(RIGHT)
        self.add(Dot((-1,0,0)))
        self.play(s.animate.scale_about(0.5,(-1,0,0)))'''
        

        
        
