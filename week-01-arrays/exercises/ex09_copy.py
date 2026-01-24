# ex09_copy.py
"""
Exercise 8: Understand shallow vs deep copy through experiments
"""
import copy
def demonstrate_shallow_copy():
    """Demonstrates shallow copy behavior."""
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    shallow_copied = copy.copy(original)
    print("Original before modification:", original)
    print("Shallow copied before modification:", shallow_copied)

    
    shallow_copied[0][0] = 99
    print("Original after modifying shallow copy:", original)
    print("Shallow copied after modification:", shallow_copied)

def demonstrate_deep_copy():
    """Demonstrates deep copy behavior."""
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    deep_copied = copy.deepcopy(original)
    print("Original before modification:", original)
    print("Deep copied before modification:", deep_copied)

    
    deep_copied[0][0] = 88
    print("Original after modifying deep copy:", original)
    print("Deep copied after modification:", deep_copied)

demonstrate_shallow_copy()
demonstrate_deep_copy()