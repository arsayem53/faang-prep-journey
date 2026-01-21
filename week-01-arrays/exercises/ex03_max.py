#ex03_max.py

def arr_max(numbers): 
    maximum = numbers[0]
    for i in range(len(numbers)):
        if maximum <= numbers[i]:
            maximum = numbers[i]
    return maximum

numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]   

maximum = arr_max(numbers)
print(f"Array max is: {maximum}")
