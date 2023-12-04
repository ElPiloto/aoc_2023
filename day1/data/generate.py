from absl import app
import string
import random

import numpy as np


digit_strs = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
word_for_digit = {str(v): k for k,v in digit_strs.items()}


def generate_solved_problem(
    min_start_len: int = 5,
    max_start_len: int = 10,
    number_flip_prob: float = 0.2,
    word_flip_prob: float = 0.5,

) -> tuple[str, int, int, int]:
  """."""
  start_len = np.random.randint(min_start_len, max_start_len+1)
  base = random.choices(string.ascii_letters[:26], k=start_len)
  num_numbers = 0
  #  We need at least two numbers to form a valid problem
  while (num_numbers < 2):
    number_slots = np.random.rand(start_len) <= number_flip_prob
    num_numbers = number_slots.sum()
  number_indices = np.argwhere(number_slots).squeeze()
  numbers = random.choices(string.digits, k=num_numbers)
  # technically, we should check that the characters before first do not spell
  # out a word. Same for the characters after the last.
  first = numbers[0]
  last = numbers[-1]
  for i, n in zip(number_indices, numbers, strict=True):
    base[i] = n
  # "render" final string
  final = []
  for i, c in enumerate(base):
    if number_slots[i] and np.random.rand() >  word_flip_prob:
      final += word_for_digit[c]
    else:
      final += c
  return final, first, last, num_numbers


def main(argv):
  del argv
  counts = []
  num_numbers = []
  for i in range(100000):
    puzzle, first, last, num = generate_solved_problem(max_start_len=20)
    print(puzzle, first, last)
    counts.append(len(puzzle))
    num_numbers.append(num)
  print(f'Min count: = {min(counts)}')
  print(f'Max count: = {max(counts)}')
  print(f'Min num_numbers: = {min(num_numbers)}')
  print(f'Max num_numbers: = {max(num_numbers)}')


if __name__ == "__main__":
  app.run(main)
str_digits
