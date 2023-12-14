#Mine
def nextGreatestLetter(letters,target):
    start,end = 0, len(letters)-1
    if target >= letters[-1] : return letters[0]
    n = len(letters)
    while start <= end:
        mid = (start + end) // 2

        if letters[mid] == target and letters[mid] != letters[mid+1]:
            return letters[mid+1]
        
        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start]
#Kunal
def nextGreatestLetter(letters,target):
    start,end = 0, len(letters)-1
    n = len(letters)
    while start <= end:
        mid = (start + end) // 2
        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % n]

if __name__ == '__main__':
    letters,target = ['c','f','j'], 'a'
    print(nextGreatestLetter(letters,target))
    letters,target = ['c','f','j'], 'c'
    print(nextGreatestLetter(letters,target))
    letters,target = ['x','x','y','y'], 'z'
    print(nextGreatestLetter(letters,target))
    letters,target = ['c','f','j'], 'd'
    print(nextGreatestLetter(letters,target))
    letters,target = ["e","e","e","e","e","e","n","n","n","n"], 'e'
    print(nextGreatestLetter(letters,target))
    letters,target = ["e","e","e",'e','n','o'], 'e'
    print(nextGreatestLetter(letters,target))
    