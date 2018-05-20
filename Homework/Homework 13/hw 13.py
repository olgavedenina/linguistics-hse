import os
import collections

start_path = '.'

d = {}

for root, dirs, files in os.walk(start_path):
    for f in files:
        base, ext = os.path.splitext(f)
        if ext in d:
            d[ext] += 1
        else:
            d[ext] = 1

max_count = max(d.values())
result = [k for k, v in d.items() if v == max_count]

print('Самое часто встречаемое разрешение в данной папке: ', result)
