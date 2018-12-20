import numpy as np


def read_offsetmats():
    badpxlist = [1908, 2078, 3429, 9381, 11432, 15208, 16573, 40248, 58541, 69006, 74179, 74499]
    c1 = np.genfromtxt('../results/c1_mat', delimiter=',')
    print(c1.shape)
    for i in range(len(badpxlist)):
        print("c1 value = ", c1[badpxlist[i]])
        print("left and right", c1[badpxlist[i] - 1], c1[badpxlist[i] + 1])
        c1[badpxlist[i]] = ((c1[badpxlist[i] - 1] + c1[badpxlist[i] + 1]) / 2)
        print(c1[badpxlist[i]])

    c2 = np.genfromtxt('../results/c2_mat', delimiter=',')
    print(c2.shape)
    for i in range(len(badpxlist)):
        print("c2 value = ", c2[badpxlist[i]])
        print("left and right", c2[badpxlist[i] - 1], c2[badpxlist[i] + 1])
        c2[badpxlist[i]] = ((c2[badpxlist[i] - 1] + c2[badpxlist[i] + 1]) / 2)
        print(c2[badpxlist[i]])

    c3 = np.genfromtxt('../results/c3_mat', delimiter=',')
    print(c3.shape)
    for i in range(len(badpxlist)):
        print("c3 value = ", c3[badpxlist[i]])
        print("left and right", c3[badpxlist[i] - 1], c3[badpxlist[i] + 1])
        c3[badpxlist[i]] = ((c3[badpxlist[i] - 1] + c3[badpxlist[i] + 1]) / 2)
        print(c3[badpxlist[i]])

    np.savetxt("./c1_mat_conv", [c1], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./c2_mat_conv", [c2], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./c3_mat_conv", [c3], fmt="%2.6f", newline=" ", delimiter=",")

    return c1, c2, c3

def gain():
    badpxlist = [1908, 2078, 3429, 9381, 11432, 15208, 16573, 40248, 58541, 69006, 74179, 74499]
    gain = np.genfromtxt('../final_results/gainmat.mat', delimiter=',')
    print(gain.shape)
    for i in range(len(badpxlist)):
        print("gain value = ", gain[badpxlist[i]])
        print("left and right", gain[badpxlist[i] - 1], gain[badpxlist[i] + 1])
        gain[badpxlist[i]] = ((gain[badpxlist[i] - 1] + gain[badpxlist[i] + 1]) / 2)
        print(gain[badpxlist[i]])

    np.savetxt("./gain_mat_conv", [gain], fmt="%2.6f", newline=" ", delimiter=",")


def compare():
    badpxlist = [1908, 2078, 3429, 9381, 11432, 15208, 16573, 40248, 58541, 69006, 74179, 74499]
    c1 = np.genfromtxt('../results/c1_mat', delimiter=',')
    for i in range(len(badpxlist)):
        print("c1 value = ", c1[badpxlist[i]])
        print("left and right", c1[badpxlist[i] - 1], c1[badpxlist[i] + 1])

def check(c1, c2,c3):
    badpxlist = [1908, 2078, 3429, 9381, 11432, 15208, 16573, 40248, 58541, 69006, 74179, 74499]
    gain = np.genfromtxt('./gain_mat_conv', delimiter=',')
    offset = (c1[74179]*24*24) + (c2[74179]*24) + c3[74179]
    input = 4852
    print(offset)
    print(gain[74179])
    output = (gain[74179] * input) - offset
    print("output value = ", output)

if __name__ == '__main__':
    print('hello')
    c1,c2,c3 = read_offsetmats()
    # compare()
    gain()
    check(c1,c2,c3)