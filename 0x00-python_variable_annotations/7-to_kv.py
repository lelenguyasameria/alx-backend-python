#!/usr/bin/env python3
"""
A module for  Complex types - string and int/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv

    Args:
        k (string: The fstring argument
        v (int OR float):

    Returns:
       tuple: The tuple
    """
    return k, pow(v, 2)