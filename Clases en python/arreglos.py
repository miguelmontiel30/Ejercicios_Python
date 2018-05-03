a = [5,8,3]
print a 
a [2] = 6
print a  



b = [1000,500,15,9,65,90,30]
print b
tam = 7

for r in range(tam):  #Range -1
    for p in range (tam -1):
        if b[p] > b[p+1]:
            tmp = b[p]
            b[p] = b[p+1]
            b[p+1] = tmp

print b