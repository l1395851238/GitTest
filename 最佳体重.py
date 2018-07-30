height = int(input("请输入身高："))
weight = int(input("请输入体重："))
bestWeight = height - 105
if bestWeight > weight:
    print("偏瘦")
elif bestWeight < weight:
    print("偏胖")
else:
    print('正常')