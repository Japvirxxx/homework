test_dic = {'a': 3, 'b': 2, 'c': 3}
print("the original dictionary is : " + str(test_dic))

K = 3

res = 0
for key in test_dic:
    if test_dic[key] == K:
        res = res + 1

print("The frequency of K is : " + str(res))