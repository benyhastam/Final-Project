f= open ("output.txt",'w')
import numpy as np

def convolution(signal, filter):
    filter_size = len(filter)
    result = np.zeros(len(signal) + filter_size - 1)
    for i in range(len(signal) + filter_size - 1):
        for j in range(filter_size):
            if i - j >= 0 and i - j < len(signal):
                result[i] += signal[i - j] * filter[j]
    return result


input_signal = [0.25,0.2,3,]

high_pass_filter = [1, 2, 3, 4]  
low_pass_filter = [0.25,0.2,3]  

high_pass_result = convolution(input_signal, high_pass_filter)
low_pass_result = convolution(input_signal, low_pass_filter)

print("signal for snipe ", high_pass_result)
print("signal for grifindor: ", low_pass_result)

print( low_pass_result,file=f)
print(high_pass_result ,file=f)
f.write( low_pass_result)
f.write(high_pass_result)
f.close()