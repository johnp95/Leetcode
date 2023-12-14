def generate_subsequences(nums):
    subsequences = [[]]

    for num in nums:
        # new_subsequences = 
        # for subseq in subsequences:
        #     new_subsequence = subseq + [num]
        #     new_subsequences.append(new_subsequence)
        subsequences += [sub+[num] for sub in subsequences]

    return subsequences

# Input list
nums = [1,2,32]

# Generate and print all subsequences in a 2D list
subsequences = generate_subsequences(nums)
print(subsequences)
