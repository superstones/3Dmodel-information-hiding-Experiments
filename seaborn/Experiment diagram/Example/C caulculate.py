def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


def gen_last_value(n, m):
    first = get_value(n)
    print("n:%s     value:%s" % (n, first))
    second = get_value(m)
    print("n:%s     value:%s" % (m, second))
    third = get_value((n - m))
    print("n:%s     value:%s" % ((n - m), third))
    return first / (second * third)


if __name__ == "__main__":
    # C(12,5)
    rest = gen_last_value(5, 4)
    print("value:", rest)
