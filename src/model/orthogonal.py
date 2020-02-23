import numpy as np
from numpy.linalg import lstsq


def find_orthogonal_basis(dimension, n_children):

    if dimension < n_children:
        print("Not enough dimensions for the number of children specified.")
        raise Exception

    basis = np.zeros((dimension, n_children))
    basis[:, 0] = np.random.rand(dimension)
    # get 5 orthogonal vectors in 10 dimensions in a matrix form

    for index in range(n_children-1):
        vector = find_orthogonal_vector(basis)
        if all(np.abs(np.dot(vector, col)) < 10e-9 for col in basis.T):
            basis[:, index + 1] = vector
        else:
            print("Failure")
            raise Exception

    return basis


# https://stackoverflow.com/questions/50660389/generate-a-vector-that-is-orthogonal-to-a-set-of-other-vectors-in-any-dimension
def find_orthogonal_vector(O):
    rand_vec = np.random.rand(O.shape[0], 1)
    A = np.hstack((O, rand_vec))
    b = np.zeros(O.shape[1] + 1)
    b[-1] = 1

    return lstsq(A.T, b)[0]


if __name__ == "__main__":
    # random matrix
    basis = find_orthogonal_basis(10, 4)
    print(basis)