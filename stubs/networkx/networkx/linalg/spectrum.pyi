from typing import Any

import numpy as np
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatch
from numpy.typing import NDArray

@_dispatch
def laplacian_spectrum(G: Graph[_Node], weight: str = "weight") -> NDArray[np.floating[Any]]: ...
@_dispatch
def normalized_laplacian_spectrum(G: Graph[_Node], weight: str = "weight") -> NDArray[np.floating[Any]]: ...
@_dispatch
def adjacency_spectrum(G: Graph[_Node], weight: str = "weight") -> NDArray[np.inexact[Any]]: ...
@_dispatch
def modularity_spectrum(G: Graph[_Node]) -> NDArray[np.inexact[Any]]: ...
@_dispatch
def bethe_hessian_spectrum(G: Graph[_Node], r: float | None = None) -> NDArray[np.floating[Any]]: ...
