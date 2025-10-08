#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Senhas Seguras
Gera senhas aleatórias com diferentes níveis de complexidade
"""

import random
import string
import secrets
import sys

class GeradorSenhas:
    def __init__(self):
        self.caracteres_minusculos = string.ascii_lowercase
        self.caracteres_maiusculos = string.ascii_uppercase
        self.numeros = string.digits
        self.simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
    def gerar_senha(self, tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
        """
        Gera uma senha segura com os parâmetros especificados
        
        Args:
            tamanho (int): Tamanho da senha (padrão: 12)
            incluir_maiusculas (bool): Incluir letras maiúsculas
            incluir_numeros (bool): Incluir números
            incluir_simbolos (bool): Incluir símbolos especiais
            
        Returns:
            str: Senha gerada
        """
        if tamanho < 4:
            raise ValueError("Tamanho mínimo da senha é 4 caracteres")
            
        # Montar conjunto de caracteres baseado nas opções
        caracteres = self.caracteres_minusculos
        
        if incluir_maiusculas:
            caracteres += self.caracteres_maiusculos
        if incluir_numeros:
            caracteres += self.numeros
        if incluir_simbolos:
            caracteres += self.simbolos
            
        # Garantir que pelo menos um caractere de cada tipo seja incluído
        senha = []
        
        # Sempre incluir pelo menos uma letra minúscula
        senha.append(random.choice(self.caracteres_minusculos))
        
        if incluir_maiusculas:
            senha.append(random.choice(self.caracteres_maiusculos))
        if incluir_numeros:
            senha.append(random.choice(self.numeros))
        if incluir_simbolos:
            senha.append(random.choice(self.simbolos))
            
        # Preencher o resto da senha
        for _ in range(tamanho - len(senha)):
            senha.append(secrets.choice(caracteres))
            
        # Embaralhar a senha
        random.shuffle(senha)
        
        return ''.join(senha)
        
    def calcular_forca_senha(self, senha):
        """
        Calcula a força da senha baseada em diferentes critérios
        
        Args:
            senha (str): Senha para analisar
            
        Returns:
            dict: Informações sobre a força da senha
        """
        pontuacao = 0
        criterios = {
            'tamanho_adequado': len(senha) >= 8,
            'tem_minuscula': any(c.islower() for c in senha),
            'tem_maiuscula': any(c.isupper() for c in senha),
            'tem_numero': any(c.isdigit() for c in senha),
            'tem_simbolo': any(c in self.simbolos for c in senha),
            'nao_e_palavra_comum': senha.lower() not in ['password', '123456', 'admin', 'qwerty']
        }
        
        pontuacao = sum(criterios.values())
        
        if pontuacao <= 2:
            nivel = "Fraca"
        elif pontuacao <= 4:
            nivel = "Média"
        else:
            nivel = "Forte"
            
        return {
            'nivel': nivel,
            'pontuacao': pontuacao,
            'criterios': criterios
        }
        
    def gerar_multiplas_senhas(self, quantidade=5, tamanho=12, **kwargs):
        """
        Gera múltiplas senhas
        
        Args:
            quantidade (int): Número de senhas a gerar
            tamanho (int): Tamanho de cada senha
            **kwargs: Outros parâmetros para gerar_senha
            
        Returns:
            list: Lista de senhas geradas
        """
        return [self.gerar_senha(tamanho, **kwargs) for _ in range(quantidade)]

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("           GERADOR DE SENHAS SEGURAS")
    print("="*50)
    print("1. Gerar senha personalizada")
    print("2. Gerar senha rápida (12 caracteres)")
    print("3. Gerar senha forte (16 caracteres)")
    print("4. Gerar múltiplas senhas")
    print("5. Analisar força da senha")
    print("6. Sair")
    print("="*50)

def obter_configuracoes():
    """Obtém as configurações do usuário"""
    print("\nConfigurações da senha:")
    
    try:
        tamanho = int(input("Tamanho da senha (padrão: 12): ") or "12")
    except ValueError:
        tamanho = 12
        
    incluir_maiusculas = input("Incluir maiúsculas? (s/n, padrão: s): ").lower() in ['s', 'sim', 'y', 'yes', '']
    incluir_numeros = input("Incluir números? (s/n, padrão: s): ").lower() in ['s', 'sim', 'y', 'yes', '']
    incluir_simbolos = input("Incluir símbolos? (s/n, padrão: s): ").lower() in ['s', 'sim', 'y', 'yes', '']
    
    return {
        'tamanho': tamanho,
        'incluir_maiusculas': incluir_maiusculas,
        'incluir_numeros': incluir_numeros,
        'incluir_simbolos': incluir_simbolos
    }

def main():
    """Função principal"""
    gerador = GeradorSenhas()
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção (1-6): ")
            
            if opcao == '1':
                config = obter_configuracoes()
                senha = gerador.gerar_senha(**config)
                print(f"\n🔐 Sua senha gerada: {senha}")
                
            elif opcao == '2':
                senha = gerador.gerar_senha(12)
                print(f"\n🔐 Senha rápida: {senha}")
                
            elif opcao == '3':
                senha = gerador.gerar_senha(16)
                print(f"\n🔐 Senha forte: {senha}")
                
            elif opcao == '4':
                try:
                    quantidade = int(input("Quantas senhas gerar? (padrão: 5): ") or "5")
                    config = obter_configuracoes()
                    senhas = gerador.gerar_multiplas_senhas(quantidade, **config)
                    print(f"\n🔐 Suas {quantidade} senhas:")
                    for i, senha in enumerate(senhas, 1):
                        print(f"{i}. {senha}")
                except ValueError:
                    print("Quantidade inválida!")
                    
            elif opcao == '5':
                senha_analise = input("Digite a senha para analisar: ")
                if senha_analise:
                    analise = gerador.calcular_forca_senha(senha_analise)
                    print(f"\n📊 Análise da senha:")
                    print(f"Nível: {analise['nivel']}")
                    print(f"Pontuação: {analise['pontuacao']}/6")
                    print("\nCritérios atendidos:")
                    for criterio, atendido in analise['criterios'].items():
                        status = "✅" if atendido else "❌"
                        print(f"  {status} {criterio.replace('_', ' ').title()}")
                        
            elif opcao == '6':
                print("\nObrigado por usar o Gerador de Senhas! 👋")
                break
                
            else:
                print("Opção inválida! Escolha entre 1 e 6.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro: {e}")
            
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
