# 📚 Key Learnings & Insights

A collection of important concepts, patterns, and "aha!" moments from the journey.

---

## Week 1: Arrays

### Day 1: Array Basics (Jan 21, 2026)

**Core Concepts:**
- Arrays store elements in contiguous memory → O(1) access by index
- Python lists are dynamic arrays (can grow/shrink)
- Linear operations (traverse, search, sum, max/min) are always O(n)
- Access is fast, modification (insert/delete middle) is slow

**Key Pattern Learned:**
```python
# Linear search pattern
for i in range(len(arr)):
    if arr[i] == target:
        return i
return -1
```

**Important Insight:**
> Even if an operation *seems* simple (like finding max), if it requires checking every element, it's O(n). There's no way around traversal for unsorted arrays.

**LeetCode Problems:**
- #1929: Concatenation - learned array building, LeetCode class format

---

### Day 2: Array Manipulation (Jan 22, 2026)

**Core Concepts:**
- Two-pointer technique: use two indices moving toward each other
- In-place algorithms: modify original to save space (O(1) vs O(n))
- Shallow copy vs deep copy: shallow fails with nested structures
- Insert/delete are O(n) due to element shifting

**Key Patterns Learned:**

1. **Two-Pointer (Reverse):**
```python
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

2. **Prefix Sum (Running Sum):** ⭐
```python
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
```

3. **2D Array Traversal:**
```python
for row in matrix:
    for element in row:
        # process element
```

**Important Insights:**
> Two pointers = indices (positions), not values. This was a key mental shift.

> Prefix sum pattern appears in hundreds of problems - it's foundational for range queries and subarray problems.

> Space complexity: Ask "Am I creating new data structures that grow with input size?" If no → O(1), if yes → O(n).

**The O(n) Pain:**
> Manually implementing insert/delete with element shifting made me *feel* why these operations are expensive. Understanding comes from doing, not just reading.

**LeetCode Problems:**
- #1480: Running Sum - mastered prefix sum pattern
- #1672: Richest Customer - learned 2D array iteration

**Code Quality Improvements:**
- Using `for element in arr` instead of `for i in range(len(arr))`
- Leveraging built-ins: `max()`, `sum()`, `enumerate()`
- Separating concerns: parameters instead of `input()` inside functions
- Avoiding variable names that shadow built-ins (`sum`, `min`, `max`)

---

## Patterns to Remember

### 1. Two-Pointer (Converging)
**Use for:** Reverse, palindrome, two sum (sorted), remove duplicates
```python
left, right = 0, len(arr) - 1
while left < right:
    # process arr[left] and arr[right]
    left += 1
    right -= 1
```

### 2. Prefix Sum / Running Sum
**Use for:** Range queries, subarray sums, cumulative operations
```python
for i in range(1, n):
    arr[i] = arr[i-1] + arr[i]
```

### 3. Linear Search
**Use for:** Finding element in unsorted array
```python
for i in range(len(arr)):
    if arr[i] == target:
        return i
return -1
```

---

## Mistakes & Lessons

1. **Typo cost:** `custmer` instead of `customer` → Always proofread before submit
2. **LeetCode format:** Forgot `class Solution:` → Remember platform requirements
3. **Space complexity confusion:** Initially unclear why reverse is O(1) → Now clear: in-place modification uses constant extra memory
4. **Indices vs values:** Confused pointer indices with array values → Two pointers = positions in array

---

## Time Complexity Quick Reference

| Operation | Time | Why |
|-----------|------|-----|
| Access arr[i] | O(1) | Direct memory calculation |
| Search unsorted | O(n) | Must check each element |
| Insert/Delete middle | O(n) | Must shift elements |
| Reverse (two-pointer) | O(n) | Visit n/2 pairs |
| Prefix sum | O(n) | Single pass through array |
| 2D traversal | O(m×n) | Visit every element |

---

## Wisdom Gained

> "Understanding comes from implementing, not just reading. The O(n) pain of insert/delete was abstract until I manually shifted elements."

> "Patterns like prefix sum and two-pointer are tools. The more problems I solve, the better I recognize when to use each tool."

> "Clean code matters: Pythonic iteration, meaningful names, separation of concerns. These habits compound over time."

---

Last Updated: Day 2, Jan 22, 2026