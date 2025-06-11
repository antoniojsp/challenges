


def power_two(num):
    if num == 0:
        return False
    if num == 1:
        return True
    if num%2 != 0:
        return False
    return power_two(num//2)

print(power_two(0))