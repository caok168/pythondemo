
list1 = ['zhangsan','lisi','wangwu','laoer']
list2 = ['zhangsan','lisi','laoer','wangqi']

list1 = []

a = [x for x in list1 if x in list2]


print(a)
