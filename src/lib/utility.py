import os
from typing import Callable
from typing import TypeVar


__data_directory = os.path.join('.', 'src', 'data')

K = TypeVar('K')
V = TypeVar('V')


def merge_dict(
        overlap: Callable[[V, V], V],
        *args: tuple[dict[K, V]]
) -> dict[K, V]:
    '''combines all the dictionaries and calls the overlap function,
    when multiple dictionaries contain the same key'''
    result = dict()
    for dic in args:
        for key, val in dic.items():
            if key in result:
                result[key] = overlap(result[key], val)
            else:
                result[key] = val
    return result


def get_data_directory() -> str:
    '''returns the directory of data files'''
    return os.path.abspath(os.path.join('.', 'src', 'data'))


def read_raw_data(filename: str) -> str:
    '''reads the entire data file and returns it as a string'''
    assert isinstance(filename, str)
    filepath = os.path.join(get_data_directory(), filename)
    print(filepath)
    assert os.path.isfile(filepath)
    with open(filepath, 'r') as contents:
        data = contents.read()
    return data


def read_lines(filename: str) -> str:
    '''reads file and returns a list of strings based on new lines,
    strips empty lines'''
    lines = read_raw_data(filename).splitlines()
    return list(filter(lambda s: len(s) > 0, lines))
