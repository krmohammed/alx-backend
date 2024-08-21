#!/usr/bin/env python3
"""provides the function index_range"""


def index_range(page, page_size):
    """index_range"""
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)
