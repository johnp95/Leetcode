tests = []

tests.append({
    # original input  #0
    'input': {
    'nums': [4,5,6,7,0,1,2],
    'target': 0,
    },
    'output': 4
})
tests.append({
    # size 10 rotated 3 time #1
    'input': {
    'nums': [4,5,6,7,0,1,2],
    'target': 3,
    },
    'output': -1
})
tests.append({
    # never rotated #2
    'input': {
    'nums': [1],
    'target': 0
    },
    'output': -1
})
tests.append({
     #3
    'input': {
    'nums': [1],
    'target': 1,
    },
    'output': 0
})
tests.append({
    # rotated n-1 times #4
    'input': {
    'nums': [3,1],
    'target': 3
    },
    'output': 0
})
tests.append({
    # rotated n-1 times #4
    'input': {
    'nums': [3,1],
    'target': 1
    },
    'output': 1
})
tests.append({
    # rotated n-1 times #4
    'input': {
    'nums': [1,3],
    'target': 1
    },
    'output': 0
})
tests.append({
    # rotated n-1 times #4
    'input': {
    'nums': [1,3],
    'target': 3
    },
    'output': 1
})
# tests.append({
#     # rotated n times #5
#     'input': {
#     'nums': [2,3,4,5,6],
#     },
#     'output': 2
# })
# # tests.append({
# #     # empty
# #     'input': {
# #     'nums': [],
# #     },
# #     'output': 0
# # })
# tests.append({
#     # one element
#     'input': {
#     'nums': [1],
#     },
#     'output': 1
# })
