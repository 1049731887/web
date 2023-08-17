import random

random_sequence = list(range(0, 400))
random.shuffle(random_sequence)

# 将随机序列按[1, 2, 3, ...]格式输出
output = "[" + ", ".join(map(str, random_sequence)) + "]"

print(output)
