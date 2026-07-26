import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    # Si OUTPUT_PATH existe (como en HackerRank) guarda en archivo, 
    # de lo contrario muestra el resultado directamente en la terminal.
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        n = int(input().strip())
        result = factorial(n)
        fptr.write(str(result) + '\n')
        fptr.close()
    else:
        print("Escribe un número entero:")
        n = int(input().strip())
        result = factorial(n)
        print(f"El factorial de {n} es: {result}")