import osc

test = osc.controller('169.254.46.163', live=True)

res = test.send(osc.construct("/info"))

print(test.SOCK)
print(res)
