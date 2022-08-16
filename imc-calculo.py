import os
import json
from re import S

os.system('clear')

while True:
    print("\n")
    print("\033[93m\033[01mCálculo de Índice de Massa Corporal (IMC)\033[0m")

    fazer_cadastro = None
    while fazer_cadastro == None:
        
        # Loop de validação para início do processo cadastro
        fazer_cadastro = input("Deseja fazer cadastro? \033[93m[s/n]\033[0m: ")

        # Valida se não foi digitado nada além de "s" (sim) ou "n" (não)
        if fazer_cadastro != 's' and fazer_cadastro != 'n':
            fazer_cadastro = None
        elif fazer_cadastro == 's':

            # Caso sim, é iniciado o processo de cadastro
            os.system('clear')
            print("\n")
            print("\033[93m\033[01m")
            print('Cadastro'.center(40,'-'))
            print("\033[0m")

            # Cadastro composto por nome, sexo, peso e alturadados
            nome = input("\nDigite seu nome de usuário: \n")

            # Loop de validação de escrita de 'm' (masculino) ou 'f' (feminino)
            sexo = None
            while sexo == None:
                sexo = input("Sexo [m/f]: ")
                if sexo != 'm' and sexo != 'f':
                    sexo = None

            peso = float(input("Quanto você pesa? (kg)\n"))
            altura = float(input("Qual a sua altura? (m)\n"))    

            # Cálculo de IMC 
            imc = round(peso/(altura**2),2)
            print("\nO seu IMC é de {:.2f}\n".format(imc))
            
            # Definição de diagnóstico do IMC diferenciado por sexo (masculino e feminino)
            diagnostico = None

            if sexo == 'm':
                if imc < 19.5:
                    diagnostico = 'Peso abaixo do normal'
                elif imc < 26:
                    diagnostico = 'Peso normal'
                elif imc < 31:
                    diagnostico = 'Sobrepeso'
                elif imc < 41:
                    diagnostico = 'Obeso'
                else:
                    diagnostico = 'Obesidade mórbida'  
            else:
                if imc < 18.5:
                    diagnostico = 'Peso abaixo do normal'
                elif imc < 25:
                    diagnostico = 'Peso normal'
                elif imc < 30:
                    diagnostico = 'Sobrepeso'
                elif imc < 40:
                    diagnostico = 'Obesa'
                else:
                    diagnostico = 'Obesidade mórbida'
            
            print(f"Diagnóstico: {diagnostico}\n")

            # Objeto que será enviado para o banco.json no cadastro
            valores = {
                "nome": nome,
                "sexo": sexo,
                "peso": peso,
                "altura": altura,
                "imc": imc,
                "diagnostico": diagnostico
            }
    
            # Conexão do programa em python com o arquivo em json
            # Método "r+" para edição do arquivo
            with open('banco.json', 'r+') as banco:

                # Carrega os dados do json e armazena na variável "dados"
                dados = json.load(banco)

                # Incrementa o objeto "valores" no banco.json em "banco"
                dados["banco"].append(valores)

                # Localiza a posição 0 do arquivo json, definindo onde os dados serão incrementados
                banco.seek(0)
                
                # Formata o arquivo 
                json.dump(dados, banco, indent=4)

    # Conexão com o arquivo json, puxando os cadastros já existentes
    with open('banco.json', 'r+') as banco:
        cadastrados = json.load(banco)

    # Variáveis para o cálculo da média 
    # Info do total dos cadastrados
    contador = 0
    media_peso = 0
    media_altura = 0
    media_imc = 0
    
    # Info apenas dos cadastrados do sexo masculino
    media_peso_m = 0
    media_altura_m = 0
    media_imc_m = 0
    total_m = 0
    
    # Info apenas dos cadastrados do sexo feminino
    media_peso_f = 0
    media_altura_f = 0
    media_imc_f = 0
    total_f = 0
    
    # Varredura dos dados no banco 
    for x in cadastrados["banco"]:
        usuario = cadastrados["banco"][contador]

        media_peso += usuario["peso"]
        media_altura += usuario["altura"]
        media_imc += usuario["imc"]

        if usuario["sexo"] == 'm':
            media_peso_m += usuario["peso"]
            media_altura_m += usuario["altura"]
            media_imc_m += usuario["imc"]
            total_m += 1
        else:
            media_peso_f += usuario["peso"]
            media_altura_f += usuario["altura"]
            media_imc_f += usuario["imc"]
            total_f += 1

        contador+=1

    # Cálculos da média dos cadastrados
    media_peso = round(media_peso/(contador),2)
    media_altura = round(media_altura/(contador),2)
    media_imc = round(media_imc/(contador),2)
    total_cadastros = total_m + total_f

    media_peso_m = round(media_peso_m/(total_m),2)
    media_altura_m = round(media_altura_m/(total_m),2)
    media_imc_m = round(media_imc_m/(total_m),2)


    media_peso_f = round(media_peso_f/(total_f),2)
    media_altura_f = round(media_altura_f/(total_f),2)
    media_imc_f = round(media_imc_f/(total_f),2)

    # Variável dos dados que serão exibidos
    tipo_exibicao = None
    media_peso_exibicao = None
    media_altura_exibicao = None
    media_imc_exibicao = None
    total_exibicao = None

    # Opção de visualizar média dos cadastrados
    ver_dados = None
    while ver_dados == None:
        ver_dados = input("Deseja ver os dados médios dos cadastrados? \033[93m[s/n]\033[0m: ")

        # Validação de escrita em 's' (sim) ou 'n' (não)
        if ver_dados != 's' and ver_dados != 'n':
            ver_dados = None
        elif ver_dados == 's':
            os.system('clear')

            # Opções de dados que deseja visualizar
            print("Quais dados você deseja ver?\n")
            print("\033[93m[1]\033[0m Todos os cadastrados")
            print("\033[93m[2]\033[0m Homens cadastrados")
            print("\033[93m[3]\033[0m Mulheres cadastrados \n")
            
            # Validação da seleção, verificando os algarismos 1, 2 e 3
            selecao = None
            while selecao == None:
                selecao = int(input("Digite o número de sua escolha:"))

                # Define quais dados serão exibidos
                if selecao != 1 and selecao != 2 and selecao != 3:
                    selecao = None
                elif selecao == 1:
                    tipo_exibicao = 'total'
                    media_peso_exibicao = media_peso
                    media_altura_exibicao = media_altura
                    media_imc_exibicao = media_imc
                    total_exibicao = total_cadastros
                elif selecao == 2:
                    tipo_exibicao = 'homens'
                    media_peso_exibicao = media_peso_m
                    media_altura_exibicao = media_altura_m
                    media_imc_exibicao = media_imc_m
                    total_exibicao = total_m
                elif selecao == 3:
                    tipo_exibicao = 'mulheres'
                    media_peso_exibicao = media_peso_f
                    media_altura_exibicao = media_altura_f
                    media_imc_exibicao = media_imc_f
                    total_exibicao = total_f

                # Exibição de dados selecionados
                os.system('clear')
                print(f"\n\033[01mMédia dos cadastrados: {tipo_exibicao}\033[0m\n")
                print(f"Total de cadastrados: {total_exibicao}")
                print(f"Peso médio: {media_peso_exibicao} kg")
                print(f"Altura média: {media_altura_exibicao} m")
                print(f"IMC médio: {media_imc_exibicao}")

    input("\nPressione Enter para reiniciar o programa...\n")

    os.system('clear')

