from collections.abc import Sequence

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatch

# TODO: Must be simple undirected graph
@_dispatch
def modularity_matrix(G: Graph[_Node], nodelist: Sequence[_Node] | None = None, weight: str | None = None): ...

# TODO: Must be simple directed graph
@_dispatch
def directed_modularity_matrix(G: Graph[_Node], nodelist: Sequence[_Node] | None = None, weight: str | None = None): ...
