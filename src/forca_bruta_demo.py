"""
forca_bruta_demo.py
Simulador didático e seguro de tentativa de credenciais (NÃO realiza conexões de rede).
Objetivo: demonstrar lógica de força bruta e gerar evidências/relatório.
"""

import time
from pathlib import Path

# --- Configurações (educacionais) ---
USERS = ["admin", "msfadmin", "test", "root"]
PASSWORDS = ["password", "123456", "msfadmin", "toor", "spring2025!"]

# Credenciais 'reais' do alvo simulado (em um laboratório controlado só seria usado para testes).
TARGET_CREDENTIAL = ("msfadmin", "msfadmin")  # (username, password) -- apenas para simulação

OUTPUT_DIR = Path("commands")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOGFILE = OUTPUT_DIR / "output_log.txt"

# --- Funções ---
def check_credentials(user: str, password: str) -> bool:
    """
    Função simulada que verifica credenciais em memória.
    Não acessa a rede, não realiza ataques reais.
    Retorna True se coincidir com TARGET_CREDENTIAL.
    """
    return (user, password) == TARGET_CREDENTIAL

def run_simulation(users, passwords, delay=0.1):
    start = time.time()
    attempts = 0
    successes = []

    with open(LOGFILE, "w", encoding="utf-8") as f:
        f.write(f"Simulação iniciada: {time.ctime()}\n")
        f.write(f"Usuários testados: {users}\n")
        f.write(f"Senhas testadas: {passwords}\n\n")

        for u in users:
            for p in passwords:
                attempts += 1
                ok = check_credentials(u, p)
                line = f"[{attempts:04d}] Testando {u}:{p} -> {'SUCCESS' if ok else 'FAIL'}\n"
                print(line.strip())
                f.write(line)
                if ok:
                    successes.append((u, p))
                    # registramos mas continuamos (didático)
                time.sleep(delay)  # atraso intencional para simular tempo entre tentativas

        elapsed = time.time() - start
        f.write("\n--- Resultado ---\n")
        f.write(f"Total de tentativas: {attempts}\n")
        f.write(f"Tempo total (s): {elapsed:.2f}\n")
        f.write(f"Credenciais encontradas: {successes}\n")
    return attempts, successes, elapsed

# --- Execução principal ---
if __name__ == "__main__":
    print("Simulador de força bruta (seguro & local). Veja o arquivo commands/output_log.txt para o log.")
    run_simulation(USERS, PASSWORDS, delay=0.05)
