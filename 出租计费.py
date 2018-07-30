while True:
    price = 0
    mile = int(input())
    if mile <= 0:
        print("请输入正确的公里数进行计算")
    elif mile <= 2:
        price = 8
    elif mile > 2 and mile <= 12:
        price = (mile - 2) * 1.2 + 8
    else:
        price = (12 - 2) * 1.2 + (mile - 12) * 1.5 + 8
    print(price)