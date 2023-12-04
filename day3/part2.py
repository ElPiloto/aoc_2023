from absl import app
import numpy as np
import string


fname = 'example.txt'
fname = 'input.txt'
with open(fname, 'r') as f:
  lines = [l.strip() for l in f.readlines()]
width = len(lines[0])
height = len(lines)

numbers = np.zeros(shape=(height, width), dtype=np.int32)
ids = np.zeros(shape=(height, width), dtype=np.int32)
symbols_locs = []


def is_digit(x):
  return x in string.digits


def is_symbol(x):
  return x != '.' #in '*#$+'


def get_number(line, start_pos):
  digits = ''
  offset = 0
  while start_pos+offset < len(line):
    if is_digit(line[start_pos+offset]):
      digits += line[start_pos+offset]
      offset += 1
    else:
      break
  return digits


next_id = 1
h = 0
for l in lines:
  w = 0
  while w < width:
    c = l[w]
    if is_digit(c):
      digits = get_number(l, w)
      number = int(digits)
      size = len(digits)
      for i in range(size):
        numbers[h, w+i] = int(digits)
        ids[h, w+i] = next_id
      next_id += 1
      w += size-1
    elif is_symbol(c):
      symbols_locs.append([h, w, c])
    w += 1
  h += 1


def inbounds(y, x):
  return y >= 0 and x >= 0 and x < width and y < height


part_numbers = []
for h, w, c in symbols_locs:
  if c != '*':
    continue
  gear_parts = []
  used_ids = [0]
  for dx in [-1, 0, 1]:
    x = w + dx
    for dy in [-1, 0, 1]:
      y = h + dy
      #print(y, x, numbers[y, x], ids[y, x], ids[y,x] in used_ids)
      if not inbounds(y, x):
        continue
      if ids[y, x] not in used_ids:
        gear_parts.append(numbers[y, x])
        used_ids.append(ids[y, x])
      else:
        print(f'Skipping id: {ids[y,x]}')
  if len(gear_parts) == 2:
    part_numbers.append(gear_parts[0] * gear_parts[1])

print(numbers)
print(ids)
print(symbols_locs)
print(part_numbers)
for l in lines:
  print(l)
print(sum(part_numbers))


def main(argv):
  del argv


if __name__ == "__main__":
  app.run(main)

