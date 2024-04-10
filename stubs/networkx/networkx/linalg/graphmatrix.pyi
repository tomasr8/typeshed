from collections.abc import Sequence
from typing import overload

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Edge, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph, _MultiEdge
from networkx.utils.backends import _dispatch
from numpy.typing import DTypeLike
from scipy import sparse

@overload
def incidence_matrix(
    G: Graph[_Node] | DiGraph[_Node],
    nodelist: Sequence[_Node] | None = None,
    edgelist: Sequence[_Edge[_Node]] | None = None,
    oriented: bool = False,
    weight: str | None = None,
) -> sparse.sparray: ...
@overload
def incidence_matrix(
    G: MultiGraph[_Node] | MultiDiGraph[_Node],
    nodelist: Sequence[_Node] | None = None,
    edgelist: Sequence[_MultiEdge[_Node]] | None = None,
    oriented: bool = False,
    weight: str | None = None,
) -> sparse.sparray: ...
@_dispatch
def adjacency_matrix(
    G, nodelist: Sequence[_Node] | None = None, dtype: DTypeLike | None = None, weight: str = "weight"
) -> sparse.sparray: ...
