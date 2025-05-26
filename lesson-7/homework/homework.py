
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, nums)))           # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums))))  # [4, 16]

# 1
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

# 2
def digit_sum(k):
    return sum(map(int, str(k)))

#  3
def print_powers_of_two(N):
    p = 2
    while p <= N:
        print(p, end=' ')
        p *= 2

