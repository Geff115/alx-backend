#!/usr/bin/env python3
"""
This script creates a method named get_page that takes
two integer arguments page with default value 1 and page_size
with default value 10.
"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List:
        """This method will use index_range to calculate the
        start and end indices for slicing the dataset and return
        the correct page of data, else it returns an empty list.
        """
        # Ensuring that page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # calling the index_range function to get the indexes
        start_index, end_index = index_range(page, page_size)

        # loading the data if it's not already loaded
        dataset = self.dataset()

        # Return the appropriate slice or an empty list if out of range
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
