#!/usr/bin/env python3
"""
iA module for  Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_list

    Args:
        input_list (float: The float argument

    Returns:
        floats: The list of floats
    """
    return sum(mxd_lst)