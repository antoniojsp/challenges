
def sum_elements(arr, index = 0):
    if index == len(arr):
        return 0
    return arr[index] + sum_elements(arr, index+1)

print(sum_elements([1,2,3, 10, 5]))