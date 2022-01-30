from funksiyalar import *
import random as rd


# o`yin haqida(shartlari)

print("\t\tKOMPYUTER && INSON\t\t\n\"inson va kompyuter orasida yashirin sonni aniqlash o'yini\"")
print("--\t\t\t\bSHARTLARI\t\t\t\b--\
       \n\t\b\b* o'yin boshlanishidan oldin foydalanuvchi sonlar oralig'ini kiritadi \
       \n\t\b\b* o'yinning maqsadi o'sha yashirilgan sonni topish \
       \n\t\b\b* o'yin 2 qismdan iborat: \
       \n\t\b\b 1-qismda: inson >> kompyuter yashirgan sonni topadi \
       \n\t\b\b 2-qismda: kompyuter >> inson yashirgan sonni topadi ")

# chegara kiritish
a,b = input("\nOraliq kiriting. Masalan (3-30),(1-10)\n").split('-')


# Inson navbati
print("\nINsoN -> KoMpuTer")
pi = person_find(int(b),int(a))

# Kompyuter navbati
print("\nKoMpuTer -> INsoN")
cj = comp_find(int(b),int(a))

get_result(pi,cj)
