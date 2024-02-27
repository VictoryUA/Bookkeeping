from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    
    # Finds a pair of elements in the list that sum up to the target value.
    # Time complexity: O(n^2)
    # Space complexity: O(1)
  
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return li[i], li[j]


assert find_sum(5, [1, 2, 3, 4, 5]) in {(1, 4), (2, 3)}

from typing import List, Tuple

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    
    # Finds a pair of elements in the list that sum up to the target value using a hash set.
    # Time complexity: O(n)
    # Space complexity: O(n)
    
    seen = set()
    for num in li:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)

assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(1, 4), (2, 3)}