import random

def nakljucje(n=1):
    podatki=[]

    for i in range(n):
        data=[random.randint(100,1000),random.randint(100,1000)]
        podatki.append(data)
    return podatki