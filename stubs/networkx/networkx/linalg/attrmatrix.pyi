from collections.abc import Sequence
from typing import Any, Literal, overload

from networkx.classes.graph import Graph, _Node
from numpy.typing import DTypeLike, NDArray
from scipy import sparse

@overload
def attr_matrix(
    G: Graph[_Node],
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: None = None,
    dtype: DTypeLike | None = None,
    order: Literal["C", "F"] | None = None,
) -> tuple[NDArray[Any], list[_Node]]: ...  # 2D array
@overload
def attr_matrix(
    G: Graph[_Node],
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: Sequence[_Node] | None = None,
    dtype: DTypeLike | None = None,
    order: Literal["C", "F"] | None = None,
) -> NDArray[Any]: ...  # 2D array
@overload
def attr_sparse_matrix(
    G: Graph[_Node],
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: None = None,
    dtype: DTypeLike | None = None,
) -> tuple[sparse.sparray, list[_Node]]: ...
@overload
def attr_sparse_matrix(
    G: Graph[_Node],
    edge_attr: str | None = None,
    node_attr: str | None = None,
    normalized: bool = False,
    rc_order: Sequence[_Node] | None = None,
    dtype: DTypeLike | None = None,
) -> sparse.sparray: ...
