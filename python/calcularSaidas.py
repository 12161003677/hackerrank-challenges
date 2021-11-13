#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calcularSaidas' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER capacidade
#  2. INTEGER_ARRAY pacotes
#

def calcularSaidas(capacidade, pacotes):
    quantidadeCaminhoes = 1
    carregamento = 0
    for i, vi in enumerate(pacotes):
        if vi + carregamento <= capacidade:
            carregamento += vi
        else:            
            quantidadeCaminhoes +=1
            carregamento = vi
    
    return quantidadeCaminhoes
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    capacidade = int(input().strip())

    pacotes_count = int(input().strip())

    pacotes = []

    for _ in range(pacotes_count):
        pacotes_item = int(input().strip())
        pacotes.append(pacotes_item)

    result = calcularSaidas(capacidade, pacotes)

    fptr.write(str(result) + '\n')

    fptr.close()
