from qiskit import *

from four_bit_oracles import oracle_1, oracle_2, oracle_3
from four_bit_oracles import oracle_4, oracle_5, oracle_6


######## Setting up a with a certain prefix ######
def pre_circuit(qc,q,n,pre):
    if len(pre)==0:
        pre_int=[]
    else:
        prefix = list(str(pre))
        pre_int=[]
        for i in range(len(prefix)):
            pre_int.append(int(prefix[i]))

    for j in range(n, n+len(pre_int)):
        if pre_int[j-n]==1:
            qc.x(q[j])

    for j in range(n+len(pre_int), 2*n):
        qc.h(q[j])
###################################################


def hodjk(qc, q, n, pre):
    
    for i in range(n):
        qc.h(q[i])

    pre_circuit(qc,q,n,pre)

    oracle_6(qc,q,0,1,2,3)
    
    #CNOT between a and x.
    for i in range(n,2*n):
        qc.cx(q[i], q[i-n])

    oracle_6(qc,q,0,1,2,3)
    
    #CNOT reversed.
    for i in range(n,2*n):
        qc.cx(q[i], q[i-n])

    for i in range(n):
        qc.h(q[i])

    #return qc

def hodjk_inv(qc, q, n,pre):
    for i in range(n):
        qc.h(q[i])

    for i in range(n,2*n):
        qc.cx(q[i], q[i-n])

    oracle_6(qc,q,0,1,2,3)

    for i in range(n,2*n):
        qc.cx(q[i], q[i-n])

    oracle_6(qc,q,0,1,2,3)

    pre_circuit(qc,q,n,pre)
    
    for i in range(n):
        qc.h(q[i])

    #return qc
