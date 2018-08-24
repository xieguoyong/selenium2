keys = {'b', 'a', 'c', 'e', 'd', 'x', 'y'}
values = {'2', '1', '3', '5', '4'}
dic = {}

# zip 需要通过list()转化为列表
# print(list(zip(keys, values)))

for key, value in zip(keys, values):
    # print(key, value)
    dic[key] = value

print(dic)
