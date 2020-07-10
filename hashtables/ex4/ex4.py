def has_negatives(a):
    cache = {}
    for i in a:
        if i < 0:
            postive_i = i * -1
            if postive_i in a:
                cache[postive_i] = True
            else:
                cache[postive_i] = False

    return [key for key, value in cache.items() if value is True]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
