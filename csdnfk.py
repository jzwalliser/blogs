import re

def is_markdown_syntax(ch, prev_ch):
    """
    判断是否是 markdown 语法符号
    """
    # 标题 #
    if ch == '#':
        return True
    if ch == '@':
        return True
    if ch == '>':
        return True
    if ch == ':':
        return True
    if ch == '\n':
        return True
    # 表格 |
    if ch == '|':
        return True
    # 列表符号 *, -, +
    if ch in ('*', '-', '+'):
        return True
    # 数字序号 1. 2. 等
    if prev_ch.isdigit() and ch == '.':
        return True
    return False


def analyze_markdown_char_by_char(text):
    i = 0
    n = len(text)

    # 状态变量
    in_code_block = False
    in_inline_code = False
    in_math = False          # $ ... $
    in_display_math = False  # $$ ... $$
    in_link_or_image = False
    in_kbd = False

    results = []

    while i < n:
        ch = text[i]
        prev_ch = text[i - 1] if i > 0 else ''
        
        if text[i:i+5] == '<kbd>':
            in_code_block = True
            for _ in range(5):
                results.append(False)
                i += 1
            continue
        if text[i:i+6] == '</kbd>':
            in_code_block = False
            for _ in range(6):
                results.append(False)
                i += 1
            continue

        # 1. 代码块 
        if text[i:i+3] == '```':
            in_code_block = not in_code_block
            for _ in range(3):
                results.append(False)
                i += 1
            continue

        if in_code_block:
            results.append(False)
            i += 1
            continue

        # 2. 行内代码 `
        if ch == '`' and not in_inline_code:
            in_inline_code = True
            results.append(False)
            i += 1
            continue
        elif ch == '`' and in_inline_code:
            in_inline_code = False
            results.append(False)
            i += 1
            continue

        if in_inline_code:
            results.append(False)
            i += 1
            continue

        # 3. 数学公式 
        if text[i:i+2] == '':
            in_display_math = not in_display_math
            results.append(False)
            results.append(False)
            i += 2
            continue

        if in_display_math:
            results.append(False)
            i += 1
            continue

        # 4. 数学公式 $
        if ch == '$' and not in_math:
            in_math = True
            results.append(False)
            i += 1
            continue
        elif ch == '$' and in_math:
            in_math = False
            results.append(False)
            i += 1
            continue

        if in_math:
            results.append(False)
            i += 1
            continue

        # 5. 图片或链接 !url 或 url
        if ch == '!' and text[i:i+2] == '![':
            in_link_or_image = True
            results.append(False)
            i += 1
            continue

        if ch == '[' and not in_link_or_image:
            if text[i:i+2] != '![':
                in_link_or_image = True
            results.append(False)
            i += 1
            continue

        if in_link_or_image:
            if ch == ')':
                in_link_or_image = False
            results.append(False)
            i += 1
            continue

        # 6. Markdown 语法符号
        if is_markdown_syntax(ch, prev_ch):
            results.append(False)
            i += 1
            continue

        # 7. 普通正文
        results.append(True)
        i += 1

    return results#

if __name__ == "__main__":
    import tkinter
    #root = tkinter.Tk()
    #text = tkinter.Text(root)
    
    filepath = "file.md"  # 修改为你的 markdown 文件路径
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    result = analyze_markdown_char_by_char(content)
    
    for idx,flag in enumerate(result):
        if result[idx]:
            print(f"\033[1;32;40m{content[idx]}\033[0m",end="")
        else:
            print(f"{content[idx]}",end="")

    output = ""
    for idx,flag in enumerate(result):
        if result[idx]:
            output += content[idx] + "&#8203;"
        else:
            output += content[idx]

    w = open("result.txt","wb")
    w.write(output.encode("utf-8"))
    w.close()



