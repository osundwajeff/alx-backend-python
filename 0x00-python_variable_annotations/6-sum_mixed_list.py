#!/usr/bin/env python3
""" Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """computes sum of a list of integers and floats numbers"""
    return sum(mxd_list)
