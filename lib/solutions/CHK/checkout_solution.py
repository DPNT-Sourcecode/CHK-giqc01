

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    num_E = skus.count('E')
    num_F = skus.count('F')
    if (num_A + num_B + num_C + num_D + num_E + num_F) < len(skus):
        return -1
    else:
        num_A_d = num_A #num_A_d: number of A that can be discounted
        discount_A_1 = num_A_d//5
        num_A_d -= 5*discount_A_1
        discount_A_2 = num_A_d//3

        discount_E = num_E//2
        if num_B >= 1:
            num_B -= discount_E

        discount_B = num_B//2

        discount_F = num_F//3
        num_F -= discount_F
        
        total = 50*num_A - 50*discount_A_1 - 20*discount_A_2  + 30*num_B - 15*discount_B\
                + 20*num_C + 15*num_D + 40*num_E + 10*num_F
        return total

skus = "FFFF"
print(checkout(skus))
