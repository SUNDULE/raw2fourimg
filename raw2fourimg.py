import numpy as np
from PIL import Image


def left_up(matrix):
    n = len(matrix) // 2
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            small_matrix = matrix[i * 2][j * 2]
            new_matrix[i][j] = small_matrix

    return new_matrix


def left_down(matrix):
    n = len(matrix) // 2
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            small_matrix = matrix[i * 2 + 1][j * 2]
            new_matrix[i][j] = small_matrix

    return new_matrix

def right_up(matrix):
    n = len(matrix) // 2
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            small_matrix = matrix[i * 2][j * 2 + 1]
            new_matrix[i][j] = small_matrix

    return new_matrix


def right_down(matrix):
    n = len(matrix) // 2
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            small_matrix = matrix[i * 2 + 1][j * 2 + 1]
            new_matrix[i][j] = small_matrix

    return new_matrix


rawImg = np.fromfile("./0.raw", dtype=np.uint8)
rawImg = rawImg.reshape(2048, 2448)

#print(rawImg)

if __name__ == '__main__':
    print(len(rawImg))
    result_left_up = np.array(left_up(rawImg))
    result_left_down = np.array(left_down(rawImg))
    result_right_up = np.array(right_up(rawImg))
    result_right_down = np.array(right_down(rawImg))


    imageLU = Image.fromarray(result_left_up.astype(np.uint8))
    imageLD = Image.fromarray(result_left_down.astype(np.uint8))
    imageRU = Image.fromarray(result_right_up.astype(np.uint8))
    imageRD = Image.fromarray(result_right_down.astype(np.uint8))

    imageLU.save("./LU.png")
    imageLD.save("./LD.png")
    imageRU.save("./RU.png")
    imageRD.save("./RD.png")

    print("全部处理完了！")



