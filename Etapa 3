dict = {}
def aab():
    for n in range(0,len(senha)):
        if tem(senha[n]) == False:
            dict[senha[n]] = 0
        else:
            dict[senha[n]] = valor(senha[n]) +1
    for i in range(0, len(dict)):
        if valor(senha[i]) != valor(senha[len(dict)]):
            return False
    return True
def tem(aa):
    for k in dict.keys():
        if aa == k:
            return True
    return False
def valor(nome):
    for k, v in dict.items():
         if nome == k:
             return v
senha = input('Digite sua senha')
while aab() == False:
    print('Senha inválida')
    senha = input('Digite sua senha')
    dict = {}
    aab()
print(f'Sua senha é {senha}')
