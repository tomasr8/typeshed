from collections.abc import Sequence
from typing import Literal

from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatch

@_dispatch
def laplacian_matrix(G, nodelist: Sequence[_Node] | None = None, weight: str = "weight"): ...
@_dispatch
def normalized_laplacian_matrix(G, nodelist: Sequence[_Node] | None = None, weight: str = "weight"): ...
@_dispatch
def total_spanning_tree_weight(G, weight: str | None = None) -> float: ...
@_dispatch
def directed_laplacian_matrix(
    G,
    nodelist: Sequence[_Node] | None = None,
    weight: str = "weight",
    walk_type: Literal["random", "lazy", "pagerank"] | None = None,
    alpha: float = 0.95,
): ...
@_dispatch
def directed_combinatorial_laplacian_matrix(
    G,
    nodelist: Sequence[_Node] | None = None,
    weight: str = "weight",
    walk_type: Literal["random", "lazy", "pagerank"] | None = None,
    alpha: float = 0.95,
): ...
