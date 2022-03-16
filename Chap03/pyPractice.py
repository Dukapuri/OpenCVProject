print("1번 짝수 홀수 판단")
def oddOrEven(num):
    if num % 2:
        print("홀수")
    else:
        print("짝수")

oddOrEven(5)
oddOrEven(6)


for kk in range(1,10):
    for jj in range(1,10):
        print(f"{kk} * {jj} = {kk * jj}")

print("3번 이메일")
def make_url(domain:str):
    return "www." + domain + ".com"
print(make_url("naver"))
print("4.100이하의 짝수가 들어있는 리스트를 생성하고 for문 역순으로 출력")
arr1 = [2 * xx for xx in range(1,51)]
arr2 = [kk for kk in arr1[::-1]]
print(arr2)

print("5. 30분 전의 시간 출력")
def function_time(h,m):
    if m < 30:
        h -= 1
        if h == 0:
            h = 12
        m += 60
    print(f"{h}시 {m - 30}분")
function_time(1,10)
function_time(4,40)
function_time(3,20)


print("6. 1~50 범위 안의 숫자중 가장 높은거")
from random import randint
numbers = [randint(1,50) for i in range(1000)]
numarray = [0 for kk in range(51)]
for kk in numbers:
    numarray[kk] += 1

maxIndex = 0
for ii,jj in enumerate(numarray):
    if numarray[maxIndex] < jj:
        maxIndex = ii
print(f"숫자: {maxIndex} 중복수: {numarray[maxIndex]}")


print("7. 이중포문을 사용해 2차원 행렬 출력")
import numpy as np

def function_array(row, col):
    i = 1
    anslist = np.zeros((row, col))
    for kk in range(row):
        for jj in range(col):
            anslist[kk][jj] = i
            i += 1
    return anslist
arr = function_array(3,4)
print(arr)


print("8. transpose")
def transpose(array):
    row = len(array[0])
    col = len(array)
    anslist = np.zeros((row,col))
    i = 1
    for kk in range(col):
        for jj in range(row):
            anslist[jj][kk] = i
            i += 1
    return anslist
print(transpose(arr))

print("9. 실수형 원소 10개를 갖는 ndarray행렬")
import numpy as np
np.random.seed(10)
float_array = np.random.rand(10)
sum = 0
for kk in float_array:
    sum += kk
avg = sum / 10
print("sum = %.2f, avg = %.2f" %(sum, avg))


from random import randint
print("10. 0~50 사이의 임의의 원소 500개 생성")
list1 = [randint(0,50) for kk in range(500)]
list2 = [0 for kk in range(51)]
listKey = []
listValue = []
for kk in list1:    #원소의 중복수를 알아내는 구문
    list2[kk] += 1

for kk, jj in enumerate(list2):
    if kk < 3:
        listKey.append(kk)
        listValue.append(jj)
    else:
        for dd,ff in enumerate(listKey):
            if kk not in listKey:
                if listValue[dd] < jj:
                    listKey[dd] = kk
                    listValue[dd] = jj

for kk in range(3):
    print(f"{kk + 1}. 숫자: {listKey[kk]} 빈도수: {listValue[kk]}")

