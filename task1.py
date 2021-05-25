def get_prime_nums(n):
    prime_nums = []
    if n > 1:
        for i in range(2, n):
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_nums.append(i)
        return prime_nums


if __name__ == '__main__':
    print(get_prime_nums(100))
