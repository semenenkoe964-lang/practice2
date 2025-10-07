def print_pack_report(count):
    if (count%5==0)and(count%3==0):
        print(count,"- расфосуем по 3 и по 5")
    elif (count%5==0):
        print(count,"- расфосуем по 5")
    elif (count%3==0):
        print(count,"- расфосуем по 3")
    else:
        print(count, "- не заказываем")
count_inp=int(input())
for i in range(count_inp,0,-1):
    print_pack_report(count_inp)
    count_inp-=1
