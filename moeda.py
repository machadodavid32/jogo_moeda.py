from random import random
def joga_moeda():
    #gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'
print(joga_moeda())
