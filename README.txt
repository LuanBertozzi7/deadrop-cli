Chat de terminal criptografado de ponta a ponta para duas pessoas, via Tor.

## Como funciona

Um lado escuta e gera um endereço `.onion` + chave pública.
O outro conecta usando essas informações.
As mensagens são cifradas antes de sair da máquina — o Tor vê apenas ciphertext.

## Criptografia

- **X25519** — troca de chaves sem transmitir o segredo
- **ChaCha20-Poly1305** — criptografia autenticada das mensagens
- **Tor hidden service** — anonimato + travessia de NAT

## Requisitos

- Python 3.10+
- Tor instalado e rodando
- `pip install cryptography`

## Uso

```bash
# Lado que escuta
python deadrop.py --listen

# Lado que conecta
python deadrop.py --connect <endereco.onion> <chave-publica>
