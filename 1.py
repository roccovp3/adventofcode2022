import os
pwd = os.path.dirname(__file__)
def main():
    print(max(getSums())) #part 1
    print(sum(getMaxN(getSums(), 3))) #part2
    return

def getSums():
    input = procInput()
    sums = [0]
    i = 0
    for x in input:
        if(x != -1):
            sums[i] += x
        else:
            sums.append(0)
            i += 1
    return sums

def getMaxN(sums, n):
    max3 = []
    for i in range(n):
        max3.append(max(sums))
        sums.remove(max(sums)) #python remove only removes first occurence, what we want
    return max3

def procInput():
    with open(pwd+"\\inputs\\input1.txt", "r") as f:
        lines = f.readlines()
        # for i, x in enumerate(lines):
        #     if(x != "\n" and "\n" in x):
        #         x = int(x[0:-1])
        #         input.append(x)
        #     else:
        #         input.append(-1)
    return [int(x) if x != "\n" and "\n" in x else -1 for x in lines]
        

if __name__ == "__main__":
    main()