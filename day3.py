# %%
from assertpy import assert_that

def solve_day3_task1(input_path: str) -> int:
  ones = None
  total_lines = 0

  with open(input_path, "r") as file:
    for line in file:
      total_lines += 1
      if not ones:
        ones = [0] * (len(line) - 1)

      for i, c in enumerate(line):
        if c == '\n':
          break
        elif c == '1':
          ones[i] += 1

  bin_gamma = [1 if v/total_lines > 0.5 else 0 for v in ones]

  gamma = 0
  epsilon = 0

  for i, v in enumerate(bin_gamma):
    if v == 1:
      gamma += 2 ** (len(bin_gamma) - i - 1)
    else:
      epsilon += 2 ** (len(bin_gamma) - i - 1)

  return gamma * epsilon
    

assert_that(solve_day3_task1("data/day3.example.txt")).is_equal_to(198)


# %%
solve_day3_task1("data/day3.input.txt")


# %%
import functools

from array import array
from typing import List

def bin_to_number(bin_num: List[int]) -> int:
  return functools.reduce(
    lambda acc, x : acc + x,
    map(
      lambda v: v[1] * (2 ** (len(bin_num) - v[0] - 1)),
      enumerate(bin_num)
    ),
    0
  )

def solve_day3_task2(input_path: str) -> int:
  loaded = []
  
  with open(input_path, "r") as file:
    loaded = list(map(
      lambda line: list(map(
        lambda c0: 0 if c0 == '0' else 1,
        filter(
          lambda c1: c1 in ['0', '1'],
          line
        )
      )),
      file
    ))

    def find_number(
      pos: int,
      considered: List[int],
      keep_larger: bool
    ):
      if len(considered) == 1:
        return loaded[considered[0]]

      found = []
      for v in considered:
        arr = loaded[v]
        if arr[pos] == 1:
          found.append(v)

      if len(found) / len(considered) >= 0.5:
        if keep_larger:
          return find_number(pos+1, found, keep_larger)
        else:
          return find_number(pos+1, [i for i in considered if i not in found], keep_larger)
      elif len(found) / len(considered) < 0.5:
        if keep_larger:
          return find_number(pos+1, [i for i in considered if i not in found], keep_larger)
        else:
          return find_number(pos+1, found, keep_larger)
      
    o2_bin = find_number(0, list(range(len(loaded))), True)
    co2_bin = find_number(0, list(range(len(loaded))), False)
        
    o2 = bin_to_number(o2_bin)
    co2 = bin_to_number(co2_bin)

  return o2 * co2

assert_that(solve_day3_task2("data/day3.example.txt")).is_equal_to(230)


# %%
solve_day3_task2("data/day3.input.txt")
# %%
