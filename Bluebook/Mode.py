# Kishan Suhi
# Bluebook 
# Mode

import statistics

data = []
while True:
    num = int(input())
    if num == -1:
        break
    data.append(num)

modes = statistics.multimode(data)
modes.sort()

for mode in modes:
    print(mode)
