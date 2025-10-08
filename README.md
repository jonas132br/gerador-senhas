# 🔐 Gerador de Senhas Seguras

Um gerador de senhas robusto e configurável em Python com análise de força.

## ✨ Funcionalidades

- ✅ Geração de senhas personalizáveis
- ✅ Diferentes níveis de complexidade
- ✅ Análise de força da senha
- ✅ Geração de múltiplas senhas
- ✅ Interface interativa no terminal
- ✅ Caracteres seguros e aleatórios

## 🚀 Como executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
```bash
python gerador_senhas.py
```

## 🎯 Opções Disponíveis

1. **Gerar senha personalizada** - Configure tamanho e tipos de caracteres
2. **Gerar senha rápida** - Senha de 12 caracteres com configurações padrão
3. **Gerar senha forte** - Senha de 16 caracteres para máxima segurança
4. **Gerar múltiplas senhas** - Várias senhas de uma vez
5. **Analisar força da senha** - Verifique a segurança de uma senha

## 🔧 Configurações

- **Tamanho**: 4 a 50 caracteres
- **Maiúsculas**: A-Z
- **Minúsculas**: a-z
- **Números**: 0-9
- **Símbolos**: !@#$%^&*()_+-=[]{}|;:,.<>?

## 🎨 Tecnologias

- **Python 3** - Linguagem principal
- **secrets** - Geração segura de números aleatórios
- **string** - Manipulação de caracteres
- **random** - Embaralhamento de senhas

## 📊 Análise de Força

O gerador analisa senhas baseado em:

- ✅ Tamanho adequado (≥8 caracteres)
- ✅ Presença de letras minúsculas
- ✅ Presença de letras maiúsculas
- ✅ Presença de números
- ✅ Presença de símbolos especiais
- ✅ Não é palavra comum

## 🎮 Exemplo de Uso

```
==================================================
           GERADOR DE SENHAS SEGURAS
==================================================
1. Gerar senha personalizada
2. Gerar senha rápida (12 caracteres)
3. Gerar senha forte (16 caracteres)
4. Gerar múltiplas senhas
5. Analisar força da senha
6. Sair
==================================================

Escolha uma opção (1-6): 2

🔐 Senha rápida: K9#mP2@vL8xQ
```

## 🔒 Segurança

- Usa `secrets` para geração criptograficamente segura
- Garante pelo menos um caractere de cada tipo selecionado
- Embaralha a senha para evitar padrões
- Não armazena senhas geradas

## 🚀 Execução rápida

```bash
python gerador_senhas.py
```

