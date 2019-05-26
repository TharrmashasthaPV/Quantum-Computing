import math
import time
from qiskit import *

from amp_amplification import amp_amp
from hodjk import hodjk


IBMQ.save_account('65e49d091cff358f401736a36dd72a4ea138e37b138e89e84c217e8fa252348b9ec143b8b407a897cbd97c544ccccc47a984b3301a280a018ae77424b5d1a113', overwrite=True)
IBMQ.load_accounts()


def sep_algo(eps, beta, n, pre, backend, shots, total_calls):
    machine = IBMQ.get_backend(backend)
    total_calls = total_calls
    #print('pre is', pre) 
    t = (((2*eps)-1)**2)/(2**(n-len(pre)))
    tau = math.asin(math.sqrt(t))
    #print('tau is', tau)
    if tau>(math.pi/12):
        s = 0
    else:
        s = math.floor(math.log((math.pi/(4*tau)),3))
    #print('S is', s)
    epsilon = (3**s)*tau*(1+beta)/2
    #print('epsilon is', epsilon)
    m = (math.sin(epsilon))**2
    #print('threshold: ',m)
    condition = False

    good = ['0']*n
    good = ''.join(good)

    if tau>math.pi/12:
        q = QuantumRegister(4*n)
        c = ClassicalRegister(n)
        qc = QuantumCircuit(q,c)

        hodjk(qc,q,n,pre)

        for j in range(n):
            qc.measure(q[j],c[n-j-1])
        qjob =execute(qc, backend=machine, shots=shots)
        
        calls = 2*shots
        total_calls += calls
        
        result = qjob.result()
        stats = result.get_counts()
        #print('stats is', stats)
        
        try:
            if (stats[good]/shots) >= (math.sin(epsilon))**2:
                #print(stats['000'/shots])
                condition = True
                return {'condition': condition, 'total_calls': total_calls}
        except:
            pass
    else:
        k=[None]*10
        for i in range(s+1):
            q = QuantumRegister(4*n)
            c = ClassicalRegister(n)
            qc = QuantumCircuit(q,c)
            
            #print('i is:',i)
            k[i]=((3**i)-1)/2
            #print('ki is',k[i])
            if k[i]==0:
                hodjk(qc,q,n,pre)
                for j in range(n):
                    qc.measure(q[j],c[n-j-1])
                qjob =execute(qc, backend=machine, shots=shots)
                
                calls = 2*shots
                total_calls+=calls
                
                result = qjob.result()
                stats = result.get_counts()
                #print(stats)
                
                try:
                    if (stats[good]/shots) >= (math.sin(epsilon))**2:
                        condition = True
                        return {'condition': condition, 'total_calls': total_calls}
                except:
                    pass
            else:
                hodjk(qc,q,n,pre)
                circ = [None]*int(k[i])
                #circ = amp_amp(circ1,q,n)
                circ[0] = amp_amp(qc, q, n, pre)
                
                for j in range(1,int(k[i])):
                    circ[j] = amp_amp(circ[j-1],q,n,pre)
                for j in range(n):
                    circ[int(k[i])-1].measure(q[j],c[n-j-1])
                    #circ.measure(q[j],c[n-j-1])
                qjob = execute(circ[int(k[i])-1], backend=machine, shots=shots)
                
                calls = (4*k[i]+2)*shots
                total_calls+=calls
                
                result = qjob.result()
                stats = result.get_counts()
                #print(stats)
                
                try:
                    if (stats[good]/shots) >= (math.sin(epsilon))**2:
                        condition = True
                        return {'condition': condition, 'total_calls': total_calls}
                        break
                except:
                    pass
    return {'condition': condition, 'total_calls': total_calls}
