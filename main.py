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

        self.NAO_FINAL = [not(self.ACEITA), 'REJEITA! Atingiu estado não final']
        self.INDEFINIDO = [False, 'REJEITA! Transição indefinida']
        self.ALFABETO = [False, 'REJEITA! Símbolo não contido no alfabeto']
        self.ERRADO = False

    def reset(self):
        self.atual = self.q0

    def step(self, simbolo):
        if simbolo not in alfabeto:
            self.ALFABETO[0] = True
            print(self.ALFABETO[1])
            self.ERRADO = True
            return
        
        if self.atual in self.fim:
            self.ACEITA[0] = True
            return

        try:
            proxEstado = self.transicoes[(self.atual, simbolo)]
        except KeyError:
            proxEstado = None

        if proxEstado is None:
            self.INDEFINIDO[0] = True
            print(self.INDEFINIDO[1])
            self.ERRADO = True
            return

        if proxEstado not in self.fim:
            self.NAO_FINAL[0] = True

        self.atual = proxEstado

        # if self.ACEITA[0]:
        #     print(self.ACEITA[1])
        # else:
        #     print(self.NAO_FINAL[1])
        


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

afd = Automato(estados, alfabeto, estadoInicial, estadosFinais, transicoes)
teste = 'AUGGUUValCGAArgUAUTyrACUThrGUAValGGGGlyCUULeuAAALysCCCProUAA'

for s in teste:
    afd.step(s)
    if afd.ERRADO:
        break
if not afd.ERRADO:
    print(afd.ACEITA[1])

# elif afd.NAO_FINAL[0]:
#     print(afd.NAO_FINAL[1])

# ACEITA = atingiu estado final
# REJEITA - última letra parou em um estado não final
# REJEITA - transição não definida
# REJEITA - não está no alfabeto

# rejeitar palaavra vazia