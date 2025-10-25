# ai_suggested_sort.py
from typing import List, Dict, Any

def sort_dicts_by_key(dicts: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sort a list of dictionaries by `key`. Non-existent keys are treated as None.
    Returns a new sorted list (does not mutate the input).
    """
    return sorted(dicts, key=lambda d: d.get(key, None), reverse=reverse)
