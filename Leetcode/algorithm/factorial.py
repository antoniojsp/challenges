

def iterative_fact(num):
    result = 1
    for i in range(1,num+1):
        result*=i
    return result

print(iterative_fact(13))


def recursion_fact(num):
    if num == 1:
        return 1

    return num * recursion_fact(num - 1)


print(recursion_fact(13))