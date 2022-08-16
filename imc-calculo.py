import os
import json

os.system('cls')

while True:
    print("\n")
    print("\033[01mCálculo de Índice de Massa Corporal (IMC)\033[0m".center(40,"-"))
    print("\n")
    
    fazer_cadastro = None
    while fazer_cadastro == None:
        fazer_cadastro = input("Deseja fazer cadastro? [s/n]: ")
        if fazer_cadastro != 's' and fazer_cadastro != 'n':
            fazer_cadastro = None
        elif fazer_cadastro == 's':

            os.system('cls')
            print("\n")
            print('Cadastro'.center(40,'-'))

            nome = input("\nDigite seu nome de usuário: \n")
            sexo = None
            while sexo == None:
                sexo = input("Sexo [m/f]: ")
                if sexo != 'm' and sexo != 'f':
                    sexo = None

            peso = float(input("Quanto você pesa em Kg? (kg)\n"))
            altura = float(input("Qual a sua altura? (m)\n"))    



            imc = round(peso/(altura**2),2)
            print("\nO seu IMC é de {:.2f}\n".format(imc))
            
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

            valores = {
                "nome": nome,
                "sexo": sexo,
                "peso": peso,
                "altura": altura,
                "imc": imc,
                "diagnostico": diagnostico
            }
    
            with open('banco.json', 'r+') as banco:
                dados = json.load(banco)

                dados["banco"].append(valores)

                banco.seek(0)
                
                json.dump(dados, banco, indent=4);

    with open('banco.json', 'r+') as banco:
        cadastrados = json.load(banco)

    contador = 0;
    media_peso = 0;
    media_altura = 0;
    media_imc = 0;
    
    for x in cadastrados["banco"]:
        media_peso += cadastrados["banco"][contador]["peso"]
        media_altura += cadastrados["banco"][contador]["altura"]
        media_imc += cadastrados["banco"][contador]["imc"]
        contador+=1

    media_peso = round(media_peso/(contador+1),2)
    media_altura = round(media_altura/(contador+1),2)
    media_imc = round(media_imc/(contador+1),2)
    
    ver_dados = None
    while ver_dados == None:
        ver_dados = input("Deseja ver os dados dos cadastrados? [s/n]: ")
        if ver_dados != 's' and ver_dados != 'n':
            ver_dados = None
        elif ver_dados == 's':
            os.system('cls')
            print("\n\033[01mDados dos cadastrados\033[0m\n")
            print(f"Peso médio: {media_peso} kg")
            print(f"Altura média: {media_altura} m")
            print(f"IMC médio: {media_imc}")

    input("\nPressione Enter para reiniciar o programa...\n")

    os.system('cls')
