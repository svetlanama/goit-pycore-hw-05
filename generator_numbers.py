import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"(?<=\s)(\d+\.\d+)(?=\s)"
    for match in re.finditer(pattern, f" {text} "):
        yield float(match.group(1))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text)) 