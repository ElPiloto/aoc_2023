

with open('part1_input.txt', 'r') as f:
  lines = f.readlines()

print(lines[-1])

digits = [str(i) for i in range(10)]
digits_per_line = []
for l in lines:
  first = None
  last = None
  counter = 0
  while first is None:
    if l[counter] in digits:
      first = l[counter]
    counter += 1

  counter = len(l) - 1
  while last is None:
    if l[counter] in digits:
      last = l[counter]
    counter -= 1
  digits_per_line.append(int(first + last))
print(sum(digits_per_line))
