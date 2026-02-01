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
### Day 3: Array Operations (Jan 23, 2026)

**Core Concepts:**
- Remove duplicates using hash set for O(n) time
- Two-pointer merge for sorted arrays (Merge Sort foundation!)
- Array rotation: slicing (simple) vs reversal (space-efficient)
- Index math for array rearrangement problems

**Key Patterns Learned:**

1. **Two-Pointer Merge (Different from Day 2!):**
```python
# Day 2: Converging pointers (reverse)
left, right = 0, len(arr)-1
while left < right:
    # Process and move toward each other

# Day 3: Parallel pointers (merge)
i = j = 0
while i < len(arr1) and j < len(arr2):
    # Compare and advance one pointer
# Don't forget remaining elements!
```

2. **Array Rotation (Reversal):**
```python
# Three magical reversals
reverse(0, n-1)   # All
reverse(0, k-1)   # First k
reverse(k, n-1)   # Rest
# Result: rotated by k!
```

3. **Index Math for Interleaving:**
```python
# Pattern for alternating elements
for i in range(n):
    result[2*i] = first_half[i]
    result[2*i + 1] = second_half[i]
```

**Important Insights:**

1. **Merge Algorithm Revelation:**
   - This is THE algorithm used in Merge Sort!
   - Two sorted arrays → one sorted array in O(n+m) time
   - Critical to remember: copy remaining elements after one exhausts

2. **Multiple Valid Solutions:**
   - Rotation: slicing (O(n) space, simple) vs reversal (O(1) space, clever)
   - Trade-offs between simplicity and efficiency
   - In interviews, discuss both approaches!

3. **k % n Pattern:**
   - Rotating by k when k > n is same as rotating by k % n
   - Always normalize k first: `k = k % len(arr)`
   - Prevents out-of-bounds errors

4. **Nested Loops for Pairs:**
   - `for i` then `for j from i+1` ensures i < j
   - Prevents double-counting: (0,3) counted, not (3,0)
   - O(n²) brute force, can optimize with hash map (future skill)

**LeetCode Problems:**

- **#1470: Shuffle Array** - learned index math pattern for interleaving
- **#1431: Kids with Candies** - simple max comparison pattern
- **#1512: Good Pairs** - nested loop for pair counting

**Mistakes & Lessons:**

1. **Forgot remaining elements in merge:** After while loop, one array still has elements!
   - Fix: `result.extend(arr1[i:])` and `result.extend(arr2[j:])`

2. **Didn't handle k > n in rotation:** Led to negative indexing errors
   - Fix: Always `k = k % len(arr)` first

3. **Confused rotation direction:** Right rotation = move last k to front
   - Visualization helped solidify this

**Code Comparison - Merge Algorithm:**
```python
# ❌ My first attempt (buggy)
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        # comparison logic
    return result  # Missing remaining elements!

# ✅ Correct version
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        # comparison logic
    result.extend(arr1[i:])  # Copy remaining
    result.extend(arr2[j:])  # Copy remaining
    return result
```

**Patterns Now in Arsenal:**

1. Two-pointer (converging) - for reverse, palindrome
2. Two-pointer (merge) - for combining sorted arrays
3. Prefix sum - for range queries
4. Hash set - for deduplication
5. Array rotation - for circular shift problems
6. Index math - for rearrangement problems
7. Nested loops - for pair counting (O(n²) baseline)

**Wisdom Gained:**

"The reversal algorithm seemed like magic until I traced it 5 times. Now I see it's just clever manipulation of array sections. Understanding comes from doing, not just reading."

"Merge algorithm is everywhere! Merge Sort, merging results, combining sorted lists. This O(n+m) pattern is foundational."

"Trade-offs matter: slicing is simple, reversal is space-efficient. In interviews, discuss both approaches and ask about constraints."

---

Last Updated: Day 3, Jan 23, 2026

### Day 4: More Array Problems (Jan 24, 2026)

**Core Concepts:**
- Two-variable tracking for single-pass problems
- Write position pointer pattern
- Sequential comparison for sorted check
- Nested loops for pair/count problems

**Key Patterns Learned:**

1. **Two Variable Tracking:**
```python
# Track largest AND second largest simultaneously
largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest    # Old largest drops down
        largest = num
    elif num > second and num != largest:
        second = num
```

2. **Write Position Pattern ⭐ (Reusable!):**
```python
# Generic pattern — appears in MANY problems
write_pos = 0
for i in range(len(arr)):
    if should_keep(arr[i]):
        arr[write_pos] = arr[i]
        write_pos += 1
# Fill or truncate remaining
```

3. **Sequential Comparison:**
```python
# Check property between consecutive elements
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:   # Violation found
        return False
return True                  # No violations
```

**Important Insights:**

1. **Pattern Recognition Across Problems:**
   - Move zeros and remove duplicates use the SAME write position pattern
   - Only the condition changes: `!= 0` vs `not seen before`
   - This is how you get fast at interviews — recognize reusable patterns

2. **Initialization Is Everything:**
   - Wrong initial values cause subtle bugs
   - For "find max/min" type problems, use `float('-inf')` or `float('inf')`
   - For "seen" tracking, use empty set or None

3. **O(n²) Has Its Place:**
   - Not every problem needs optimal complexity
   - Nested loops are fine when constraints are small
   - But always think: "Can I do better?"

**Mistakes & Lessons:**
1. Typo `secoond_largest` — always proofread variable names
2. Wrong initialization `second = arr[0]` — think about what starting value makes sense
3. Missing duplicate check — `[10, 10, 10]` should return None for second largest

**Week 1 Patterns Arsenal (Complete):**
1. Two-pointer (converging) — reverse, palindrome
2. Two-pointer (merge) — merge sorted arrays
3. Prefix sum — range queries
4. Hash set — deduplication
5. Array rotation — slicing & reversal
6. Index math — interleaving
7. Nested loops — pair counting
8. Write position — move zeros, remove duplicates ⭐
9. Two variable tracking — second largest ⭐
10. Sequential comparison — is sorted

---

Last Updated: Day 4, Februay 1, 2026