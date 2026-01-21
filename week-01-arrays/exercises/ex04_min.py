#ex04_min.py
def arr_min(numbers):  
    minimum = numbers[0]
    for i in range(len(numbers)):
        if minimum >= numbers[i]:
            minimum = numbers[i]
    return minimum


numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]
minimum = arr_min(numbers)
print(f"Array min is: {minimum}")