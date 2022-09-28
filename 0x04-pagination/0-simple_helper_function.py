#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    function should return a tuple of size two containing
     a start index and an end index corresponding
      to the range of indexes to return in a list
      for those particular pagination parameters.
    """
    if page and page_size:
        start_idx = (page - 1) * page_size
        end_page = start_idx + page_size
    return start_idx, end_page
