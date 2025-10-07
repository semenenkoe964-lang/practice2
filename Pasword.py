from random import choices

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz' 
punctuation = '!#$%&*+-=?@^_' 

chars = ''

is_lower_case=int(input("1 - нижний регистр 0 - верхний регистр 2 - верхний регистр : "))
is_punctuation=int(input("1 - есть спец символы 0 - нет спец символов: "))
is_digits=int(input("1 - есть цифры 0 - нет цифр: "))
pwd_length = int(input('Введите длину пароля: '))
if (is_lower_case==0):
    lowercase=""
elif(is_lower_case==1):
    uppercase=""
if not(is_punctuation):
    punctuation=""
if not(is_digits):
    digits=""
for text, seq in (('Включить цифры',         digits     ),
                  ('Включить uppercase',     uppercase  ),
                  ('Включить lowercase',     lowercase  ),
                  ('Включить спец. символы', punctuation)):
        chars += seq

password = ''.join(choices(chars, k=pwd_length))

print('\n', password, '\n', sep='')
