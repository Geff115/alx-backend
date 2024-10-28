#!/usr/bin/env python3
"""
This script creates a method named get_hyper that takes the same
arguments as get_page and returns a dictionary containing
key-value pairs.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """This method provides more information about the
        paginated data.
        """
        # Getting the data for the requested page
        data = self.get_page(page, page_size)

        # Calculating the total number of pages
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # return a dictionary with the correct pagination metadata
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
