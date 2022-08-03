
def hanoi(disks, from_, to_, by_):
    if(disks == 1):
        print(from_,to_)
    else:
        hanoi(disks-1, from_, by_, to_)
        print(from_,to_)
        hanoi(disks-1, by_, to_, from_)

n = int(input())
print(2**n-1)
hanoi(n,1,3,2)