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
