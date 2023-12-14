from collections import defaultdict

trees = [1,2,2,3,2]
# trees = [1,2,1]

# trees = [0,1,2,2]

treeTypesMap = {}
# treeTypesMap = defaultdict(lambda : 0 )
start, end, result = 0, 0, 0

while end < len(trees):
    treeTypesMap[trees[end]] = treeTypesMap.get(trees[end], 1) 
    # if trees[end] not in treeTypesMap:
    #     treeTypesMap[trees[end]] = 1
    # else:c
    #     treeTypesMap[trees[end]] += 1
    treeTypesMap[trees[end]] = 1
    print(f'outer -> {start} {end} {treeTypesMap}')
    end += 1
    while len(treeTypesMap) > 2:
        treeTypesMap[trees[start]] -= 1
        print(f'\tinner -> {start} {end} {treeTypesMap}')

        if treeTypesMap[trees[start]] == 0:
            del treeTypesMap[trees[start]]
        start += 1
        
    result = max(result, end - start)
   
print(result)



    

