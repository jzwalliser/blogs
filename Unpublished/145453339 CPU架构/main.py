from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_height = 8.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class Archs(Scene):
    def construct(self):
        def CPU(text,color):
            cpu = VGroup()
            rect = Rectangle(width=2,height=2).scale(1.1)
            cpu += rect
            lline = Line((0,0,0),(0.3,0,0)).move_to(rect.get_left())
            for i in range(1,3):
                cpu += lline.copy().shift(UP * 0.4 * i)
            for i in range(1,3):
                cpu += lline.copy().shift(DOWN * 0.4 * i)
            rline = lline.copy().move_to(rect.get_right())
            for i in range(1,3):
                cpu += rline.copy().shift(UP * 0.4 * i)
            for i in range(1,3):
                cpu += rline.copy().shift(DOWN * 0.4 * i)
            tline = Line((0,0,0),(0,0.3,0)).move_to(rect.get_top())
            for i in range(1,3):
                cpu += tline.copy().shift(LEFT * 0.4 * i)
            for i in range(1,3):
                cpu += tline.copy().shift(RIGHT * 0.4 * i)
            bline = tline.copy().move_to(rect.get_bottom())
            for i in range(1,3):
                cpu += bline.copy().shift(LEFT * 0.4 * i)
            for i in range(1,3):
                cpu += bline.copy().shift(RIGHT * 0.4 * i)
            cpu += lline
            cpu += rline
            cpu += tline
            cpu += bline
            rect.scale(0.9).set_fill(opacity=0.4).set_color(color)
            t = MathTex(text).move_to(rect.get_center())
            cpu += t
            return cpu
        jz = Tex("Jz",color=YELLOW)
        icon = LabeledDot(jz,color=RED).scale(3).scale(0.4).to_edge(DR,buff=0.2)
        title = Title("常见CPU架构与指令")
        x86 = CPU(r"\rm x86",[BLUE,GREEN]).next_to(title,DOWN,buff=-0.3).shift(LEFT * 5).scale(0.5)
        arm = CPU(r"\rm arm",[RED,ORANGE]).next_to(x86,DOWN,buff=-0.3).scale(0.5)
        riscv = CPU(r"\rm risc-v",[PINK,PURPLE]).next_to(arm,DOWN,buff=-0.3).scale(0.5)
        mips = CPU(r"\rm mips",[YELLOW,GOLD]).next_to(riscv,DOWN,buff=-0.3).scale(0.5)
        
        x86s = ["MOV","ADD","SUB","MUL","DIV","AND","OR","XOR","NOT","SHL","SHR","PUSH","POP","CALL","RET","JMP","JE","JNE","CMP","LEA"]
        x86inst = VGroup()
        for i in x86s:
            x86inst += MathTex(r"\rm "+ i).scale(0.5)
        x86inst.arrange_in_grid(rows=2,buff=0.3).next_to(x86,RIGHT).set_color([BLUE_A,GREEN_A])
            
        arms = ["LDR","STR","ADD","SUB","MUL","AND","ORR","EOR","LSL","LSR","BL","B","CBZ","CBNZ","CMP","MOV","LDMIA","STMDB","SVC","NOP"]
        arminst = VGroup()
        for i in arms:
            arminst += MathTex(r"\rm "+ i).scale(0.5)
        arminst.arrange_in_grid(rows=2,buff=0.3).next_to(arm,RIGHT).set_color([RED_A,ORANGE])
        
        riscvs = ["LW","SW","LD","SD","ADDI","ADD","SUB","AND","OR","XOR","SLLI","SRLI","BEQ","BNE","BLT","BGE","JAL","JALR","AUIPC","LUI"]
        riscvinst = VGroup()
        for i in riscvs:
            riscvinst += MathTex(r"\rm "+ i).scale(0.5)
        riscvinst.arrange_in_grid(rows=2,buff=0.3).next_to(riscv,RIGHT).set_color([PINK,PURPLE_A])
        
        mipss = ["LW","SW","LB","SB","ADDU","SUBU","MULTU","DIVU","AND","OR","XOR","SLL","SRL","JR","JAL","BEQ","BNE","SLT","MFHI","MFLO"]
        mipsinst = VGroup()
        for i in mipss:
            mipsinst += MathTex(r"\rm "+ i).scale(0.5)
        mipsinst.arrange_in_grid(rows=2,buff=0.3).next_to(mips,RIGHT).set_color([YELLOW_A,GOLD_A])
        
        self.add(title,icon,x86,arm,x86inst,arminst,riscv,riscvinst,mips,mipsinst)

