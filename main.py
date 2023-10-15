import csv

def isValid(a,b,c,d,e):
    tempVar = [a,b,c,d,e]

    for i in range(5):
        for other in range(5):
            if i != other:
                if tempVar[i] == tempVar[other]:
                    return False

    return True

def saveToFile(arr):
    with open("GeneratedNums.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for i in range(len(arr)):
            writer.writerow(arr[i])


def generateNumbers():
    pbNums = [1,2,3,4,5,6,1]
    arrPBnums = [pbNums,[1,2,3,4,5,6,2]]

    intgennums = 2

    print(arrPBnums)
    for a in range(1,51):
        for b in range(1,51):
            for c in range(1,51):
                for d in range(1,51):
                    for e in range(1,51):
                        for f in range(1,51):
                            for i in range(1,21):
                                if isValid(a,b,c,d,e):
                                    arrPBnums.append([a, b, c, d, e, f, i])
                                    intgennums+=1
                                    print(intgennums)
                        saveToFile(arrPBnums)
                        arrPBnums.clear()

    print(arrPBnums)

if __name__ == '__main__':
    generateNumbers()