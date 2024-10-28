#!/usr/bin/env python3
"""
This script creates a function named index_range
that takes two arguments page and page size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    ARGS:
        - page: current page number, starting from 1.
        - page_size: number of items in a page

    RETURN: a tuple of a start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
