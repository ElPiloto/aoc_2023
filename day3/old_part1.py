from absl import app
import numpy as np
import string


fname = 'example.txt'
with open(fname, 'r') as f:
  lines = [l.strip() for l in f.readlines()]
width = len(lines[0])
height = len(lines)

numbers = np.zeros(shape=(height, width), dtype=np.int32)
symbols_locs = []


def is_digit(x):
  return x in string.digits


def is_symbol(x):
  return x in '*#$+'


def get_number(line, start_pos):
  pass

h = 0
for l in lines:
  w = 0
  while w < width:
    c = l[w]
    if is_digit(c):
      numbers[h, w] = int(c)
    elif is_symbol(c):
      symbols_locs.append([h, w, c])
    w += 1
  h += 1
print(numbers)
print(symbols_locs)
for l in lines:
  print(l)


def main(argv):
  del argv


if __name__ == "__main__":
  app.run(main)

