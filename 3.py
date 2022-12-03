import os
pwd = os.path.dirname(__file__)

def main():
    sum = 0
    sum2 = 0
    for x in procInput():
        sum += getPriority(x[0].intersection(x[1]).pop())
    print(sum)
    for x in procInput2():
        sum2 += getPriority(x.pop())
    print(sum2)
    return sum

def getPriority(item):
    if(item >= 'a' and item <= 'z'):
        return ord(item) - ord('a') + 1
    if(item >= 'A' and item <= 'Z'):
        return ord(item) - ord('A') + 27

def procInput():
    with open(pwd+"\\inputs\\input3.txt", "r") as f:
        lines = f.readlines()
    return [[set(x[0:len(x)//2]), set(x[len(x)//2:-1])] for x in lines]

def procInput2():
    with open(pwd+"\\inputs\\input3.txt", "r") as f:
        lines = f.readlines()
    arr = []
    for x in lines:
        if(lines.index(x) % 3 == 0):
            arr.append(set(x[0:-1]).intersection(set(lines[lines.index(x)+1][0:-1]).intersection(set(lines[lines.index(x)+2][0:-1]))))
    return arr
if __name__ == "__main__":
    main()