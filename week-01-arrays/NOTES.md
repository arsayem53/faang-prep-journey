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