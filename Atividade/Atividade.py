import numpy as np
num = int(input("Digite um numero: "))
def int_to_bin(num):
    return np.binary_repr(num)

print(f'O número {num} em binário é {int_to_bin(num)}')