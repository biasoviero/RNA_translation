class Automato:
    def __init__(self, estados, alfabeto, q0, fim, transicoes):
        self.estados = estados
        self.alfabeto = alfabeto
        self.q0 = q0
        self.fim = fim
        self.transicoes = transicoes
        self.atual = q0
        self.ACEITA = [False, 'ACEITA!']

        # Verifica se aceita palavra vazia
        if q0 in fim:
            self.ACEITA[0] = True

        # Casos onde a entrada é rejeitada
        self.NAO_FINAL = [not(self.ACEITA), 'REJEITA! Atingiu estado não final! O códon de parada não foi lido']
        self.INDEFINIDO = [False, lambda s, c: f'REJEITA! O aminoácido {s} não é codificado pelo códon {c}']
        self.ALFABETO = [False, lambda s: f'REJEITA! O símbolo {s} não está contido no alfabeto']
        self.ERRADO = False
        
    # A função avalia o símbolo fornecido pelos usuário e, caso eles sejam válidos, muda para a próximo estado
    # argumentos sigla e codon são utilizados quando é lido um aminoácido, nesse caso sigla=True e codon=códon que o codifica
    def step(self, simbolo, sigla = False, codon = None):
        if simbolo not in alfabeto: # Se o símbolo lido não está no alfabeto, informa ao usuário sobre esse erro e encerra a leitura da entrada
            self.ALFABETO[0] = True
            print(self.ALFABETO[1](simbolo))
            self.ERRADO = True
            return

        #proxEstado = None significa transição indefinida
        try:
            proxEstado = self.transicoes[(self.atual, simbolo)] 
        except KeyError:
            proxEstado = None

        # Caso o próximo estado não exista, informa ao usuário e encerra a leitura da entrada
        if proxEstado is None:
            self.INDEFINIDO[0] = True
            if sigla: print(self.INDEFINIDO[1](simbolo, codon))
            else: print('REJEITA! Transição indefinida')
            self.ERRADO = True
            return

        # Se o próximo estado não é de fim, continua a leitura
        if proxEstado not in self.fim:
            self.NAO_FINAL[0] = True

        # Se o próximo estado é de fim, a entrada é aceita    
        if proxEstado in self.fim:
            self.ACEITA[0] = True
            return
        
        if sigla:
            print(f'Códon {codon} e aminoácido {simbolo}: OK')
        self.atual = proxEstado
        

# Configurações do autômoto do sistema
estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47']
alfabeto = ['U', 'C', 'A', 'G', 'Phe', 'Leu', 'Ser', 'Tyr', 'Cys', 'Trp', 'Pro', 'His', 'Gln', 'Arg', 'Ile', 'Thr', 'Asn', 'Lys', 'Val', 'Ala', 'Asp', 'Glu', 'Gly']
estadoInicial = 'q0'
estadosFinais = ['q28', 'q30']
transicoes = {
    ('q0', 'A') : 'q1',
    ('q1', 'U') : 'q2',
    ('q2', 'G') : 'q3',
    ('q3', 'U') : 'q4',
    ('q3', 'C') : 'q5',
    ('q3', 'A') : 'q6',
    ('q3', 'G') : 'q7',
    ('q4', 'U') : 'q8',
    ('q4', 'C') : 'q9',
    ('q4', 'A') : 'q10',
    ('q4', 'G') : 'q11',
    ('q5', 'U') : 'q12',
    ('q5', 'C') : 'q13',
    ('q5', 'A') : 'q14',
    ('q5', 'G') : 'q15',
    ('q6', 'U') : 'q16',
    ('q6', 'C') : 'q17',
    ('q6', 'A') : 'q18',
    ('q6', 'G') : 'q19',
    ('q7', 'U') : 'q20',
    ('q7', 'C') : 'q21',
    ('q7', 'A') : 'q22',
    ('q7', 'G') : 'q23',
    ('q8', 'U') : 'q24',
    ('q8', 'C') : 'q24',
    ('q8', 'A') : 'q25',
    ('q8', 'G') : 'q25',
    ('q9', 'U') : 'q26',
    ('q9', 'C') : 'q26',
    ('q9', 'A') : 'q26',
    ('q9', 'G') : 'q26',
    ('q10', 'U') : 'q27',
    ('q10', 'C') : 'q27',
    ('q10', 'A') : 'q28',
    ('q10', 'G') : 'q28',
    ('q11', 'U') : 'q29',
    ('q11', 'C') : 'q29',
    ('q11', 'A') : 'q30',
    ('q11', 'G') : 'q31',
    ('q12', 'U') : 'q32',
    ('q12', 'C') : 'q32',
    ('q12', 'A') : 'q32',
    ('q12', 'G') : 'q32',
    ('q13', 'U') : 'q33',
    ('q13', 'C') : 'q33',
    ('q13', 'A') : 'q33',
    ('q13', 'G') : 'q33',
    ('q14', 'U') : 'q34',
    ('q14', 'C') : 'q34',
    ('q14', 'A') : 'q35',
    ('q14', 'G') : 'q35',
    ('q15', 'U') : 'q36',
    ('q15', 'C') : 'q36',
    ('q15', 'A') : 'q36',
    ('q15', 'G') : 'q36',
    ('q16', 'U') : 'q37',
    ('q16', 'C') : 'q37',
    ('q16', 'A') : 'q37',
    ('q17', 'U') : 'q38',
    ('q17', 'C') : 'q38',
    ('q17', 'A') : 'q38',
    ('q17', 'G') : 'q38',
    ('q18', 'U') : 'q39',
    ('q18', 'C') : 'q39',
    ('q18', 'A') : 'q40',
    ('q18', 'G') : 'q40',
    ('q19', 'U') : 'q41',
    ('q19', 'C') : 'q41',
    ('q19', 'A') : 'q42',
    ('q19', 'G') : 'q42',
    ('q20', 'U') : 'q43',
    ('q20', 'C') : 'q43',
    ('q20', 'A') : 'q43',
    ('q20', 'G') : 'q43',
    ('q21', 'U') : 'q44',
    ('q21', 'C') : 'q44',
    ('q21', 'A') : 'q44',
    ('q21', 'G') : 'q44',
    ('q22', 'U') : 'q45',
    ('q22', 'C') : 'q45',
    ('q22', 'A') : 'q46',
    ('q22', 'G') : 'q46',
    ('q23', 'U') : 'q47',
    ('q23', 'C') : 'q47',
    ('q23', 'A') : 'q47',
    ('q23', 'G') : 'q47',
    ('q24', 'Phe') : 'q3',
    ('q25', 'Leu') : 'q3',
    ('q26', 'Ser') : 'q3',
    ('q27', 'Tyr') : 'q3',
    ('q29', 'Cys') : 'q3',
    ('q31', 'Trp') : 'q3',
    ('q32', 'Leu') : 'q3',
    ('q33', 'Pro') : 'q3',
    ('q34', 'His') : 'q3',
    ('q35', 'Gln') : 'q3',
    ('q36', 'Arg') : 'q3',
    ('q37', 'Ile') : 'q3',
    ('q38', 'Thr') : 'q3',
    ('q39', 'Asn') : 'q3',
    ('q40', 'Lys') : 'q3',
    ('q41', 'Ser') : 'q3',
    ('q42', 'Arg') : 'q3',
    ('q43', 'Val') : 'q3',
    ('q44', 'Ala') : 'q3',
    ('q45', 'Asp') : 'q3',
    ('q46', 'Glu') : 'q3',
    ('q47', 'Gly') : 'q3',

}
print("\n")
print("                     SIMULAÇÃO DO PROCESSO DE TRADUÇÃO DO RNA\n")


while True: 

    modo = int(input("\nDigite\n (1) para leitura pelo terminal\n (2) para leitura de arquivo\n (3) para encerrar o programa\n"))
    codon = ''
    # Modo 1 (leitura pelo terminal)
    if modo == 1:
        aviso = 'Para que a entrada seja aceita, siga as instruções abaixo: \n \
                1 - Digite o códon de início; \n \
                2 - Na linha seguinte, escreva um códon; \n \
                3 - Na próxima linha, o aminoácido correspondente; \n \
                4 - Repita os passos 2 e 3 quantas vezes forem necessárias; \n \
                5 - Digite um códon de parada.\n'
        print(aviso)
        print("Para encerrar a leitura pule uma linha (tecle duas vezes seguidas no Enter)")

        afd = Automato(estados, alfabeto, estadoInicial, estadosFinais, transicoes) # Inicializa o autômato
        while True:
            # Recebe um códon ou uma sigla em cada linha do terminal
            entrada = input()

            if not entrada: # Caso a entrada seja vazia, termina a leitura
                break

            if entrada not in alfabeto: # Caso a entrada seja um códon, avalia se cada letra(base) está no alfabeto
                for i in entrada:   
                    afd.step(i)
                    if afd.ERRADO: # Se houve um erro na leitura do códon, acaba esse processo
                        break
                if not(afd.ERRADO):
                    codon = entrada
                    if codon == 'AUG': print('Códon de ínicio: OK')
                    elif codon in ['UAA', 'UAG', 'UGA']: print(f'Códon de fim {codon}: OK')
                    else: print(f'Códon {codon}: OK')
            else: # Caso seja uma sigla, avalia se corresponde ao códon recebido na linha anterior
                afd.step(entrada, True, codon)

            if afd.ERRADO or afd.ACEITA[0]: # Se houve um erro na leitura da entrada ou a entrada é aceita, acaba esse processo
                break 
                
        if not afd.ACEITA[0] and not afd.ERRADO: # Se a leitura terminou e ela não foi aceita e não apresentou erros, o último estado não é final
            print(afd.NAO_FINAL[1])

        elif afd.ACEITA[0]: # Se a leitura chegou ao fim, não teve erros e está num estado final, a entrada é aceita
            print(afd.ACEITA[1])
        codon = ''

            

    # Modo 2 (leitura de arquivo)
    elif modo == 2:
        nome_arquivo = input("Digite o caminho do arquivo: ")

        try:
            # Abre o arquivo informado pelo usuário e faz sua leitura
            with open(nome_arquivo, 'r') as arquivo:
                entrada = arquivo.read()
                entrada = entrada.replace(',', '')
    
                afd = Automato(estados, alfabeto, estadoInicial, estadosFinais, transicoes) # Inicializa o autômato

                trios = [entrada[i:i+3] for i in range(0, len(entrada), 3)] # Cria uma lista onde cada elemento é formado por 3 caracteres da entrada

                # Percorre a lista dos grupos de 3 caracteres
                for s in trios: 
                    if s in alfabeto: # Caso esses 3 caracteres juntos estejam dentro do alfabeto, esse grupo representa um sigla
                        afd.step(s, True, codon)
                    else: # Caso contrário, é um códon
                        # Como a entrada é um códon, avalia cada letra(base)
                        codon = ''
                        for i in s:
                            afd.step(i)
                            codon += i
                        if not(afd.ERRADO):
                            if codon == 'AUG': print('Códon de ínicio: OK')
                            elif codon in ['UAA', 'UAG', 'UGA']: print(f'Códon de fim {codon}: OK')
                            else: print(f'Códon {codon}: OK')

                    if afd.ERRADO or afd.ACEITA[0]: # Se houve um erro na leitura da entrada ou a entrada é aceita, acaba esse processo
                        break

                if not afd.ACEITA[0] and not afd.ERRADO: # Se a leitura terminou e ela não foi aceita e não apresentou erros, o último estado não é final
                    print(afd.NAO_FINAL[1])

                elif afd.ACEITA[0]: # Se a leitura chegou ao fim, não teve erros e está num estado final, a entrada é aceita
                    print(afd.ACEITA[1])

            arquivo.close()

        # Casos de erro na abertura e leitura do arquivo         
        except FileNotFoundError:
                print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        except Exception as e:
                print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
        codon = ''


    # modo 3 (encerra o programa)
    elif modo == 3:
        break


   