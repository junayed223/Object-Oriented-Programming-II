""" Code for multiplication """
num = int(input())
def mlp(num):
    for i in range(1,11):
        if i == 6:
            continue
        if i == 9:
            break
        print(f"{num}  * {i} = {num*i}")

mlp(num)

""" Code for sum even number """
sum = 0
for i in range(1,11):
        if i%2 == 0:
            sum+=i
print(sum)

""" Code for sum even from list """
list = [1, 3, 7, 8, 2]
sum = 0
for i in range(0, 5):
        if list[i] % 2 == 0:
            sum+=list[i]
print(sum)

""" Code for (list value) even/odd counter """
list = [1, 3, 7, 8, 2]
sum = 0
even_count = 0
odd_count = 0
for i in range(0, 5):
        if list[i] % 2 == 0:
            even_count += 1
        if list[i] % 2 != 0:
                odd_count += 1
print(even_count, odd_count)

""" Code for (index value) even/odd counter """
list = [1, 3, 7, 8, 2]
sum = 0
even_count = 0
odd_count = 0
for i in range(0, 5):
        if i % 2 == 0:
            even_count = even_count + list[i]
        if i % 2 != 0:
            odd_count = odd_count + list[i]
print(even_count, odd_count)

""" Code for (odd list value * 5) (even list value * 6) even/odd counter """
list = [1, 3, 7, 8, 2]
sum = 0
even_count = 0
odd_count = 0
for i in range(0, 5):
        if i % 2 == 0:
            b = list[i]*6
            even_count = even_count + b
        if i % 2 != 0:
            num2 = list[i]*5
            odd_count = odd_count + num2
print(even_count, odd_count)


""" Last Task """
a = [1,3,5,7,4]
print("Accessing list ",a[-2], a[2])
a[-3]=50
print("After Changing ", a)

a.append(100)
print ("After Append", a)

a.insert(2,200)
print("After Inserting : ",a)

a.pop();
a.remove(1)
print("After Pop ", a)

a1 = [2,4,6]
a2 = a + a1
print("Join ", a2)

b = a2.copy()
print("Copy of a3 to b:",b)

print("Sorted b:",sorted(b))

for i in range (len(b)):
    print(b[i],end=" ")
print("\nAfter Sclicing",a[2:4])