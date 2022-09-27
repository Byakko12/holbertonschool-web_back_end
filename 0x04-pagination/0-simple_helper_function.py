#!/usr/bin/env python3

def index_range(page, page_size):

    if page and page_size:
        start_idx = (page - 1) * page_size
        end_page = start_idx + page_size
    return start_idx, end_page
