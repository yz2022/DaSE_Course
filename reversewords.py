def reversewords(data):
    data = data.split(" ")
    data = data[-1::-1]  # -1移到末尾，倒着以1步移
    ndata = " ".join(data)  # join可以连列表类型的序列，不仅仅是字符串
    return ndata


if __name__ == "__main__":
    data = "i love you"
    print(reversewords(data))
