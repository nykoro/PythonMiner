import hashlib  

previous_hash = "0000000000000000000a1b2c3d4e5f6789abcdef1234567890abcdef12345678"
transactions = [
    "user1 sent 0.00000001 BTC to user2",
    "user3 sent 0,0004 BTC to user4",
    "user5 sent 0.9 BTC to user6",
    "user7 sent 0.5001 BTC to user8",
    "user9 sent 0.245401 BTC to user10",
    "user11 sent 2.170001 BTC to user12",
    "user13 sent 1.15665001 BTC to user14",
]
transactions_data = "".join(transactions)
nonce = 0
frequence_try= 1000000

def calculate_hash(previous_hash, transactions, nonce): 
    data=f"{previous_hash}{transactions}{nonce}"
    return hashlib.sha256(data.encode()).hexdigest()

difficulty = 7

while True:
    block_hash = calculate_hash(previous_hash,transactions_data,nonce)
    if nonce % frequence_try == 0: #progresso a cada X tentativas
        print(f"Tentando nonce: {nonce}, Hash atual: {block_hash}")
    if block_hash.startswith("0"*difficulty): #valor da dificuldade é variável
        print(f"Bloco minerado! Nonce {nonce}, Hash: {block_hash}")
        break
    nonce += 1