from absl import app


digits = [str(i) for i in range(10)]
digit_strs = {
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

def find_digit_forward(line, pos) -> str | None:
  if line[pos] in digits:
    return line[pos]
  for word, digit in digit_strs.items():
    end_pos = len(word) + pos
    if end_pos > len(line):
      continue
    if line[pos:end_pos] == word:
      return str(digit)
  return None

def find_digit_backward(line, pos) -> str | None:
  if line[pos] in digits:
    return line[pos]
  for word, digit in digit_strs.items():
    start_pos = pos - len(word) + 1
    if start_pos < 0:
      continue
    if line[start_pos:pos+1] == word:
      return str(digit)
  return None


def solve(lines: tuple[str], should_print: bool = False):
  digits_per_line = []
  for l in lines:
    first = None
    last = None
    counter = 0
    while first is None:
      first = find_digit_forward(l, counter)
      counter += 1

    counter = len(l) - 1
    while last is None:
      last = find_digit_backward(l, counter)
      counter -= 1
    digits_per_line.append(int(first + last))
  answer = sum(digits_per_line)
  if should_print:
    print(answer)
  return answer

def load(fname: str = 'part1_input.txt') -> list[str]:
  with open(fname, 'r') as f:
    lines = f.readlines()
  lines = [l.strip() for l in lines]
  return lines


def main(argv):
  lines = load()
  solve(lines, True)


if __name__ == "__main__":
  app.run(main)

