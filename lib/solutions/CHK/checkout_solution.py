

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    num_E = skus.count('E')
    if (num_A + num_B + num_C + num_D + num_E) < len(skus):
        return -1
    else:
        num_A_d = num_A #num_A_d: number of A that can be discounted
        discount_A_1 = num_A_d//5
        num_A_d -= 5*discount_A_1
        discount_A_2 = num_A_d//3

        discount_E = num_E//2
        num_B -= discount_E

        discount_B = num_B//2

        total = 50*num_A - 50*discount_A_1 - 20*discount_A_2  + 30*num_B - 15*discount_B\
                + 20*num_C + 15*num_D + 40*num_E
        return total

skus = "EEB"
print(checkout(skus))

