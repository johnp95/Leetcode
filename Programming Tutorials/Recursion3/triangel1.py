def func(r,c):
    if r == 0  : return   
    if c < r:
        print('*',end="")
        func(r,c+1)
    else:
        print()
        func(r-1,0)

if __name__ == '__main__':
    func(4,0)