with open('sample.txt', 'r') as texto:
    lines1 = texto.readlines()


words = str(lines1).split(" ")
for i in words:
 print(i)