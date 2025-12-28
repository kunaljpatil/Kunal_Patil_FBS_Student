# Q6. Find two numbers in list whose product is maximum using set.


lst = [2, 3, 5, 7, 9, 4]

max_product = -1
pair = ()

nums = set(lst)

nums_list = list(nums)

for i in range(len(nums_list)):
    for j in range(i+1, len(nums_list)):
        p = nums_list[i] * nums_list[j]
        if p > max_product:
            max_product = p
            pair = (nums_list[i], nums_list[j])

print("Max product pair =", pair)
print("Product =", max_product)
