from cython.parallel import prange
import numpy as np
cimport numpy as np

#calcular a soma paralela
def parallel_sum(np.ndarray[np.int32_t, ndim=1] vetor):
    cdef int i
    cdef long temp_soma = 0

    # Soma em paralelo
    for i in prange(vetor.shape[0], nogil=True):  # Paralelismo com prange
        temp_soma += vetor[i]

    return temp_soma

