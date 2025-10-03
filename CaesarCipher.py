offset=int(input("Введите сдвиг: "))
cipher=input("Шифр 1 , Дешифр 0: ")
txt=input("Текст :")
newTxt=""
alphabet=0
startAlpha=1040
endAlpha=1103
if 65<=ord(txt[0])<=122:
    alphabet=1
if alphabet:
    startAlpha=65
    endAlpha=122
if cipher=="1":
    for i in txt:
        if ord(i)+offset<=endAlpha:
            newTxt+=chr(ord(i)+offset)
        else:
            newTxt += chr(ord(i) + offset-endAlpha+startAlpha)
else:
    for i in txt:
        if ord(i)-offset>=startAlpha:
            newTxt+=chr(ord(i)-offset)
        else:
            newTxt += chr(endAlpha-(startAlpha-(ord(i) + offset)))
print(newTxt)
