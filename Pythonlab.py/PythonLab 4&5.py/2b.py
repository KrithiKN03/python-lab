#cumulative sum
def csum(lst):
     s=0
     for n in range(len(lst)):
        s+=lst[n]
        lst[n]=s
     return lst
test=[1,4,5]
print(csum(test))

