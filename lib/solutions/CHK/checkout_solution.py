

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    num_A = skus.count('A')
    num_B = skus.count('B')
    num_C = skus.count('C')
    num_D = skus.count('D')
    num_E = skus.count('E')
    num_F = skus.count('F')
    num_G = skus.count('G')
    num_H = skus.count('H')
    num_I = skus.count('I')
    num_J = skus.count('J')
    num_K = skus.count('K')
    num_L = skus.count('L')
    num_M = skus.count('M')
    num_N = skus.count('N')
    num_O = skus.count('O')
    num_P = skus.count('P')
    num_Q = skus.count('Q')
    num_R = skus.count('R')
    num_S = skus.count('S')
    num_T = skus.count('T')
    num_U = skus.count('U')
    num_V = skus.count('V')
    num_W = skus.count('W')
    num_X = skus.count('X')
    num_Y = skus.count('Y')
    num_Z = skus.count('Z')

    if (num_A + num_B + num_C + num_D + num_E + num_F + num_G + num_H + num_I\
        + num_J + num_K + num_L + num_M + num_N + num_O + num_P + num_Q + num_R\
        + num_S + num_T + num_U + num_V + num_W + num_X + num_Y + num_Z) < len(skus):
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
        
        num_H_d = num_H #num_H_d: number of H that can be discounted
        discount_H_1 = num_H_d//10
        num_H_d -= 10*discount_H_1
        discount_H_2 = num_H_d//5

        discount_K = num_K//2

        discount_N = num_N//3
        if num_M >= 1:
            num_M -= discount_N

        discount_P = num_P//5

        discount_R = num_R//3
        if num_Q >= 1:
            num_Q -= discount_R

        discount_Q = num_Q//3
        
        discount_U = num_U//4
        num_U -= discount_U

        num_V_d = num_V #num_V_d: number of V that can be discounted
        discount_V_1 = num_V_d//3
        num_V_d -= 3*discount_V_1
        discount_V_2 = num_V_d//2

        group_discount_items = num_S + num_T + num_X + num_Y + num_Z
        group_discount_num = group_discount_items//3
        items_to_remove = 3*group_discount_num
        #removal priority: x>s>t>y>z
        for i in range(items_to_remove):
            if num_X >= 1:
                num_X -=1
            elif num_S >=1:
                num_S -=1
            elif num_T >=1:
                num_T -=1
            elif num_Y >=1:
                num_Y -=1
            elif num_Z >=1:
                num_Z -=1

        total = 50*num_A - 50*discount_A_1 - 20*discount_A_2  + 30*num_B - 15*discount_B\
                + 20*num_C + 15*num_D + 40*num_E + 10*num_F + 20*num_G + 10*num_H -20*discount_H_1\
                - 5*discount_H_2 + 35*num_I + 60*num_J + 70*num_K - 20*discount_K + 90*num_L\
                + 15*num_M + 40*num_N + 10*num_O + 50*num_P - 50*discount_P + 30*num_Q - 10*discount_Q\
                + 50*num_R + 20*num_S + 20*num_T + 40*num_U + 50*num_V - 20*discount_V_1 - 10*discount_V_2\
                + 20*num_W + 17*num_X + 20*num_Y + 21*num_Z + 45*group_discount_num
        return total

skus = "SSSXS"
print(checkout(skus))
