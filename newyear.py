
"""
I am really grateful to the sololearn community for the code of the day and the massive likes and congrats from the lads here at the community

i refuse to believe there wouldn't be another better :) 

thanks everyone!!!, and a happy new year.....
"""

import sys, codecs  

#YOUR NAME
sololearner = (input("") or "Sololearner").upper()    

sys.stdout = codecs.getwriter("utf_16")(sys.stdout.buffer,'strict')  

style_cr = lambda ch: chr(0x1f0ef + ord(ch))  

width = lambda ch, t, c=0: (style_cr(ch) + "\t"*t + style_cr(ch)).center(c)  

fill = lambda ch, t, c=0: (style_cr(ch) * t).center(c)  

char_style = {     
'A': (fill("a", 1, 20), width("a", 2, 13), fill("a", 4, 10), *(width("a", i, 10) for i in (4, 5))),      

'B': (fill("b", 4), *(width("b", i) for i in (4, 5)), fill("b", 5), *(width("b", i) for i in (5, 4)), fill("b", 4)),      

'C': (fill("c", 5), *(style_cr("c") for i in range(3)), fill("c", 5)),      

'D': (fill("d", 3), *(width("d", i) for i in (3, 4, 4, 3)), fill("d", 3)),      

'E': (fill("e", 5), style_cr("e"), fill("e", 3), style_cr("e"), fill("e", 5)),      

'F': (fill("f", 5), style_cr("f"), fill("f", 3), *(style_cr("f") for _ in range(2))),      

'G': (fill("g", 5), width("g", 5), style_cr("g"), style_cr("g") + "\t"*4 + style_cr("g") + style_cr("g"), width("g", 5), fill("g", 5)),      

'H': (*(width("h", 5) for _ in range(2)), fill("h", 5, 6), *(width("h", 5) for _ in range(2))),      

'I': (fill("i", 3, 10), *(fill("i", 1, 15) for _ in range(3)), fill("i", 3, 10)),      

'J': (fill("j", 3, 10), *(fill("j", 1, 15) for _ in range(2)), width("j", 2), fill("j", 3, 1)),      

'K': (width("k", i) for i in (2, 1, 0, 1, 2)),      

'L': (*(style_cr("l") for _ in range(4)), fill("l", 3)),      

'M': (width('m', 6), style_cr("m") + "\t" + style_cr("m") + "\t"*2 +style_cr("m") + "\t" + style_cr("m"), style_cr("m") + "\t"*2 + style_cr("m")*2 + "\t" +style_cr("m"), *(width('m', 6) for _ in range(2))),      

'N': (width("n", 4), style_cr("n")*2 + "\t"*2 + style_cr("n"), style_cr("n") + "\t" + style_cr("n") + "\t"*2 + style_cr("n"), style_cr("n") + "\t"*2 + style_cr("n") + "\t" + style_cr("n"), style_cr("n") + "\t"*2 + style_cr("n")*2, width("n", 4)),      

'O': (fill("o", 1, 13), width("o", 2, 7), *(width("o", 4, 6) for _ in range(3)), width("o", 2, 7), fill("o", 1, 13)),      

'P': (fill("p", 4), *(width("p", 4) for i in range(2)), fill("p", 4), *(style_cr("p") for i in range(2))),      

'Q': (fill("q", 4, 5), *(width("q", 4) for i in range(2)), style_cr("q") + "\t"*2 + style_cr("q") + "\t" +style_cr("q"), fill("q", 4, 5), "\t"*5 + style_cr("q")),      

'R': (fill("r", 4, 5), *(width("r", 4) for _ in range(2)), fill("r", 4), *(width("r", i) for i in range(4, 7))),      

'S': (fill("s", 4, 5), width("s", 4), "\t" + style_cr("s"), "\t"*2 + style_cr("s"), "\t"*3 + style_cr("s"), "\t"*4 + style_cr("s"), width("s", 4), fill("s", 4, 5)),      

'T': (fill("t", 4), *(fill("t", 1, 12) for _ in range(4))),      

'U': (*(width("u", 4) for _ in range(4)), fill("u", 4, 5)),      

'V': (*(" "*i + width("v", j, 10) for i, j in enumerate((5, 4, 3, 2))), fill("v", 1, 23)),      

'W': (*(width('w', 6) for _ in range(2)), style_cr("w") + "\t"*2 + style_cr("w")*2 + "\t" +style_cr("w"), style_cr("w") + "\t" + style_cr("w") + "\t"*2 +style_cr("w") + "\t" + style_cr("w"), width('w', 6)),      

'X': (*(" "*i + width("x", j, 10) for i, j in enumerate((4, 3, 2))), style_cr("x").center(18), *(width("x", i, 10) for i in (2, 3, 4))),      

'Y': (*(" "*i + width("y", j, 10) for i, j in enumerate((4, 3, 2))), *(fill("y", 1, 20) for _ in range(3))),      

'Z': (fill("z", 5), *("\t"*i + style_cr("z") for i in range(5, -1, -1)), fill("z", 5)) 
}  

for i in ("Happy New Year " + sololearner + " from Lexzy").upper().split():
    for j in i: print(*char_style[j], sep="\n", end="\n\n")
    print(end="\n\n\n\n")

print("Welcome to 2019 everyone!!!）
