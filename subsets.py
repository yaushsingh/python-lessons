from itertools import chain,combinations
a={4,3,2,1}

def powerset(a_set):
    s=a_set
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

subset = list(powerset(a))
# c= list(powerset(a))
# print(len(c[1]))
# for ele in subset:
#     b = sum(list(ele))
#     if b == 4:
#         print(ele)

a= [ ele for ele in subset if sum(list(ele)) == 5]
print(a)