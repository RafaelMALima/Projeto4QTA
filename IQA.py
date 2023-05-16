def IQA(qi,wi):
    iqa=1 # Índice de Qualidade das Águas, um número entre 0 e 100;
    # qi [i]: qualidade do i-ésimo parâmetro, um número entre 0 e 100, obtido da respectiva “curva média devariação de qualidade”, em função de sua concentração ou medida
    # wi [i]: peso correspondente ao i-ésimo parâmetro, um número entre 0 e 1, atribuído em função da sua importância para a conformação global de qualidade
    for i in range(0,i):
        iqa*=qi[i]**wi[i]
        
    return iqa
