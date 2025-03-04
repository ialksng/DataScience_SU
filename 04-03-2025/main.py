price = 4000

for i in [5, 10, 15, 20]:
    print(price - price*i/100)

print(price - price*5/100)
print(price - price*10/100)
print(price - price*15/100)
print(price - price*20/100)

n = 5
for i in range(1, 11):
    print(i*n)

for i in range(2, 11):
    if(i % 2 == 0):
        print(i)

for i in range(2, 11, 2):
    print(i)

i = 0
while i in range(5):
    print(i)
    i +=1

j = 5
while j <= 20:
    print(price - price*j/100)
    j += 5

m = 1
while m <= 10:
    print(n*m)
    m += 1

k = 2
while k <= 10:
    if k % 2 == 0:
        print(k)
    k += 1

# zip -- iterating over multiple lists simultaneously
a = [1, 3, 4, 5]
b = ['A', 'B', 'C', 'D']
c = ['!', '@', '#','$']

for i, j, k in zip(a, b, c):
    print(i, j, k)

combined =  list(zip(a, b, c))
print(combined)

data = [(1, 'A', '!'), (3, 'B', '@'), (4, 'C', '#'), (5, 'D', '$')]
x, y, z = zip(*data)
print(x)
print(y)
print(z)

# enumerate - iterate over both index and value of an iterable simultaneously
serial_no = [1, 2, 3]
fruits = ['A', 'B', 'C']
for i, j in zip(serial_no, fruits):
    print(i, j)

fruits = ['A', 'B', 'C']
for i, j in enumerate(fruits, start = 7):
    print(i, j)


message = " hello "
for i, j in enumerate(message):
    print(i, j)