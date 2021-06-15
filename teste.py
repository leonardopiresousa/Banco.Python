from models.cliente import Cliente
from models.conta import Conta

joao: Cliente = Cliente('João Palhinha', 'palhinha@gmail.com', '23657890', '21/05/2021')
nuno: Cliente = Cliente('Nuno Mendes', 'nmendes@gmail.com', '37890384', '20/05/2021')

#print(joao)
#print(nuno)

contaj: Conta = Conta(joao)
contan: Conta = Conta(nuno)

#print(contaj)
#print(contan)
