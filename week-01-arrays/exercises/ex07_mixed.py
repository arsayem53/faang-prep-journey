#ex08_mixed.py

def arr_print(numbers):
    print("All array inputs are:")
    for i in range(len(numbers)):
        print(f"{numbers[i]}")


def arr_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


def arr_max(numbers): 
    maximum = numbers[0]
    for i in range(len(numbers)):
        if maximum <= numbers[i]:
            maximum = numbers[i]
    return maximum


def arr_min(numbers):  
    minimum = numbers[0]
    for i in range(len(numbers)):
        if minimum >= numbers[i]:
            minimum = numbers[i]
    return minimum


def arr_count(numbers):
    count = 0
    target = int(input("Enter your target number: "))
    for num in numbers:
        if target == num:
            count += 1
        else:
            continue
    return count



def arr_linear_search(numbers):
    position = -1
    target = int(input("Enter your target number: "))
    for i in range(len(numbers)):
        if target == numbers[i]:
            position = i
            break
        else:
            continue
    return position



numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]
while True:
    option = int(input("""Which operation you wanna do:
               1. Print all array inputs
               2. print array sum
               3. print array max
               4. print array min
               5. print occurance of target number
               6. linear search
               7. Break
               """))
    if option == 1:
        arr_print(numbers)
    elif option == 2:
        total = arr_sum(numbers)
        print(f"Array sum is: {total}")
    elif option == 3:    
        maximum = arr_max(numbers)
        print(f"Array max is: {maximum}")
    elif option == 4:
        minimum = arr_min(numbers)
        print(f"Array min is: {minimum}")
    elif option == 5:
        count = arr_count(numbers)
        print(f"Occurence = {count}")
    elif option == 6:
        position = arr_linear_search(numbers)
        if position == -1:
            print(f"Not found")
        else:
            print(f"Position = {position}")  
    elif option == 7:
        break
    