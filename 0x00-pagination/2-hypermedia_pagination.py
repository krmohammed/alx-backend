#!/usr/bin/env python3
"""provides the function index_range
    and the class Server
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """index_range"""
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page with hypermedia"""
        dataset_got = self.get_page(page, page_size)
        if page_size > 0:
            total_pages = math.ceil(len(self.dataset()) / page_size)
        else:
            total_pages = 0
        next_page = page + 1 if (page + 1) <= total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_got),
            "page": page,
            "data": dataset_got,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
