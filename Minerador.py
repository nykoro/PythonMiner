import hashlib  

previous_hash = "0000000000000000000a1b2c3d4e5f6789abcdef1234567890abcdef12345678" #hash e transações ficticias
transactions = [
    "\nuser1 sent 0.00000001 BTC to user2\n",
    "user3 sent 0,0004 BTC to user4\n",
    "user5 sent 0.9 BTC to user6\n",
    "user7 sent 0.5001 BTC to user8\n",
    "user9 sent 0.245401 BTC to user10\n",
    "user11 sent 2.170001 BTC to user12\n",
    "user13 sent 1.15665001 BTC to user14\n",
]
transactions_data = "".join(transactions)
nonce = 0
frequence_try= 100000

def calculate_hash(previous_hash, transactions, nonce): 
    data=f"{previous_hash}{transactions}{nonce}"
    return hashlib.sha256(data.encode()).hexdigest()

difficulty = 7 #Esse bobalhão deve ser automatizado no futuro, só não sei como ainda.

while True:
    block_hash = calculate_hash(previous_hash,transactions_data,nonce)
    if nonce % frequence_try == 0: #progresso a cada número de tentativas definidas na variável frequence_try.
        print(f"Tentando nonce: {nonce}, Hash atual: {block_hash}")
    if block_hash.startswith("0"*difficulty): #valor que multiplica a variável difficulty é alterável.
        print(f"Bloco minerado! Nonce {nonce}, Hash: {block_hash}")
        break
    nonce += 1

# Criar um registro de cada bloco minerado. Inicio

with open("info_do_bloco_minerado.txt", "w") as file:
    file.write(f"Hash anterior: {previous_hash} \n")
    file.write(f"\nTransactions: {transactions_data} \n")
    file.write(f"Nonce: {nonce} \n") #vai ficar em ingles mesmo pra ficar mais bonitinho. Algumas quebras de linha adicionadas puramente por estética ou facilitação da leitura.
    file.write(f"\nBlock Hash: {block_hash} \n")

print("Bloco salvo em 'info_do_bloco_minerado.txt'")

# Criar um registro de cada bloco minerado. Fim
