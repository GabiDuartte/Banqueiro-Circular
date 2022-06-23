def circular(processos, quantum, tc):
    turnaround = [0] * len(processos)  

    tempo_atual = 0  
    while True:
        if sum(processos) <= 0:
            print("Finalizado")
            break
        else:
            for i in range(len(processos)):
                if processos[i] <= 0:

                    print(f"\nP{i} foi finalizado")

                elif processos[i] <= quantum:
                    tempo_atual += processos[i]
                    processos[i] -= processos[i]

                    print(f"\nP{i} executado")
                    print(f"Termino em {tempo_atual}")

                    if processos[i] == 0:
                        turnaround[i] = tempo_atual
                        print(f"Processo P{i} terminou em {tempo_atual}")
                
                        tempo_atual += tc

                else:
                    tempo_atual += quantum
                    processos[i] -= quantum

                    print(f"\nP{i} executado")
                    print(f"Termino em {tempo_atual}")
                    
                    tempo_atual += tc
                    turnaround[i] = tempo_atual

     

    print(f"Turnaround: {turnaround}")
    return turnaround


def tempoMedio(lista_de_processos, lista_de_tempos):
    resultado = sum(lista_de_tempos) / (len(lista_de_processos))
    print(f"Tempo Médio de Turnaround = {resultado:.2f}")


def main():
    
    qtd = int(input('Quantidade de processos: '))

    processos = list()

    for i in range(qtd):
        processo = int(input(f'Processo {i+1}: '))
        processos.append(processo)
    
    print(f'Processos: {processos}')
    quantum = int(input('\nQuantum: '))
    tc = int(input('\nTroca de contexto: '))

    turnAround = circular(processos, quantum, tc)
    tempoMedio(processos, turnAround)

    
main()

