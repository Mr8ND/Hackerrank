import math

def normFunc(x, m, std):
    x, m, std = float(x), float(m), float(std)
    return (1/((2*math.pi*(std**2))**0.5))*math.exp((-(x - m)**2)/(2*(std**2)))

def probX(X, m, std):
    vec_x = [x/100.0 for x in range(-10000, (X*100)+1)]
    result_vec = [normFunc(x, m, std) for x in vec_x]
    return sum(result_vec)/100
            
print probX(40,30,4)
print 1 - probX(21, 30, 4)
print probX(35, 30, 4) - probX(30, 30, 4)