# manual_sort.py
from typing import List, Dict, Any

def sort_dicts_by_key_manual(dicts: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Manual stable sort using insertion sort (for demonstration).
    Good for small lists; O(n^2) worst-case.
    """
    arr = list(dicts)  # copy to avoid mutation
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        current_key = current.get(key, None)
        while j >= 0:
            j_key = arr[j].get(key, None)
            # Compare with None handling
            if reverse:
                cond = (j_key is None) or (current_key is not None and current_key > j_key)
            else:
                cond = (j_key is None) or (current_key is not None and current_key < j_key)
            if cond:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = current
    return arr
