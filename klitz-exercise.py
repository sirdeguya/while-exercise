def countstep(startnum) :
    countnum = 0
    printer = ""
    while startnum > 1 :
        if startnum % 2 == 0 :
            startnum = int(startnum / 2)
        else :
            startnum = startnum * 3 + 1
        countnum = countnum + 1
    return countnum

num = 1 
largest = 1
while num <= 1000 :
    countstepnum = countstep(num)
    if countstepnum > largest :
        largestnum = num
        largest = countstepnum
    num = num + 1
print(f' המספר שצריך הכי הרבה צעדים הוא {largestnum} עם {largest} צעדים')
