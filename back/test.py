import datetime
a = datetime.datetime.utcnow().date()
a = datetime.datetime.utcnow().time('H, M')
print(a)