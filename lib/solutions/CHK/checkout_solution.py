

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    if (num_A + num_B + num_C + num_D) < len(skus):
        return -1
    else:

        discount_A = num_A//3

        discount_B = num_B//2

        total = 50*num_A - 20*discount_A + 30*num_B - 15*discount_B\
                + 20*num_C + 15*num_D
        return total

skus = "AAa"
print(checkout(skus))
