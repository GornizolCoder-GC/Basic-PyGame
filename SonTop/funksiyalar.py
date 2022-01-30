import  random

# Inson navbati funksiyasi
def person_find(finish,start=1):
    ''' Kompyuter son yashiradi Inson topadi - funksiyasi '''
    x = random.randint(start,finish)
    i = 0
    n = None
    print(f"{start} dan {finish} gacha oraliqda son yashirilgan, shu sonni toping!")
    while n!=x:
        n = int(input("\nKalit so`z: "))
        if n > x:
            print("pastga")
        elif n < x:
            print("yuqoriga")
        i+=1
    else:
        print(f"🥳 Tabriklaymiz! Javobingiz to'g'ri.\nYashirilgan son: {x}\nUrinishlar soni: {i}")
    return i

# Kompyuter navbati funksiyasi
def comp_find(stop, start=1):
    ''' Inson son yashiradi Kompyuter topadi - funksiyasi '''
    x = list(range(start,stop))

    # Binary search operatori
    st1 = 0
    fn1 = len(x)
    j = 0
    n = ''
    input(f"{start} dan {stop} gacha oraliqda son o'ylang. O'ylab bo'lib ENTER tugmasini bosing!")
    while n!='T':
        middle = (st1+fn1)//2
        print(x[middle])
        n = input(f"\nO'ylagan soningiz {x[middle]} bo'lsa T(true), kichik bo'lsa '-' va agar katta bo'lsa '+' kiriting:  ")
        if n == '-':
            fn1 = middle-1
        elif n == '+':
            st1 = middle+1
        j+=1
    else:
        print(f"🥳🥳🥳🥳"
        f"\nYashirilgan son: {x[middle]}"
        f"\nUrinishlar soni: {j}")
    return j

# Inson va kompyuterlarning urinishlarini solishtirish
def get_result(person_i, comp_j):
    ''' Urinishlarni solishtirish '''
    i = person_i
    j = comp_j
    print(f"Inson\tKompyuter\n <{i}>  :  <{j}>")
    if i<j:
        print("<<<  Inson yutdi  >>>")
    elif i>j:
        print("<< Kompyuter yutdi >>")
    else:
        print("!! DURRANG !!")
