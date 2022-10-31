h = True
num = []
while h == True:
    x = int(input('Digite os votos computados (0 para encerrar):'))
    num.append(x)
    if x == 0:
        num.remove(0)
        h = False
nums = sorted(num)
lista2 =[]
print(num,nums)
for n in range(1, len(nums)+1):
    lista2.append(n)
for n in nums:
    if n in lista2:
        lista2.remove(n)
print(lista2)    
