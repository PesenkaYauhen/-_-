t = int(input())

for i in range(1, t + 1):
    sum = 0
    s = input()
    s1 = s.split(sep = ' ')

    n = int(s1[0])
    #print(n)
    b = int(s1[1])
    #print(b)
    for j in range(1, n+1):
        n1 = len(str(j))
        x = ""
        count = 0
        while n1 > 0:


           j_str = str(j)
           x1_i = int(j_str[count]) // b
           x1 = str(x1_i)
           #print(x1 +" после  деления")
           x += x1
           #print(count, "count")
           count += 1
           #print(count, "count")
           n1 -= 1
        #print(x, "получаемое число")
        x_int = int(x)
        y = j /b
        if x_int == y:
            sum += 1
    print(sum)