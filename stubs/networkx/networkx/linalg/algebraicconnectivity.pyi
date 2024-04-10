from _typeshed import Unused
from typing import Any, TypeVar

import numpy as np
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatch
from networkx.utils.misc import _RandomState
from numpy.typing import NDArray

_NDArray = TypeVar("_NDArray", bound=NDArray[Any])

class _PCGSolver:
    def __init__(self, A, M) -> None: ...
    def solve(self, B: _NDArray, tol: float) -> _NDArray: ...

class _LUSolver:
    def __init__(self, A) -> None: ...
    def solve(self, B: _NDArray, tol: Unused = None) -> _NDArray: ...

# TODO: Must not be directed graph
@_dispatch
def algebraic_connectivity(
    G: Graph[_Node],
    weight: str = "weight",
    normalized: bool = False,
    tol: float = 1e-08,
    method: str = "tracemin_pcg",
    seed: _RandomState = None,
) -> float: ...

# TODO: Must not be directed graph
@_dispatch
def fiedler_vector(
    G: Graph[_Node],
    weight: str = "weight",
    normalized: bool = False,
    tol: float = 1e-08,
    method: str = "tracemin_pcg",
    seed: _RandomState = None,
) -> NDArray[np.floating[Any]]: ...
@_dispatch
def spectral_ordering(
    G: Graph[_Node],
    weight: str = "weight",
    normalized: bool = False,
    tol: float = 1e-08,
    method: str = "tracemin_pcg",
    seed: _RandomState = None,
) -> NDArray[np.floating[Any]]: ...
@_dispatch
def spectral_bisection(
    G: Graph[_Node],
    weight: str = "weight",
    normalized: bool = False,
    tol: float = 1e-08,
    method: str = "tracemin_pcg",
    seed: _RandomState = None,
) -> tuple[set[_Node], set[_Node]]: ...
