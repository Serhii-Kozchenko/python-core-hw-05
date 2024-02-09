from typing import Callable
import re

text = "10.01 Загальний дохід працівника 1000 складається 1000.15з декількох частин: 1000.05 як основний дохід,n\
        доповнений додатковими надходженнями 27.05 і 324.05 доларів 10.01." 


def generator_numbers(text: str):
    pattern = r"(?<=\s)\d+\.\d+(?=\s)"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

   
def sum_profit(text: str, func: Callable):
    total_sum = 0
    for i in func(text):
        total_sum+=i
    return round(total_sum,2)
   

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

