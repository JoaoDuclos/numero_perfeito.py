def numeroperfeito(n):
    if n.isdigit():
        n_digit = int(n)
        x = 1
        divisores = 0
        total = 0
        while x<n_digit:
            resto = n_digit % x
            if resto == 0:
                total+=x
                divisores+=1
            x+=1
        if total == n_digit:
            return True
        else:
            return False
    else:
        print('\nPor favor digite um número.')




n = input('Digite um númeoro: ')
if n.isdigit():
    n_digit = int(n)
    if numeroperfeito(n):
        print('O número é perfeito. :)')
    else:
        print('O número não é perfeito. :(')
else:
    print('\nPor favor digite um número.')