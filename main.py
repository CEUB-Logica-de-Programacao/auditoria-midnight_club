def etapa1(id):
    lista = []
    def aaa():
        for i in range(0,4):
            lista.append(int(id[i]))
            x = sorted(lista)
        new1 =int(x[0])*10 + int(x[2])
        new2 =int(x[1])*10 + int(x[3])
        return new1 + new2
    id = input()
    print(aaa())
    return 1000

def etapa2(x):
    h = True
    num = []
    while h == True:
        x = int(input())
        num.append(x)
        if x == 0:
            num.remove(0)
            h = False
    nums = sorted(num)
    lista2 =[]
    for n in range(1, len(nums)+1):
        lista2.append(n)
    for n in nums:
        if n in lista2:
            lista2.remove(n)
    print(lista2)
    return []

def etapa3(senha):
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
    return False

if __name__ == "__main__":
    if etapa1('1234') > 100:
        print('ID inválido')
        exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
