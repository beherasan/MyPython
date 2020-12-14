## Input n : Number of elements in an array
## Input x : The array used to calculate Q1, Q2, and Q3

def median(lst):
    if len(lst)%2 == 0:
        return (lst[(len(lst)//2)-1] + lst[len(lst)//2])/2
    else:
        return lst[len(lst)//2]

n = int(input())
x = list(map(int, input().rstrip().split()))

x.sort()

q2 = median(x)

if len(x)%2 != 0:
    end = (len(x)//2)
    q1 = median(x[0:end])
    q3 = median(x[end+1:])
else:
    end = (len(x)//2)
    q1 = median(x[:end])
    q3 = median(x[end:])

print (int(q1))
print (int(q2))
print (int(q3))
