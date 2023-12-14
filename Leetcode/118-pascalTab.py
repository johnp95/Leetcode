def generate(numRows):
    table = [[]]*(numRows+1)
    table[0] = [1]
    table[1] = [1,1]
    ans = [table[0], table[1]]
    if numRows > 2:
        for i in range(1,len(table)):
            if i+1 <= numRows:
                table[i+1] = [1] + [ sum(table[i][j:j+2]) for j in range(len(table[i])-1)] + [1]
    return table[:numRows]

if __name__ == '__main__':            
    res = generate(5)
    print(res)