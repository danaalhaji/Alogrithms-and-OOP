def countList(a, count = 0):
    print(count)
    # print(a)
    if len(a) == 0:
        return count
    else:
        count+=1
        newArray = a[count-1 : ]
        return countList(newArray,count)

array = [1,2,3,4,5,6,7]
print(countList(array))