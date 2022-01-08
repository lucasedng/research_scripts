from typing import List
from numpy import array
from re import compile

import re


def name_request_from_web(site_return: str) -> str:

    initial_str = '<a NAME="NAME"><STRONG>NAME</STRONG></a><br>'
    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + \
        site_return[initial_index:].find(final_str)

    return site_return[initial_index:final_index]


def dimension_request_from_web(site_return: str) -> int:

    if '<a NAME="DIMENSION"><STRONG>DIMENSION</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="DIMENSION"><STRONG>DIMENSION</STRONG></a><br>'
    elif '<a NAME="DIM"><STRONG>DIM</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="DIM"><STRONG>DIM</STRONG></a><br>'
    else:
        return -1

    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + site_return[initial_index:].find(final_str)

    return int(site_return[initial_index:final_index])


def determinant_request_from_web(site_return: str) -> float:

    if '<a NAME="DET"><STRONG>DET</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="DET"><STRONG>DET</STRONG></a><br>'
    else:
        return -1.0

    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + site_return[initial_index:].find(final_str)

    return float(site_return[initial_index:final_index])


def minimal_norm_request_from_web(site_return: str) -> float:

    if '<a NAME="MINIMAL_NORM"><STRONG>MINIMAL_NORM</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="MINIMAL_NORM"><STRONG>MINIMAL_NORM</STRONG></a><br>'
    else:
        return -1.0

    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + site_return[initial_index:].find(final_str)

    return float(site_return[initial_index:final_index])


def kissing_number_request_from_web(site_return: str) -> float:

    if '<a NAME="KISSING_NUMBER"><STRONG>KISSING_NUMBER</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="KISSING_NUMBER"><STRONG>KISSING_NUMBER</STRONG></a><br>'
    else:
        return -1

    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + site_return[initial_index:].find(final_str)

    return int(site_return[initial_index:final_index])


def gram_matrix_request_from_web(site_return: str) -> List[List[float]]:

    if '<a NAME="GRAM"><STRONG>GRAM</STRONG></a><br>' in site_return:
        initial_str = '<a NAME="GRAM"><STRONG>GRAM</STRONG></a><br>'
    else:
        return [[]]

    final_str = '<br><p><li>'

    initial_index = site_return.find(initial_str)+len(initial_str)
    final_index = initial_index + site_return[initial_index:].find(final_str)

    numeric_const_pattern = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
    rx = compile(numeric_const_pattern, re.VERBOSE)

    numbers = [
        float(s)
        for s in rx.findall(site_return[initial_index:final_index])
    ]
    num_row = int(numbers[0])
    num_columns = int(numbers[1])

    gram_matrix = array(numbers[2:]).reshape(num_row, num_columns)

    return gram_matrix.tolist()
