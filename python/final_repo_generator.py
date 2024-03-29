import json
import os
from collections import OrderedDict

import numpy as np


def readandconvert_mats():
    gain_mat = np.genfromtxt('./results/Gain_mat_10_50')
    gain_mat = np.asarray(gain_mat).reshape(-1)
    np.savetxt('./final_results/gainmat.mat', [gain_mat], fmt="%2.6f", newline=" ", delimiter=",")

    # c1_mat = np.genfromtxt('./results/c1_mat')
    # c1_mat = np.asarray(c1_mat).reshape(-1)
    # np.savetxt('./final_results/c1.mat', [c1_mat], fmt="%2.6f", newline=" ", delimiter=",")
    #
    # c2_mat = np.genfromtxt('./results/c2_mat')
    # c2_mat = np.asarray(c2_mat).reshape(-1)
    # np.savetxt('./final_results/c2.mat', [c2_mat], fmt="%2.6f", newline=" ", delimiter=",")
    #
    # c3_mat = np.genfromtxt('./results/c3_mat')
    # c3_mat = np.asarray(c3_mat).reshape(-1)
    # np.savetxt('./final_results/c3.mat', [c3_mat], fmt="%2.6f", newline=" ", delimiter=",")

    # bolos = np.genfromtxt('./results/bolo_coefficients')

    return 0


def create_git_repo():
    path = os.getcwd()
    print(path)


def update_json(bolos):
    with open("./final_results/calib_param.json", "r") as read_file:
        data = json.load(read_file, object_pairs_hook=OrderedDict)
    print(data)
    # print(data['BiasWindows'][1]['c1'])

    data['BiasWindows'][1]['c1'] = bolos[0]
    data['BiasWindows'][1]['c2'] = bolos[1]

    with open("./final_results/convertedjson.json", "w") as write_file:
        json.dump(data, write_file)


if __name__ == '__main__':
    readandconvert_mats()
    # update_json(bolos)
    # create_git_repo()
