# %%
from typing import List

from assertpy import assert_that

def readlines_as_int(path: str) -> List[int]:
  input = []
  with open(path, "r") as file:
    for l in file.readlines():
      input.append(int(l))
  return input

def solve_day1_task1(data: List[int]) -> int:
  c = 0
  for i in range(1, len(data)):
    if data[i-1] < data[i]:
      c += 1
  return c

assert_that(solve_day1_task1(readlines_as_int("data/day1.example.txt"))).is_equal_to(7)


# %%
solve_day1_task1(readlines_as_int("data/day1.input.txt"))


# %%
from queue import Queue

def solve_day1_task2(data: List[int]) -> int:
  c = 0
  q = Queue(3)
  last_sum = sum(q.queue)
  
  for v in data[0:3]:
    q.put(v)

  for v in data[3:]:
    q.get()
    q.put(v)
    curr_sum = sum(q.queue)
    
    if (curr_sum > last_sum):
      c += 1
    
    last_sum = curr_sum
  
  return c

assert_that(solve_day1_task2(readlines_as_int("data/day1.example.txt"))).is_equal_to(5)


# %%
solve_day1_task2(readlines_as_int("data/day1.input.txt"))

