# Projeto Didático: Força Bruta e Mitigação (Hipotético)

> **Aviso de Segurança (Crucial)**
>
> Este projeto é estritamente **educacional** e **defensivo**. Todos os testes devem ser realizados em um ambiente de laboratório isolado (VMs) sob seu controle, usando _targets_ intencionalmente vulneráveis (ex.: Metasploitable, DVWA). **Jamais** execute técnicas de ataque contra sistemas, redes ou ativos de terceiros sem permissão explícita.

---

## Objetivo

Simular ataques de força bruta e password spraying em um ambiente controlado para entender vetores, registrar evidências e, principalmente, documentar medidas de mitigação e defesa.

---

## Estrutura do Repositório

```
/ (root)
├─ README.md
├─ wordlists/
│  ├─ users.txt
│  └─ passwords.txt
├─ screenshots/
├─ commands/          # comandos de exemplo em arquivos .sh ou .txt
├─ LICENSE
└─ CONTRIBUTING.md
```

---

## 1. Configuração do Laboratório

**Ferramentas**
- VirtualBox (ou VMware)
- Kali Linux (atacante)
- Metasploitable 2 (vítima) e/ou VM com DVWA

**Rede**
- Usar `Host-Only` ou `Internal Network` para isolar as VMs.
- Verificar conectividade: `ping <IP-alvo>`.

---

## 2. Cenários e Comandos (Exemplos Educacionais)

> **Observação:** os exemplos abaixo são conceituais — são mostrados na documentação para fins didáticos. Não execute em redes/hosts que você não possua.

### 2.1 Força Bruta em FTP (Medusa — Exemplo)
- Exemplo de comando (hipotético):

`medusa -h 192.168.56.101 -u users.txt -P passwords.txt -M ftp`

ou para um usuário conhecido:

`medusa -h 192.168.56.101 -U msfadmin -P passwords.txt -M ftp`

### 2.2 Password Spraying em SMB
- Exemplo de comando (hipotético):

`medusa -h 192.168.56.101 -u users.txt -p 'Spring2025!' -M smb`

*Dica:* faça enumeração prévia com `nmap`, `enum4linux` para mapear serviços e usuários.

### 2.3 Automação em Formulário Web (DVWA)
- Técnica: automatizar POSTs para o endpoint de login, lidando com CSRF e sessões.
- Ferramentas comuns: Burp Suite (Intruder), Hydra, wfuzz. Medusa tem módulo genérico, mas costuma ser mais complexo para web.

---

## 3. Wordlists (Didáticas)

- `wordlists/users.txt` — exemplos: `admin`, `msfadmin`, `root`, `test`
- `wordlists/passwords.txt` — exemplos: `password`, `123456`, `msfadmin`, `toor`

> Arquivos curtos e educacionais — **não** publique wordlists ofensivas em repositórios públicos.

---

## 4. Evidências e Logs

- Coloque capturas de tela de testes (apenas em laboratório) em `screenshots/`.
- Salve saídas de comandos em `commands/` (ex.: `ftp_medusa_output.txt`).

---

## 5. Mitigações e Recomendações

**Força Bruta em Serviços (FTP, SMB)**
- Account lockout (3–5 tentativas).
- Políticas de senha forte (length + complexity).
- Rate limiting e IDS/IPS.
- Evitar portas padrão quando possível (mudança de porta não é solução completa).

**Password Spraying**
- MFA (recomendado).
- Monitoramento e correlação de logs (mesma senha testada em vários usuários).

**Automação Web**
- CAPTCHA / reCAPTCHA.
- WAF e rate limiting por endpoint.
- Validação de tokens CSRF e checagem de sessões.

---

## 6. Regras do Repositório

- **Privacidade:** recomendo criar o repositório como **private** no GitHub.
- **LICENSE:** use MIT ou outra licença permissiva; inclua um `DISCLAIMER` sobre o caráter educacional.
- **CONTRIBUTING.md:** instruções para manter o foco educacional e ético.

---

## 7. Modelo Rápido de `CONTRIBUTING.md`

```
# Contribuindo
Este repositório é educativo. Contribuições são bem-vindas, desde que:
- O material permaneça didático e defensivo.
- Não sejam adicionadas ferramentas/exploits para uso ilegítimo.
- Não se compartilhem wordlists ofensivas ou técnicas que facilitem abuso fora de laboratórios controlados.
```

---

## 8. Checklist antes de subir ao GitHub

- [ ] Remover/obscurecer credenciais reais
- [ ] Tornar o repo privado
- [ ] Incluir LICENSE e DISCLAIMER explícito
- [ ] Garantir que screenshots não exponham redes reais

---

## Contato / Observações

Se quiser, posso:
- Gerar os arquivos `README.md`, `CONTRIBUTING.md`, `.gitignore` e `LICENSE` prontos neste repositório de trabalho.
- Preparar um script `push_to_github.sh` com os comandos Git para facilitar o envio (você executaria localmente).

*Boa prática:* mantenha tudo privado enquanto estiver em desenvolvimento e só publique conteúdo público se estiver seguro de que não vaza informações sensíveis.

---

*Documento gerado automaticamente via assistente — versão educativa.*
