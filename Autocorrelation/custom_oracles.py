'''This file contains oracles for a few 4-bit Boolean functions.
The oracles take "qc", "q", "top" and "anc" as arguments. "qc" is the quantum 
circuit, "q" is the qubits currently working on, "top" is the number of 
the topmost qubit of the set of qubits on which the oracle needs to be 
implemented and "anc" are the ancilliary qubits.'''


from qiskit import *

def oracle1(qc,q,top,anc):
    '''This is the oracle for the 4-bit constant
    function f(x)=0.'''


def oracle2(qc,q,top,anc):
    '''This is the oracle for the 4-bit function
    whose truth table vector is 
    f = [1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 1]'''

    qc.cz(q[top],q[top+3])

    qc.x(q[top])
    qc.cz(q[top],q[top+3])
    qc.x(q[top])

    qc.x(q[top+1])
    qc.ccx(q[top+1],q[top+2],anc[0])
    qc.cz(anc[0],q[top+3])
    qc.ccx(q[top+1],q[top+2],anc[0])
    qc.x(q[top+1])

    qc.cx(q[top],q[top+1])
    qc.x(q[top+3])
    qc.ccx(q[top+3],q[top+2],anc[0])
    qc.cx(anc[0],q[top+1])
    qc.ccx(q[top+3],q[top+2],anc[0])
    qc.x(q[top+3])
    qc.cx(q[top],q[top+1])


def oracle3(qc,q,top,anc):
    '''This is the oracle for the 4-bit function
    whose truth table vector is 
    f = [1 0 1 1 0 0 1 1 1 0 0 0 1 1 0 0]'''

    qc.x(q[top])
    qc.cz(q[top],q[top+2])
    qc.x(q[top])

    qc.x(q[top+2])
    qc.x(q[top+3])
    qc.cz(q[top+2],q[top+3])
    qc.x(q[top+3])
    qc.x(q[top+2])

    qc.x(q[top+2])
    qc.cx(q[top],q[top+3])
    qc.x(q[top+3])
    qc.ccx(q[top+1],q[top+2],anc[0])
    qc.cz(anc[0],q[top+3])
    qc.ccx(q[top+1],q[top+2],anc[0])
    qc.x(q[top+3])
    qc.cx(q[top],q[top+3])
    qc.x(q[top+2])


def oracle4(qc,q,top,anc):
    '''This is the oracle for the 4-bit function 
    f(x)=x1x2+x3x4.'''

    qc.cz(q[top],q[top+1])
    qc.cz(q[top+2],q[top+3])


def oracle5(qc,q,top,anc):
    '''This is the oracle for the 4-bit function 
    whose truth table vector is 
    f=[0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0]'''

    qc.x(q[top+2])
    qc.cx(q[top],q[top+1])
    qc.x(q[top+1])
    qc.cz(q[top+1],q[top+2])
    qc.x(q[top+1])
    qc.cx(q[top],q[top+1])
    qc.x(q[top+2])


def oracle6(qc,q,top,anc):
    '''This is the oracle for the 4-bit function 
    whose truth table vector is 
    f = [1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 0]'''

    qc.x(q[top])
    qc.x(q[top+3])
    qc.cz(q[top],q[top+3])
    qc.x(q[top+3])

    qc.cx(q[top+3],q[top+1])
    qc.ccx(q[top],q[top+1],anc[0])
    qc.cz(anc[0],q[top+2])
    qc.ccx(q[top],q[top+1],anc[0])
    qc.cx(q[top+3],q[top+1])
    qc.x(q[top])

    qc.x(q[top+2])
    qc.ccx(q[top],q[top+2],anc[0])
    qc.cz(anc[0],q[top+3])
    qc.ccx(q[top],q[top+2],anc[0])
    qc.x(q[top+2])

    qc.x(q[top+1])
    qc.x(q[top+3])
    qc.ccx(q[top],q[top+1],anc[0])
    qc.ccx(q[top+2],anc[0],anc[1])
    qc.cz(anc[1],q[top+3])
    qc.ccx(q[top+2],anc[0],anc[1])
    qc.ccx(q[top],q[top+1],anc[0])
    qc.x(q[top+3])
    qc.x(q[top+1])
