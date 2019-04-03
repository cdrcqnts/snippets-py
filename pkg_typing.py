from typing import Dict, Union, List


ComplexType = Dict[str, Union[str, int]]


def func_param(a: int, b: str) -> None:
    print(str(a) + b)


def func_return() -> int:
    return 3


def func_return_complex() -> ComplexType:
    return {"a": "a_string", "b": 1}


def func_complex_list(a: str, b: Union[str, int]) -> List[ComplexType]:
    return [{"a": "a_string", "b": 1}]


func_param(1, ' two')