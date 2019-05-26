def oracle_1(qc,q,*a):
    
    '''This is the oracle for the 4-bit 
    constant function f(x)=0'''

    #Nothing happens here.



def oracle_2(qc,q,*a):
    
    '''This is the oracle for the 4-bit
    balanced function whose output values 
    are f=[1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 1]'''

    qc.x(q[a[1]])
    qc.x(q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.x(q[a[3]])
    qc.x(q[a[1]])

    qc.x(q[a[0]])
    qc.x(q[a[2]])
    qc.x(q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.x(q[a[3]])
    qc.x(q[a[2]])
    qc.x(q[a[0]])

    qc.cx(q[a[0]],q[a[1]])
    qc.x(q[a[1]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.x(q[a[1]])
    qc.cx(q[a[0]],q[a[1]])

    qc.x(q[a[2]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.x(q[a[2]])




def oracle_3(qc,q,*a):

    '''This is the oracle for the 4-bit 
    balanced function whose output values
    are f=[1 0 1 1 0 0 1 1 1 0 0 0 1 1 0 0]'''

    qc.x(q[a[1]])
    qc.x(q[a[2]])
    qc.x(q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.x(q[a[3]])
    qc.x(q[a[2]])
    qc.x(q[a[1]])

    qc.x(q[a[0]])
    qc.cz(q[a[0]],q[a[2]])
    qc.x(q[a[0]])

    qc.x(q[a[2]])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.cz(q[8],q[a[2]])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.x(q[a[2]])




def oracle_4(qc,q,*a):

    '''This is the oracle for the 4-bit
    bent function f(x)=x1x2+x3x4.'''

    qc.x(q[a[0]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.x(q[a[0]])

    qc.x(q[a[3]])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.x(q[a[3]])

    qc.cx(q[a[1]],q[a[2]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cx(q[a[1]],q[a[2]])



def oracle_5(qc,q,*a):

    '''This is the oracle for the 4-bit
    function whose functional values are
    f=[0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0]'''

    qc.cx(q[a[0]],q[a[1]])
    qc.cx(q[a[0]],q[a[3]])
    qc.x(q[a[1]])
    qc.x(q[a[2]])
    qc.ccx(q[a[1]],q[a[3]],q[8])
    qc.cz(q[8],q[a[2]])
    qc.ccx(q[a[1]],q[a[3]],q[8])
    qc.x(q[a[2]])
    qc.x(q[a[1]])
    qc.cx(q[a[0]],q[a[3]])
    qc.cx(q[a[0]],q[a[1]])



def oracle_6(qc,q,*a):

    '''This is the oracle for the 4-bit
    function whose functional values are
    f=[1 0 1 1 1 0 0 0 0 1 1 0 0 1 0 0]'''

    qc.x(q[a[0]])
    qc.x(q[a[2]])
    qc.x(q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.x(q[a[3]])
    qc.x(q[a[2]])
    qc.x(q[a[0]])

    qc.x(q[a[1]])
    qc.x(q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[1]],q[a[2]],q[8])
    qc.x(q[a[3]])
    qc.x(q[a[1]])

    qc.x(q[a[2]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.cz(q[8],q[a[3]])
    qc.ccx(q[a[0]],q[a[2]],q[8])
    qc.x(q[a[2]])

    qc.x(q[a[0]])
    qc.x(q[a[1]])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.ccx(q[a[2]],q[8],q[9])
    qc.cz(q[9],q[a[3]])
    qc.ccx(q[a[2]],q[8],q[9])
    qc.ccx(q[a[0]],q[a[1]],q[8])
    qc.x(q[a[1]])
    qc.x(q[a[0]])
