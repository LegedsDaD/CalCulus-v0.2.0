"""
CalCulus core bindings
"""

from .calculus_core import Scalar, Vec3, Solver, Constants

# ----------------- Helper: ensure input is Scalar -----------------
def _to_scalar(x):
    if not isinstance(x, Scalar):
        return Scalar(x)
    return x

# ----------------- Convenience math functions -----------------
def sin(x): return _to_scalar(x).sin()
def cos(x): return _to_scalar(x).cos()
def tan(x): return _to_scalar(x).tan()
def asin(x): return _to_scalar(x).asin()
def acos(x): return _to_scalar(x).acos()
def atan(x): return _to_scalar(x).atan()
def sinh(x): return _to_scalar(x).sinh()
def cosh(x): return _to_scalar(x).cosh()
def tanh(x): return _to_scalar(x).tanh()
def exp(x): return _to_scalar(x).exp()
def log(x): return _to_scalar(x).log()
def log10(x): return _to_scalar(x).log10()
def sqrt(x): return _to_scalar(x).sqrt()
def cbrt(x): return _to_scalar(x).cbrt()
def abs(x): return _to_scalar(x).abs()
def pow(x, n): return _to_scalar(x).pow(n)
