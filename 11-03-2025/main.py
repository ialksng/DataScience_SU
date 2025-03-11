brand = ["Apple", "Sansung", "LG", "Apple"]

RAM = [4, 12, 8, 8]

Memory = [64, 128, 64, 128]

price = [90000, 60000, 40000, 120000]

type(brand)

len(brand)

max(brand)

min(brand)

price[0: 3]

print(brand.pop())

brand.append("Motorola")

print(sum(price))

## LIST COMPREHENSION
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in List:
    print(i ** 2)

att = {"RAM": 4, "Memory": 64, "Price":90000}

products = {"RAM" : RAM, "brand": brand, "Memory": Memory, "price": price}

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

sum = n1 + n2

product = n1 * n2

# Using .format()
message = "sum is {0} and product is {1}".format(sum, product)
print(message)


# Using f-strings
message = f"sum is {sum} and product is {product}"
print(message)

details = "I am Ajay Kumar from CS branch with rollnumber 40104767."
first_name = details.split()[2]
print(first_name)

roll_number = details.split()[8]
print(roll_number)

sur_name = details.split()[3]
print(sur_name[::-1])

details = "I am Ajay Kumar from CS branch with roll number 40104767."

if details.isupper():
    print("uppercase")
else:
    details = details.upper()
    print(details)

if details.isupper():
    print("uppercase.")








