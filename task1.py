def get_prime_nums(n):
    prime_nums = []
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_nums.append(i)
        return prime_nums


if __name__ == '__main__':
    print(get_prime_nums(199))
