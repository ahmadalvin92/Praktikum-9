#4
import random

def random_String(x, n):
    ran_dom = []
    a = 0
    while a < n:
        rand = [''.join(random.sample(x, len(x)))]
        ulangi = 0
        if (rand  not in ran_dom):
            ran_dom += rand
            a += 1
            ulangi += 1
            print()
        print(ran_dom)

random_String('aku', 4)
