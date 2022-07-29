from dataclasses import replace


f = open("readme.md", "r")
f2 = open("readme2.md", "x")
f2 = open("readme2.md", "w")

text = f.readlines()
for s in text:
    s = s.replace(" ", "")
    f2.write(s)

print(f2)

