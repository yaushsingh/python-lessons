my_account ={"nic": 12, "mega": 13, "broker": 35}
for name in my_account:
    print(name)
for value in my_account.values():
    print(value)
ages =list(range(20))
odds=[_ for _ in ages if _%2==1]
print(odds)