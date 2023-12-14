def subSeq1(input_str,current='',index=0):
    if index == len(input_str):
        if current:
            print(current)
        return
    subSeq1(input_str,current+input_str[index],index+1)
    subSeq1(input_str,current,index+1)
    
def subSeq2(current,input_str):
    if len(input_str)==0:
        print(current)
        return
    ch = input_str[0]
    subSeq2(current+ch,input_str[1:])
    subSeq2(current,input_str[1:])

def subSeqArray(current,input_str):

    if len(input_str) ==  0:
        return [current] if current else []
    ch = input_str[0]
    left = subSeqArray(current+ch,input_str[1:])
    right = subSeqArray(current,input_str[1:])
    return left + right
def subSeqArray2(input_str,current='',idx=0):

    if idx == len(input_str):
        return [current] if current else []
    
    left = subSeqArray2(input_str,current+input_str[idx],idx+1)
    right = subSeqArray2(input_str,current,idx+1)
    return left + right
def findAscii(input_str,current="",idx=0):
    if idx == len(input_str):
        if current:
            print(current)
        return
    findAscii(input_str,current+input_str[idx],idx+1)
    findAscii(input_str,current,idx+1)
    findAscii(input_str,current+str(ord(input_str[idx])),idx+1)
    
if __name__ == '__main__':
    s = 'abc'
    subSeq1(s)
    # subSeq2('',s)
    findAscii(s)
