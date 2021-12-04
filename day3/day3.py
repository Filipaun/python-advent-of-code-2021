import numpy as np

data = np.genfromtxt('day3/input.txt', delimiter=1, dtype=np.int8) 

gamma_rate = np.zeros(data.shape[1])
epsilon_rate =  np.zeros(data.shape[1])

def to_decimal(bin_array):
    decimal_val = 0
    length = len(bin_array)

    for i in range(length):
        decimal_val += bin_array[i]*2**(length-(i+1))
    
    return decimal_val

def part1():
    for i in range(data.shape[1]):
        if sum(data[:,i]) > data.shape[0]/2:
            gamma_rate[i] = 1
            epsilon_rate[i] = 0
        else:
            gamma_rate[i] = 0
            epsilon_rate[i] = 1
    gamma_rate_dec = to_decimal(gamma_rate)
    epsilon_rate_dec = to_decimal(epsilon_rate)
    
    print(f"Gamma: {gamma_rate_dec}, Eps: {epsilon_rate_dec}")
    print(f"Prod: {gamma_rate_dec*epsilon_rate_dec}")

def part2():
    most_common = 0

    ox_array = np.copy(data)
    n_ox = ox_array.shape[0]
    co2_array = np.copy(data)
    n_co2 = ox_array.shape[0]

    for i in range(data.shape[1]):
        if sum(ox_array[:,i])/n_ox >= 0.5:
            most_common = 1
        else:
            most_common = 0
        
        j = 0
        while j < ox_array.shape[0]:
            if ox_array[j,i] != most_common:
                ox_array = np.delete(ox_array,j,0)
                n_ox -= 1
            else:
                j += 1
        if (n_ox) == 1:
            break

    for i in range(data.shape[1]):
        if sum(co2_array[:,i])/n_co2 >= 0.5:
            most_common = 1
        else:
            most_common = 0
        
        j = 0
        while j < co2_array.shape[0]:
            if co2_array[j,i] == most_common:
                co2_array = np.delete(co2_array,j,0)
                n_co2 -= 1
            else:
                j += 1
        if (n_co2) == 1:
            break


    ox_rating = to_decimal(ox_array[0])
    co2_rating = to_decimal(co2_array[0])
    print(f"Ox: {ox_rating}, Co2: {co2_rating}")
    print(f"Life support: {ox_rating*co2_rating}")

part1()
part2()