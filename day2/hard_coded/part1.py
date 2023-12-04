import numpy as np

COLOR_ORDER = {'red': 0, 'green': 1, 'blue': 2}
MAX_COUNTS = np.array([12, 13, 14]) # red, green, blue

with open('input.txt', 'r') as f:
  lines = [l.replace('\n', '') for l in f.readlines()]

def consume_id(line) -> tuple[int, tuple[str]]:
  id, rest = line.split(': ')
  id = id.replace('Game ', '').replace(': ', '')
  rest = rest.split(';')
  return int(id), rest

def parse_sets(sets: tuple[str]):
  parsed_sets = []
  for s in sets:
    cubes = s.split(',')
    count = np.zeros_like(MAX_COUNTS)
    for color, idx in COLOR_ORDER.items():
      for cube in cubes:
        if color in cube:
          count[idx] = int(cube.replace(f'{color}', ''))
    parsed_sets.append(count)
  parsed_sets = np.stack(parsed_sets)
  return parsed_sets
  #return np.stack(parsed_sets)

ids_rest = list(map(consume_id, lines))

possible_ids = 0
for (id, rest) in ids_rest:
  set_counts = parse_sets(rest)
  if (set_counts <= MAX_COUNTS).all():
    possible_ids += id

print(possible_ids)
