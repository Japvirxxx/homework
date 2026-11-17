
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

def find_product(tup):
    product = 1
    for num in tup:
            product *= num
    return product

result1 = find_product(tup1)
result2 = find_product(tup2)
print("The product of tup1",result1)
print("The product of tup2",result2)