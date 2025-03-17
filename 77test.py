import time
import random

# Gera um tempo aleatório entre 1 e 3 segundos (com precisão de milissegundos)
delay = random.uniform(0, 2)

print(f"Aguardando {delay:.3f} segundos...")
time.sleep(delay)

print("Fim do delay!")
