import numpy as np

from computeoffset import *
from gain import *


def get_offset_Mats(h, w, t_low, t_high, t_step):
    y = np.arange(t_low, t_high, t_step)
    filename = []
    offset_array = np.zeros((len(y), h, w))
    k = 0

    for i in range(t_low, t_high, t_step):
        filename.append('./results/Offset_Mat_' + str(i))
        offset_m = np.loadtxt(filename[k])
        offset_array[k] = offset_m
        k = k + 1
    return offset_array, y


# def compute_offset_polynomial(offset_array, y, h, w, t_low, t_high, t_step):
#     offset_polynomial = np.zeros((3, h, w))
#     print('Computing offset polynomial matrices...')
#     for i in range(0, h, 1):
#         for j in range(0, w, 1):
#             index = 0
#             pix_offset_Acc = []
#             for k in range(t_low, t_high, t_step):
#                 pix_offset_Acc.append(offset_array[[index], [i], [j]])
#                 index = index + 1
#             poly = np.polyfit(y, pix_offset_Acc, 2)
#             offset_polynomial[[0], [i], [j]] = poly[0]
#             offset_polynomial[[1], [i], [j]] = poly[1]
#             offset_polynomial[[2], [i], [j]] = poly[2]
#
#     np.savetxt("./results/c1_mat", offset_polynomial[0], fmt="%2.6f")
#     np.savetxt("./results/c2_mat", offset_polynomial[1], fmt="%2.6f")
#     np.savetxt("./results/c3_mat", offset_polynomial[2], fmt="%2.6f")
#     print('\nDone.')
#
#     return 0


def compute_offset_polynomial_vectorized(offset_array, y, h, w):
    offset_mat = np.empty((len(offset_array), (h * w)))
    print("Computing offset polynomial matrices...")
    for i in range(len(offset_array)):
        flattened_mat = offset_array[i].flatten()
        offset_mat[i] = flattened_mat
    offset_polynomial = np.polyfit(y, offset_mat, 2)

    np.savetxt("./results/c1_mat", [offset_polynomial[0]], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/c2_mat", [offset_polynomial[1]], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/c3_mat", [offset_polynomial[2]], fmt="%2.6f", newline=" ", delimiter=",")
    print("\nDone.")
    compute_cubic_interpolation(offset_array, y, h, w)


def compute_cubic_interpolation(offset_array, y, h, w):
    if input("\n" "Do you want to compute cubic interpolation matrices? (y/n)") != "y":
        exit()

    offset_mat = np.empty((len(offset_array), (h * w)))
    print("Computing cubic polynomial matrices...")
    for i in range(len(offset_array)):
        flattened_mat = offset_array[i].flatten()
        offset_mat[i] = flattened_mat
    offset_polynomial = np.polyfit(y, offset_mat, 3)

    np.savetxt("./results/cubic_c1_mat", [offset_polynomial[0]], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/cubic_c2_mat", [offset_polynomial[1]], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/cubic_c3_mat", [offset_polynomial[2]], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/cubic_c4_mat", [offset_polynomial[3]], fmt="%2.6f", newline=" ", delimiter=",")

    print("\nDone.")


def compute_transposed_coeffecients(offset_array, y, h, w):
    offset_mat = np.empty((len(offset_array), (h * w)))
    print("Computing transposed matrices...")
    for i in range(len(offset_array)):
        flattened_mat = offset_array[i].flatten()
        offset_mat[i] = flattened_mat
    offset_polynomial = np.polyfit(y, offset_mat, 2)

    # transposed_list.append(np.rot90(np.rot90(offset_polynomial[0])))
    # transposed_list.append(np.rot90(np.rot90(offset_polynomial[1])))
    # transposed_list.append(np.rot90(np.rot90(offset_polynomial[2])))

    c1 = offset_polynomial[0]
    c1 = np.reshape(c1, [240, 320])
    c1 = np.rot90(c1, k=2, axes=(0, 1))

    c2 = offset_polynomial[1]
    c2 = np.reshape(c2, [240, 320])
    c2 = np.rot90(c2, k=2, axes=(0, 1))

    c3 = offset_polynomial[2]
    c3 = np.reshape(c3, [240, 320])
    c3 = np.rot90(c3, k=2, axes=(0, 1))

    c1 = np.asarray(c1).reshape(-1)
    c2 = np.asarray(c2).reshape(-1)
    c3 = np.asarray(c3).reshape(-1)

    np.savetxt("./results/cubic_rot_c1_mat", [c1], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/cubic_rot_c2_mat", [c2], fmt="%2.6f", newline=" ", delimiter=",")
    np.savetxt("./results/cubic_rot_c3_mat", [c3], fmt="%2.6f", newline=" ", delimiter=",")

    print("\nDone.")


def main(height, width, t_low, t_high, t_step):
    offset_array, y = get_offset_Mats(height, width, t_low, t_high, t_step)
    # compute_offset_polynomial(offset_array, y, height, width, t_low, t_high, t_step)
    compute_offset_polynomial_vectorized(offset_array, y, height, width)
    # compute_transposed_coeffecients(offset_array, y, height, width)


if __name__ == '__main__':
    main(288, 384, 0, 41, 4)
