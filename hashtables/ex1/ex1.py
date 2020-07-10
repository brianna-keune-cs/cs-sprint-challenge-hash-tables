def get_indices_of_item_weights(weights, length, limit):
    cache = {weights[i]: i for i in range(length)}

    for i in range(length):
        weight = weights[i]
        if limit - weight in cache:
            index_of_limit_diff = cache[limit - weight]
            if i > index_of_limit_diff:
                return (i, index_of_limit_diff)
            return (index_of_limit_diff, i)

    return None
