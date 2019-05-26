from qiskit import *

from hodjk import hodjk, hodjk_inv
#from simple_oracle import simple_oracle, simple_oracle_inv

def amp_amp(qc, q, n,pre):
    def s_0(qc,q,n):
        if n>2:
            for i in range(2*n):
                qc.x(q[i])
            qc.ccx(q[0],q[1],q[2*n])
            for i in range((2*n)-3):
                qc.ccx(q[i+2],q[(2*n)+i],q[(2*n)+i+1])
            qc.cz(q[(4*n)-3], q[(2*n)-1])
            for i in reversed(range((2*n)-3)):
                qc.ccx(q[i+2],q[(2*n)+i],q[(2*n)+i+1])
            qc.ccx(q[0],q[1],q[2*n])
            '''qc.ccx(q[0],q[1],q[8])
            qc.ccx(q[2],q[8],q[9]))
            qc.cz(q[9],q[3])
            qc.ccx(q[2],q[8],q[9])
            qc.ccx(q[0],q[1],q[8])'''
            for i in range(2*n):
                qc.x(q[i])
        elif n==1:
            qc.x(q[0])
            qc.z(q[0])
            qc.x(q[0])
        else:
            qc.x(q[0])
            qc.x(q[1])
            qc.cz(q[0],q[1])
            qc.x(q[1])
            qc.x(q[0])
        #return qc
    
    def s_good(qc,q,n):
        for i in range(n):
            qc.x(q[i])
        qc.ccx(q[0],q[1],q[8])
        qc.ccx(q[2],q[8],q[9])
        qc.cz(q[9],q[3])
        qc.ccx(q[2],q[8],q[9])
        qc.ccx(q[0],q[1],q[8])
        for i in range(n):
            qc.x(q[i])
        #return qc

    def minus(qc,q,n):
        qc.x(q[2*n])
        qc.z(q[2*n])
        qc.x(q[2*n])
        #return qc


    s_good(qc,q,n) 
    hodjk_inv(qc,q,n,pre) 
    s_0(qc,q,n) 
    hodjk(qc,q,n,pre)

    return qc
