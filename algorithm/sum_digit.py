

def sum_digit(num):
    if num == 0:
        return 0
    digit = num%10
    return digit + sum_digit(num//10)






print(sum_digit(17))