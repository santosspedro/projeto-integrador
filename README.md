# projeto-integrador

## Protocolo de comunicação cliente-servidor

A comunicação entre cliente e servidor é feita via TCP, usando mensagens de texto em UTF-8.

### Formato da mensagem enviada pelo cliente

O cliente envia **uma linha de texto** contendo uma lista de **números inteiros separados por espaço**.  
Exemplo:

```text
10 5 3 20
