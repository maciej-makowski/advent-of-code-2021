# %%
from assertpy import assert_that

def solve_day2_task1(input_path: str) -> int:
  position = 0
  depth = 0
  with open(input_path, "r") as file:
    for line in file:
      [command, distance] = line.split(" ")
      num_distance = int(distance)

      if command == "forward":
        position += num_distance
      elif command == "up":
        depth -= num_distance
      elif command == "down":
        depth += num_distance
      else:
        raise Exception(f"Invalid line: {line}")

  return position * depth
    

assert_that(solve_day2_task1("data/day2.example.txt")).is_equal_to(150)


# %%
solve_day2_task1("data/day2.input.txt")


# %%
def solve_day2_task2(input_path: str) -> int:
  position = 0
  depth = 0
  aim = 0
  with open(input_path, "r") as file:
    for line in file:
      [command, distance] = line.split(" ")
      num_distance = int(distance)

      if command == "forward":
        position += num_distance
        depth += aim * num_distance
      elif command == "up":
        aim -= num_distance
      elif command == "down":
        aim += num_distance
      else:
        raise Exception(f"Invalid line: {line}")

  return position * depth
    

assert_that(solve_day2_task2("data/day2.example.txt")).is_equal_to(900)


# %%
solve_day2_task2("data/day2.input.txt")

