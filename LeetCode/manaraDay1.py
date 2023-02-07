'''
Given two strings s and t, 
both consisting of lowercase English letters and digits
, your task is to calculate how many ways exactly one digit could be
removed from one of the strings so that s is lexicographically smaller
than t after the removal. Note that we are removing only a single instance 
of a single digit, rather than all instances (eg: removing 1 from the string
a11b1c could result in a1b1c or a11bc, but not abc).
Also note that digits are considered lexicographically smaller than letters.
'''
def solution(s, t):
    counts=0
    countT=0
    count=0
    temps=s
    tempt =t
    if (s[0].isalpha() and t[0].isalpha()) and (s[0] < t[0]):
        return 0
    for i in range(0 , len(s)-1):
        if s[i].isnumeric():
            temps.replace(temps[i], "")
            if temps[0] < t[0]:
                counts+=1
                temps = s
    for i in range(0 , len(t)-1):
        if t[i].isnumeric():
            tempt.replace(tempt[i], "")
            if s[0] < tempt[0]:
                countT+=1
                tempt = t
            
    count = counts + countT
    return count
def compareChar(sC, tC):
    if sC < tC:
        return True
