from random import randint


list1 = []
length = int(input('Enter number '))
for i in range(length):
    list1.append(randint(1, 100))


for i in range(length):
    for j in range(i, length):
        if list1[i] > list1[j]:
            temp = list1[j]
            list1[j] = list1[i]
            list1[i] = temp

print(list1)

print('branch1 commit1')
print('branch1 2 commit')
print('commit 3')

