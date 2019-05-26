import math
import time
from sep_algo import sep_algo

start = time.time()

q=[]
l=[]
total_calls = 0

epsilon = 0.65 #epsilon here is basically the epsilon in epsilon-LS.
beta = 1/math.sqrt(2) #Set your beta here.
n = 4 #Set what bit function your f is.

backend = 'ibmq_qasm_simulator' #Set your backend here.
shots = 2048 #Set the number of shots here.

result = sep_algo(epsilon, beta, n, '0', backend, shots, total_calls)
total_calls = result['total_calls']
if result['condition']==True:
    q.append(0)
    #print(0, 'goes to Q.')
#else:
    #print(0, 'goes out.')

result = sep_algo(epsilon, beta, n, '1', backend, shots, total_calls)
total_calls = result['total_calls']
if result['condition']==True:
    q.append(1)
    #print(1, 'goes to Q.')
#else:
    #print(1, 'goes out.')

while True:
    if len(q)==0:
        print('No more structures with the set conditions.')
        break
    p = q.pop(0)
    p = list(str(p))
    p.append('0')
    p0 = ''.join(p)
    result = sep_algo(epsilon, beta, n, p0, backend, shots, total_calls)
    total_calls = result['total_calls']
    if result['condition']==True:
        if len(p)==n:
            l.append(p0)
            #print(p0, 'goes to L.')
        else:
            q.append(p0)
            #print(p0, 'goes to Q.')
    #else:
        #print(p0,'goes out.')
    p.pop()
    p.append('1')
    p1 = ''.join(p)
    result = sep_algo(epsilon, beta, n, p1, backend, shots, total_calls)
    total_calls = result['total_calls']
    if result['condition']==True:
        if len(p)==n:
            l.append(p1)
            #print(p1,'goes to L.')
        else:
            q.append(p1)
            #print(p1, 'goes to Q.')
    #else:
        #print(p1,'goes out.')

end = time.time()

print('The list is : ', l)
print('The total number of oracle calls made is ', total_calls)
print('The run time is ', end-start)
