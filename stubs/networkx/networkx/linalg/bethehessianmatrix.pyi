from collections.abc import Sequence

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatch
from scipy import sparse

# TODO: Must be simple  undirected graph
@_dispatch
def bethe_hessian_matrix(G: Graph[_Node], r: float | None = None, nodelist: Sequence[_Node] | None = None) -> sparse.sparray: ...
