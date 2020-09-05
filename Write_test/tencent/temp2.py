
def compute(A, B, C):
    if 4*pow(A, 2)-8*A*B*C <= 0:
        print(0)
    else:
        temp = A*A-2*A*B*C
        sqrt_temp = pow(temp, 0.5)
        y2 = (A+sqrt_temp)/B
        y1 = (A-sqrt_temp)/B
        x2 = pow(y2, 2)/(2*A)
        x1 = pow(y1, 2)/(2*A)
        result1 = (x1+x2)*(y2-y1)/2
        result2 = (pow(y2, 3)-pow(y1, 3))/(6*A)
        print(result1-result2)


n = int(input())
for i in range(n):
    A, B, C = list(map(int, input().split()))
    compute(A, B, C)
