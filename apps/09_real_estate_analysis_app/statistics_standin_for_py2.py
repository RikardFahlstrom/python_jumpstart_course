def mean(data):
    total = 0.0 #  To get the answer in float
    count = 0
    for x in data:
        count += 1
        total += x

    return total / max(1, count)  # max(1, count) to prevent it from dividing with 0

