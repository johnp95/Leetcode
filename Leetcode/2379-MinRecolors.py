blocks = 'WBBWWBBWBW'
blocks = 'WBWBBBW'
blocks = 'BWWWBB'
blocks = list(blocks)

k = 6
min_ops = float('inf')
for i in range(len(blocks)-k+1):
    sub = blocks[i:i+k]
    min_ops = min(min_ops,sub.count('W'))
print(min_ops)