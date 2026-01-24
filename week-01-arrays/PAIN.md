# Week 1 - Arrays
## Day 1: Pain Points and Learnings

### 1. Confusions / Challenges
- Initially thought Python list concatenation (`nums + nums`) might be faster than O(n). Realized it still traverses elements.  
- Struggled to understand why linear search for max or sum cannot be faster than O(n).  
- Printing vs returning results caused LeetCode submission errors.  
- Understanding LeetCode’s `Solution` class requirement was initially confusing.

### 2. Key Learnings
- Traversal is unavoidable; must accept O(n) for operations like sum, max, linear search.  
- Python list is dynamic but insertion/deletion in the middle is costly.  
- Always match LeetCode’s function signature and return value requirements.  
- Print statements are for local testing; platform judges check returned data.  
- Contiguous memory explains why access by index is fast (O(1)).

### 3. Notes for Next Steps
- Day 2 will cover insertion/deletion and array shifting costs.
- Keep practicing linear operations to build strong intuition.


## Day 2: Pain Points and Learnings

### 1. Confusions / Challenges
- Two-pointer concept initially unclear - confused indices (positions) with values
- Understanding space complexity: why reverse is O(1) space took time
- Shallow vs deep copy: Initially didn't understand when shallow copy fails
- Insert/delete operations: Manually implementing the shift logic was tedious but enlightening
- Small typo (`custmer` instead of `customer`) caused runtime error - reminder to proofread!
- Getting used to LeetCode's class format still feels slightly awkward

### 2. Breakthrough Moments
- **Two pointers clicked:** Realized it's just two indices moving toward each other - elegant!
- **The O(n) pain is real:** Manually shifting elements in insert/delete made me *feel* why it's expensive
- **Prefix sum pattern:** The formula `arr[i] = arr[i-1] + arr[i]` is so simple yet powerful
- **In-place saves space:** Understanding that modifying original uses O(1) vs O(n) for new array
- **Pythonic code:** Using `max(a, b)` and `sum(row)` makes code cleaner

### 3. Key Learnings
- Two pointers = **indices** (positions), not values themselves
- In-place algorithms trade off space for inability to recover original data
- Shallow copy only copies references - fails with nested structures
- Insert/delete are O(n) because of element shifting, not the operation itself
- Prefix sum is a pattern that appears in hundreds of problems - memorize it!
- 2D arrays: iterate with `for row in matrix` is cleaner than nested indices
- Space complexity = "Does my extra memory grow with input size?"

### 4. Code Quality Improvements
- Started using more Pythonic patterns (`for element in arr` instead of `for i in range`)
- Using `max()` and `sum()` built-ins instead of manual loops
- Better variable names (avoided shadowing built-ins like `sum`, `min`, `max`)
- Passing parameters instead of using `input()` inside functions - separation of concerns!

### 5. What Still Needs Practice
- Recognizing when to use two pointers vs other patterns
- More comfort with space complexity analysis
- Writing cleaner code on first attempt (less refactoring)
- Speed - some exercises took longer than estimated time

### 6. Notes for Next Steps
- Day 3 covers remove duplicates (two-pointer variation), merge sorted arrays, rotation
- Need to practice more two-pointer problems to build intuition
- Keep eye out for prefix sum pattern in future problems

### 7. Time Management
- Morning exercises: ~2 hours (as planned) ✅
- Afternoon LeetCode: ~1.5 hours (faster than expected!) ✅
- Understanding concepts: Taking time to really understand > rushing ✅