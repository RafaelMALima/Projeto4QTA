def IQA(q_i):
    w_i = [0,0.15,0.12,0.10,0.10,0.10,0.10,0.08,0.08,0.17]
    iqa_parcial =lambda q,i : q**w_i[i]
    iqa = 1
    for i in range(1,len(w_i)): iqa*= iqa_parcial(q_i[i-1], i)
    return iqa
