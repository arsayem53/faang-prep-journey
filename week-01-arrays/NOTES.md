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
