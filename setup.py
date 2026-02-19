from setuptools import setup, Extension
import pybind11
import os

ext = Extension(
    "calculus.calculus_core",
    ["calculus_core.cpp"],
    include_dirs=[pybind11.get_include()],
    language="c++",
    extra_compile_args=["/O2"] if os.name=="nt" else ["-O3"]
)

setup(
    name="calculus",
    version="0.2.0",
    packages=["calculus"],
    ext_modules=[ext],
    zip_safe=False,
)
