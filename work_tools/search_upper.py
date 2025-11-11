with open('sample.txt', 'r') as texto:
    lines1 = texto.readlines()


count = 0

for word in lines1:
    word = word.split(" ")
    for i in word:
        if i.isupper():
            print(i)

            count+=1


print(count)