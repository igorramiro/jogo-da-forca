import re
import os
erros=['/','\\','|','/','\\','|','O']
erro=[' ',' ',' ',' ',' ',' ',' ']
def corpo(letras,string):#define o corpo
    print(f'Letras usadas:{letras}\n',
      '  ________\n',
      '|        |\n',
      '|        |\n',
      f'|        {erro[6]}\n',
      f'|       {erro[3]}{erro[5]}{erro[4]}\n',
      f'|        {erro[2]}\n',
      f'|       {erro[0]} {erro[1]}\n',
      f'|      {re.sub("_", "_ ",string)}\n')

def partida():#inicia a partida
    vidas=7
    letras_usadas=''
    palavra=input("Palavra:")
    palavra_oculta=re.sub('[a-z]|[A-Z]', '_',palavra)# troca as letras por _
    os.system('cls')#apaga o console
    corpo(letras_usadas,palavra_oculta)
    while palavra_oculta!=palavra and vidas!=0:
        jogador_letra=input('Digite uma letra: ')
        acerto=0


        for i in range(len(palavra)):
            if jogador_letra.lower()==palavra[i] or jogador_letra.upper()==palavra[i]:
                aux = list(palavra_oculta)#transforma em lista
                aux[i] = palavra[i]
                palavra_oculta = "".join(aux)#une a lista
                acerto=1
            elif acerto==0 and i==(len(palavra)-1):
                erro[vidas-1]=erros[vidas-1]
                vidas-=1
        os.system('cls')
        letras_usadas+=jogador_letra + '-'
        corpo(letras_usadas,palavra_oculta)
    if palavra_oculta==palavra:
        print('Parabens, você ganhou')
    else: 
        print('Que pena, você perdeu')
    nova_partida=input('Nova partida(s/n)? ')
    os.system('cls')
    if nova_partida.lower()=='s':
        partida()
partida()
