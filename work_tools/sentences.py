with open('sample.txt', 'r',  encoding="utf-8") as texto:
    lines = texto.read()

temp = lines.split(".")

for i in temp:
    print(i)