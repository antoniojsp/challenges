

with open('sample.txt', 'r') as texto:
    lines1 = texto.readlines()


for i in lines1:
    name, texts = i.split(":")

    print(len(texts))