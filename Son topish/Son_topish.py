import random as r
def son_top(x=10):
    tasodifiy_son = r.randint(1,x)
    print(f"Men 1 dan {x}gacha son o'yladim. Topa olasizmi?")
    count =0
    while True:
        count+=1
        taxmin = int(input(">>"))
        if taxmin < tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling.")
        elif taxmin > tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            print(f"Tabriklaymiz! {count} ta taxmin bilan topdingiz!")
            break

    return count

def son_top_pc(x=10):
    print(f"Siz 1 dan {x}gacha son o'ylang. Topishga harakat qilaman!")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing: ")
    quyi = 1
    yuqori = x
    count = 0
    while True:
        count+=1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t),"
                    "men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            print(f"Men {count} ta taxmin bilan topdim!")
            break

    return count

def play(x=10):
    yana = True
    while yana:
        count_user = son_top(x)
        count_pc = son_top_pc(x)
        if count_user > count_pc:
            print("Men yutdim!")
        elif count_user < count_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'naysizmi? Ha(1)/Yo'q(0): "))

play()