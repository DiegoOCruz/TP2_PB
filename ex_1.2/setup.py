from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize(
        Extension(
            "parallel_sum",
            sources=["parallel_sum.pyx"],
            include_dirs=[np.get_include()],
            extra_compile_args=["-fopenmp"],
            extra_link_args=["-fopenmp"]
        )
    )
)

