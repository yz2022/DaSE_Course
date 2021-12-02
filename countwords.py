def countwords(data):
    counts = {}
    for i in data:
        counts[i] = counts.get(i, 0) + 1  # get返回指定键的值
    return counts


if __name__ == "__main__":
    data = ["zy", "yy", "zy", "ffff"]
    print("The result is %s" % countwords(data))
