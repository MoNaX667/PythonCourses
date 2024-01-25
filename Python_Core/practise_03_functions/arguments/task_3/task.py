def union(*args) -> set:
    result_collection = set()

    for elem in args:
        result_collection.update(elem)

    return result_collection


def intersect(*args) -> set:
    result_collection = set()
    counter = 0

    for elem in args:
        if counter != 0:
            result_collection = set(result_collection) & set(elem)
        else:
            result_collection = elem
        counter += 1

    return result_collection

