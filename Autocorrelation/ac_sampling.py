'''     This is a quantum circuit for estimating the A.C Coefficients 
   of a 4 bit boolean function. 
        Here we suppose that the first four qubits as the first 
    register and the second four qubits as the second register. 
        In this program we first create a quantum circuit such that
    the final state produced is a superposition in such a way that 
    if on measuring the first register we get zero, then the post
    measurement state has amplitudes proportional to the respective
    A.C Coefficients.
        Finally we print only the outputs that are accepted, ie., the
    outputs whose first register is zero'''


from qiskit import *
from qiskit.tools.monitor import job_monitor
from custom_oracles import oracle1, oracle2, oracle3
from custom_oracles import oracle4, oracle5, oracle6



#Setting up API.

'''Set up the IBMQ account API token.'''

IBMQ.save_account('PLEASE_INPUT_YOUR_API_TOKEN_HERE', overwrite=True)
IBMQ.load_accounts()

n = int(input('Please enter the number of bits of the function : '))
shots = 2048
backend = IBMQ.get_backend('ibmq_qasm_simulator')


#Setting up registers and creating a circuit.

q = QuantumRegister(2*n)
anc = QuantumRegister(n-2)
c = ClassicalRegister(2*n)
qc = QuantumCircuit(q,c)


#Building the circuit.

'''Building the sampling circuit.'''

for i in range(2*n):
    qc.h(q[i])
oracle1(qc,q,0,anc)
for j in range(n):
    qc.cx(q[j],q[j+n])
oracle1(qc,q,0,anc)
for j in range(n):
    qc.cx(q[j],q[j+n])

qc.measure(q,c)


#Executing the circuit and getting the result.

qjob = execute(qc, shots=shots, backend=backend)
job_monitor(qjob)
result = qjob.result()
stats = result.get_counts()
#print(stats)


#Printing the selected outputs.

bitstring = []
for i in range(int(pow(2,n))):
    bitstring.append(bin(i)[2:].zfill(2*n))

count = 0
for string in bitstring:
    if string in stats:
        count += stats[string]

for string in bitstring:
    if string in stats:
        print(str(string) + ' : ' + str(round(stats[string]/count,6)))
    else:
        print(str(string) + ' + ' + str(0))
