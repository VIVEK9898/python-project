d1={'mango':56,'banana':11}
d2={'apple':6,'grapes':21}
d3={'orange':6,'guava':41}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)
