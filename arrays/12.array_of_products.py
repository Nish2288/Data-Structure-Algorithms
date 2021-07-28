# O(N)
def arrayOfProducts(array):
    leftProduct =[1 for _ in range(len(array))]
    rightProduct = [1 for _ in range(len(array))]
    product = [1 for _ in range(len(array))]
    left = 1
    for i in range(len(array)):
        leftProduct[i] = left
        left = left * array[i]
    right = 1
    for j in reversed(range(len(array))):
        rightProduct[j] = right
        right = right * array[j]

        product[j] = rightProduct[j] * leftProduct[j]

    # for k in range(len(array)):
    #     product[k] = leftProduct[k] * rightProduct[k]

    return product

# O(N^2)
# def arrayOfProducts(array):
#     product = []
#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if i != j :
#                 runningProduct = runningProduct * array[j]
#         product.append(runningProduct)
#     return product


array = [5, 1, 4, 2]
print(arrayOfProducts(array))