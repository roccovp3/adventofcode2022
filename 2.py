import os
pwd = os.path.dirname(__file__)
def main():
    print(getScore2())
    return

def getScore():
    values = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    winPairs = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    losePairs = [["A", "Z"], ["B", "X"], ["C", "Y"]]
    drawPairs = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    total = 0
    for pair in procInput():
        if pair in winPairs:
            total += 6
        elif pair in drawPairs:
            total += 3
        total += values[pair[1]]
    return total

def getScore2():
    total = 0
    values = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    for pair in procInput():
        if pair[1] == "X":
            total += (values[pair[0]]-2) % 3 + 1
        elif pair[1] == "Z":
            total += (values[pair[0]]) % 3 + 1
            total += 6
        elif pair[1] == "Y":
            total += values[pair[0]]
            total += 3
    return total


def procInput():
    with open(pwd+"\\inputs\\input2.txt", "r") as f:
        lines = f.readlines()
        # for i, x in enumerate(lines):
        #     if(x != "\n" and "\n" in x):
        #         x = int(x[0:-1])
        #         input.append(x)
        #     else:
        #         input.append(-1)
    return [[x[0], x[2]] for x in lines]
        

if __name__ == "__main__":
    main()