# Week 1: Arrays - Theory Notes

## Day 1: Array Basics

### 1. Arrays vs Lists (Python)
- Python lists behave like dynamic arrays internally.
- Elements are stored in contiguous memory locations.
- Access by index is O(1) because memory is contiguous.
- Appending at the end is O(1) amortized; resizing happens occasionally.
- Inserting or deleting at a position requires shifting elements → O(n).

### 2. Time Complexity Recap
| Operation              | Complexity |
|------------------------|------------|
| Access by index        | O(1)       |
| Search (linear)        | O(n)       |
| Insert at end          | O(1) amortized |
| Insert at index        | O(n)       |
| Delete at index        | O(n)       |

### 3. Key Operations Practiced
1. Traverse array  
2. Sum of elements  
3. Find maximum  
4. Find minimum  
5. Count occurrences of a target  
6. Linear search  
7. Concatenate array (LeetCode #1929)

### 4. Important Observations
- Traversal always takes O(n), even for max, sum, or search.
- Accessing `numbers[i]` is O(1) because of contiguous memory.
- Python lists are dynamic arrays, but operations like insertion/deletion in the middle are expensive.
- Concatenation (`nums + nums`) creates a new array → O(n) time and O(n) space.
- Even one-liner solutions obey time complexity rules.

### 5. LeetCode Platform Notes
- LeetCode expects a function inside a `Solution` class.
- Only the **return value** is checked; `print()` is ignored.
- Function signature must match exactly; otherwise, submission fails.

- 
## Day 2: Array Manipulation & 2D Arrays

### 1. Two-Pointer Technique
- **Pattern:** Use two indices moving toward each other or in same direction
- **Common uses:** Reverse array, palindrome check, two sum (sorted), remove duplicates
- **Example (Reverse):**
```python
  left, right = 0, len(arr) - 1
  while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
```
- **Complexity:** O(n) time, O(1) space (in-place modification)

### 2. In-Place Algorithms
- **Definition:** Modifies original data structure without creating a copy
- **Space advantage:** O(1) instead of O(n)
- **Trade-off:** Original data is lost (can't recover it)
- **Examples:** Reverse in-place, prefix sum in-place

### 3. Shallow Copy vs Deep Copy
- **Shallow Copy:** Copies top-level structure only
  - Works fine for simple types (int, string)
  - **Fails** with nested structures (list of lists)
  - Methods: `arr[:]`, `arr.copy()`, `list(arr)`
  
- **Deep Copy:** Recursively copies everything
  - Safe for nested structures
  - Method: `copy.deepcopy(arr)`
  
- **Visual:**
```
  original = [[1, 2], [3, 4]]
  shallow = original[:]     # Shares inner lists
  deep = copy.deepcopy(original)  # Independent copy
```

### 4. Insert/Delete Operations - The O(n) Reality
- **Insert at position k:** Must shift all elements after k to the right → O(n)
- **Delete at position k:** Must shift all elements after k to the left → O(n)
- **Why expensive:** 
  - Worst case: insert/delete at index 0 (shift all n elements)
  - Best case: insert/delete at end (no shifting) → O(1)
- **Key insight:** Contiguous memory is fast for access but slow for modification

### 5. Prefix Sum Pattern ⭐ IMPORTANT
- **Definition:** Running sum where `result[i] = sum of elements from 0 to i`
- **Formula:** `arr[i] = arr[i-1] + arr[i]` (for i ≥ 1)
- **Pattern:**
```python
  for i in range(1, len(arr)):
      arr[i] += arr[i-1]
```
- **Use cases:**
  - Range sum queries
  - Subarray problems
  - Many DP problems
- **Complexity:** O(n) time, O(1) space (if modifying in-place)

### 6. 2D Arrays (Matrices)
- **Structure:** Array of arrays (rows and columns)
- **Access:** `matrix[row][col]`
- **Iteration patterns:**
```python
  # Pattern 1: Pythonic
  for row in matrix:
      for element in row:
          # process
  
  # Pattern 2: With indices
  for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          # process matrix[i][j]
  
  # Pattern 3: With enumerate
  for i, row in enumerate(matrix):
      for j, element in enumerate(row):
          # process with indices
```
- **Time complexity:** O(m × n) where m = rows, n = columns

### 7. Time & Space Complexity Summary - Day 2

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Reverse (two-pointer) | O(n) | O(1) | In-place, swap elements |
| Shallow copy | O(n) | O(n) | Copy references only |
| Deep copy | O(n×d) | O(n×d) | d = depth of nesting |
| Insert at position | O(n) | O(1) | Must shift elements |
| Delete at position | O(n) | O(1) | Must shift elements |
| Prefix sum (in-place) | O(n) | O(1) | Modify original |
| Traverse 2D array | O(m×n) | O(1) | Visit all elements |

### 8. Key Operations Practiced
1. Reverse array using two pointers (ex07)
2. Shallow vs deep copy experiments (ex08)
3. Insert element at position (ex09)
4. Delete element at position (ex10)
5. Running sum / prefix sum (LeetCode #1480) ⭐
6. Maximum in 2D array (LeetCode #1672)

### 9. Important Patterns to Remember

**Two-Pointer (Converging):**
```python
left, right = 0, len(arr) - 1
while left < right:
    # Process arr[left] and arr[right]
    left += 1
    right -= 1
```

**Prefix Sum:**
```python
for i in range(1, len(arr)):
    arr[i] = arr[i-1] + arr[i]
```

**2D Array Sum:**
```python
max_sum = 0
for row in matrix:
    row_sum = sum(row)
    max_sum = max(max_sum, row_sum)
```

### 10. Space Complexity Intuition
- **O(1) space:** Only a few variables, doesn't grow with input
  - Examples: two pointers, max tracking, in-place operations
- **O(n) space:** New array/structure of size n
  - Examples: creating copy, building new result array
- **Key question:** "Am I creating a new data structure that grows with input size?"

## Day 3: Array Operations & Algorithms

### 1. Remove Duplicates Pattern

**Problem:** Remove duplicate elements from an array

**Approach 1: Using Hash Set (Unsorted Array)**
- Use a `set()` to track elements we've seen
- Only add elements to result if not in set
- **Time:** O(n), **Space:** O(n)
```python
def remove_duplicates(arr):
    seen = set()
    result = []
    for element in arr:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result
```

**Use case:** Unsorted arrays where order must be preserved

---

### 2. Merge Two Sorted Arrays ⭐ IMPORTANT

**Pattern:** Two-pointer merge (used in Merge Sort!)

**Algorithm:**
1. Use two pointers `i` and `j` for each array
2. Compare elements at both pointers
3. Take the smaller one, advance that pointer
4. After one array exhausted, copy remaining from other

**Visualization:**
```
arr1 = [1, 3, 5]    arr2 = [2, 4, 6]
        ↑                    ↑
        i                    j

Compare: 1 vs 2 → Take 1, i++
result = [1]

Compare: 3 vs 2 → Take 2, j++
result = [1, 2]

... continue until one array empty
Copy remaining elements
```

**Code Pattern:**
```python
def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    
    # Merge while both have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Copy remaining (only one will have elements left)
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
```

**Key Points:**
- Each element visited exactly once → O(n + m)
- Must handle remaining elements after one array exhausted
- Used as subroutine in Merge Sort algorithm

---

### 3. Array Rotation ⭐ MULTIPLE APPROACHES

**Problem:** Rotate array right by k positions

**Example:**
```
arr = [1, 2, 3, 4, 5], k = 2
Result: [4, 5, 1, 2, 3]
```

**Approach 1: Using Slicing (Pythonic)**
```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n
    return arr[-k:] + arr[:-k]
```
- **Time:** O(n), **Space:** O(n)
- Creates new array
- Simple and readable

**Approach 2: Reversal Algorithm (Space Efficient)**

**Magic Formula:** Three reversals
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements

**Example:**
```
arr = [1, 2, 3, 4, 5], k = 2

Step 1: Reverse all
[5, 4, 3, 2, 1]

Step 2: Reverse first k=2
[4, 5, 3, 2, 1]

Step 3: Reverse remaining 3
[4, 5, 1, 2, 3] ✓
```

**Code Pattern:**
```python
def rotate_array_reversal(arr, k):
    n = len(arr)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)   # Reverse all
    reverse(0, k - 1)   # Reverse first k
    reverse(k, n - 1)   # Reverse rest
    return arr
```
- **Time:** O(n), **Space:** O(1)
- In-place modification
- More space-efficient

**Important:** Always use `k = k % n` to handle cases where `k > n`

---

### 4. LeetCode Patterns Learned

**Pattern 1: Array Interleaving (Shuffle)**
- Problem: Rearrange array by alternating between two halves
- Key insight: Use index math `2*i` and `2*i+1` for positioning

**Pattern 2: Comparison with Max (Kids with Candies)**
- Find global maximum first
- Compare each element against this maximum
- Simple O(n) pattern for "can reach maximum" problems

**Pattern 3: Count Pairs (Good Pairs)**
- Nested loop pattern: `for i` then `for j from i+1`
- Ensures `i < j` without double counting
- O(n²) brute force, can optimize with hash map

---

### 5. Time & Space Complexity Summary - Day 3

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Remove duplicates (set) | O(n) | O(n) | Set stores unique elements |
| Merge sorted arrays | O(n+m) | O(n+m) | Result array |
| Rotate (slicing) | O(n) | O(n) | Creates new array |
| Rotate (reversal) | O(n) | O(1) | In-place, 3 reversals |
| Shuffle array | O(n) | O(n) | Index math pattern |
| Good pairs (brute force) | O(n²) | O(1) | Nested loops |

---

### 6. Key Operations Practiced

1. **Remove duplicates** using set (ex11)
2. **Merge sorted arrays** with two pointers (ex12) ⭐
3. **Rotate array** with reversal algorithm (ex13) ⭐
4. **Shuffle array** with index math (LC #1470)
5. **Kids with candies** - comparison pattern (LC #1431)
6. **Good pairs** - nested loop pattern (LC #1512)

---

### 7. Important Patterns to Remember

**Two-Pointer Merge:**
```python
i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1
result.extend(arr1[i:])
result.extend(arr2[j:])
```

**Array Rotation (Slicing):**
```python
k = k % len(arr)
return arr[-k:] + arr[:-k]
```

**Array Interleaving:**
```python
for i in range(n):
    result[2*i] = nums[i]        # Even positions
    result[2*i + 1] = nums[i+n]  # Odd positions
```

**Nested Loop for Pairs:**
```python
count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if condition:
            count += 1
```

---

### 8. Algorithm Analysis Tips

**Space Complexity Questions to Ask:**
1. Am I creating a new array/structure that grows with input? → O(n)
2. Am I only using a few variables regardless of input size? → O(1)
3. Am I modifying in-place? → O(1)

**Time Complexity Questions to Ask:**
1. How many times do I visit each element?
2. Are there nested loops? → Usually O(n²)
3. Do I process each element once? → Usually O(n)

---

### 9. Edge Cases to Always Consider

- **Empty array:** `[]`
- **Single element:** `[5]`
- **All duplicates:** `[1, 1, 1, 1]`
- **No duplicates:** `[1, 2, 3, 4]`
- **k > array length:** Handle with `k = k % n`
- **k = 0:** No rotation needed
- **Different length arrays:** When merging

---