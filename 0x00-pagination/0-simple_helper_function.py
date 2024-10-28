#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Return the start and end index for a given page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
