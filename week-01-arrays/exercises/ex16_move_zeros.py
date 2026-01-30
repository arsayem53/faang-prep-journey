# ex15_move_zeros.py
def move_zeros(arr):
    curr_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
           arr[curr_pos] = arr[i]
           curr_pos +=1
    for i in range(curr_pos, len(arr)):
         arr[i] = 0
         curr_pos +=1
arr = [10, 0, 30, 0, 50]
move_zeros(arr)
print(f"Zero moved: {arr}")