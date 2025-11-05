# Projeto Didático: Força Bruta e Mitigação 

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

## Configuração do Laboratório

**Ferramentas**
- VirtualBox (ou VMware)
- Kali Linux (atacante)
- Metasploitable 2 (vítima) e/ou VM com DVWA

**Rede**
- Usar `Host-Only` ou `Internal Network` para isolar as VMs.
- Verificar conectividade: `ping <IP-alvo>`.

---

## Cenários e Comandos (Exemplos Educacionais)

> **Observação:** os exemplos abaixo são conceituais — são mostrados na documentação para fins didáticos. Não execute em redes/hosts que você não possua.

### Força Bruta em FTP (Medusa)
- Exemplo de comando (hipotético):

`medusa -h 192.168.56.101 -u users.txt -P passwords.txt -M ftp`

ou para um usuário conhecido:

`medusa -h 192.168.56.101 -U msfadmin -P passwords.txt -M ftp`

### Password Spraying em SMB
- Exemplo de comando:

`medusa -h 192.168.56.101 -u users.txt -p 'Spring2025!' -M smb`


### Automação em Formulário Web (DVWA)
- Técnica: automatizar POSTs para o endpoint de login, lidando com CSRF e sessões.
- Ferramentas comuns: Burp Suite (Intruder), Hydra, wfuzz.

---

## Wordlists (Didáticas)

- `wordlists/users.txt`: `admin`, `msfadmin`, `root`, `test`
- `wordlists/passwords.txt`: `password`, `123456`, `msfadmin`, `toor`

## Mitigações e Recomendações

**Força Bruta em Serviços (FTP, SMB)**
- Account lockout (3–5 tentativas).
- Políticas de senha forte (length + complexity).
- Rate limiting e IDS/IPS.
- Evitar portas padrão quando possível (mudança de porta não é solução completa).

**Password Spraying**
- MFA.
- Monitoramento e correlação de logs (mesma senha testada em vários usuários).

**Automação Web**
- CAPTCHA / reCAPTCHA.
- WAF e rate limiting por endpoint.
- Validação de tokens CSRF e checagem de sessões.

# Contribuindo
Este repositório é educativo. Contribuições são bem-vindas, desde que:
- O material permaneça didático e defensivo.
- Não sejam adicionadas ferramentas/exploits para uso ilegítimo.
- Não se compartilhem wordlists ofensivas ou técnicas que facilitem abuso fora de laboratórios controlados.
```

