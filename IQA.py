def IQA(q_i):
    w_i = [0,0.15,0.12,0.10,0.10,0.10,0.10,0.08,0.08,0.17]
    iqa_parcial =lambda q,i : q**w_i[i]
    iqa = 1
    for i in range(1,len(w_i)): iqa*= iqa_parcial(q_i[i-1], i)
    return iqa

#1. Linha de tendência para definir q[Coliformes]
def Coliformes(x):
    if x > 1e5:
        return 3
    if x <21:
        return 6.17e-6*x**6 - 5.34e-4*x**5 + 1.83e-2*x**4 - 3.18e-1*x**3 + 3.01*x**2 - 1.64e1*x + 110
    if x<101:
        return 0.0019*x**2 - 0.4252*x + 62.238
    if x<882:
        return -6.15e-8*x**3 + 1.2e-4*x**2 - 8.71e-2*x + 45.5
    if x<10448:
        return 8.59e-15*x**4 - 2.27e-10*x**3 + 2.19e-6*x**2 - 9.81e-3*x + 26.4
    return -4.67e-28*x**6 + 1.64e-22*x**5 - 2.26e-17*x**4 + 1.52e-12*x**3 - 5e-8*x**2 + 6.44e-4*x - 3.14

#2. Linha de tendência para definir q[pH]
def pH(x):
    if x<2:
        return 2
    if x>12:
        return 3
    if x<7:
        return - 0.0276*x**6 + 0.7266*x**5 - 7.7866*x**4 + 44.327*x**3 - 139.41*x**2 + 229.58*x-152.35
    if x>=7:
        return 0.0915*x**6 - 5.4509*x**5 + 133.54*x**4 - 1720.5*x**3 + 12280*x**2 - 46009*x + 70788
    
#3. Linha de tendência para definir q[DBO]
def DBO(x):
    if x >30:
        return 2
    return -6.89e-7*(x**6) + 7.09e-5*(x**5) - 2.58e-3*(x**4) + 3.34e-2*(x**3) + 0.211*(x**2) - 10.8*(x) + 104.7

#4. Linha de Tendência para definir q[NTotal]
def NTotal(x):
    if x>100:
        return 1
    return 6e-6*x**4 - 0.0015*x**3 + 0.1246*x**2 - 4.9171*x + 91.755

#5. Linha de Tendência para definir q[Ptotal]


def PTotal(x):
    if x>10:
        return 1
    return 0.0045*x**6 - 0.1502*x**5 + 1.9786*x**4 - 13.066*x**3 + 45.86*x**2 - 86.143*x + 91.32

#6. Linha de Tendência para definir q[Temp]
def Temp(x):
    if x<-5:
        return 1
    if x>15:
        return 9
    return 0.0001*(x**6) - 0.0047*(x**5) + 0.0397*(x**4) + 0.1473*(x**3) - 2.7079*(x**2) - 1.4269*x + 90.443

#7. Linha de Tendência para definir q[Turbidez]
def Turbidez(x):
    if x>100:
        return 5
    return -0.0001*x**3 + 0.0221*x**2 - 1.9571*x + 93.383


#8. Linha de Tendência para definir q[ResTotal]
def ResTotal(x):
    if x>500:
        return 32
    return 6e-7*x**3 - 0.0006*x**2 + 0.0475*x + 84.371

#9. Linha de Tenderência para definir q[O2]
def O2(x):
    if x>140:
        return 47
    return -3.95e-11*x**6 + 5.08e-08*x**5 - 1.41e-05*x**4 + 1.37e-03*x**3 - 4.38e-2*x**2 + 1.06*x + 1.36