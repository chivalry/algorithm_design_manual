def integer_division(num, div):
    if num < 0:
        return -1
    return 1 + integer_division(num - div, div)


if __name__ == '__main__':
    assert integer_division(7, 3) == 7 // 3
    assert integer_division(10, 5) == 10 // 5