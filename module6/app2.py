"""
Create list of prime number up to specified limit using dedicated function

generate_primes(10) -> [1,2,3,5,7]

"""
import random


def generate_primes(limit: int):
    result = []
    for i in range(1, limit + 1):
        for j in range(2, i // 2 + 2):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


generate_primes(100)



"""
Select 2 (distinct) random numbers from primes numbers generated above

select_primes(generate_primes(100)) -> (<int>, <int>)
"""

def select_primes(in_list: list):
    i = random.choices(in_list)
    in_list.remove(i[0])
    j = random.choices(in_list)
    return i[0], j[0]


print(select_primes(generate_primes(100)))