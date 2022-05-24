def swap_case(s):
    s = str(s)
    x = s.swapcase()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)