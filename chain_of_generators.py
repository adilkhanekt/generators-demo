

def gen_num(start_num: int, end_num: int):
    while start_num <= end_num:
        yield start_num
        start_num +=1


# Eaxmple 1
def get_pow(start_num: int, end_num: int):
    for i in gen_num(start_num, end_num):
        if i % 2 == 0:
            yield i**2


pow_gen = get_pow(1, 10)

pow1 = next(pow_gen)
pow2 = next(pow_gen)
pow3 = next(pow_gen)

print(f"First: {pow1}, second: {pow2}, third: {pow3}")


# Example 2
def get_pow_another(iterator):
    for i in iterator:
        if i % 2 == 0:
            yield i**2

num_gen = gen_num(1, 10)
pow_gen_another = get_pow_another(num_gen)

pow_another_1 = next(pow_gen_another)
pow_another_2 = next(pow_gen_another)
pow_another_3 = next(pow_gen_another)

print(f"First: {pow_another_1}, second: {pow_another_2}, third: {pow_another_3}")