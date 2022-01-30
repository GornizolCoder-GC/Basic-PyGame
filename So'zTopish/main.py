import random as r
import funksiyalar
from base import enuz

savol = r.choice(list(enuz.keys()))
xname = enuz[savol]
yname = ''.join(["-" for x in xname])
print(f"'{savol}' so'zining ma'nosi nima?\n{yname}")

urinish = 0
while xname != yname:
    yname = funksiyalar.get_info(xname,yname)
    print(yname)
    urinish+=1
else:
    print(f"Urinishlar soni: {urinish}")
