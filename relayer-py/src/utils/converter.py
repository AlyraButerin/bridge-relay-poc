"""Converter tool."""
from io import BytesIO
from typing import Any, Dict
import pickle

from web3.datastructures import AttributeDict

def _serialize_data(data: Any) -> BytesIO:
    """Serialize data to a BytesIO object.

    Args:
        data (Any): The data to serialize.

    Returns:
        BytesIO: The data serialized
    """
    if isinstance(data, AttributeDict):
        data = dict(data)
    
    pickle_data = pickle.dumps(
        data, protocol=pickle.HIGHEST_PROTOCOL)

    return BytesIO(pickle_data)

def to_bytes(data: Any) -> bytes:
    """Convert data to a bytes object.

    Args:
        data (Any): The data to convert.

    Returns:
        bytes: The data converted
    """
    return _serialize_data(data).getvalue()


def from_bytes(data: bytes) -> Any:
    """Convert data from a bytes object.

    Args:
        data (bytes): The data to convert.

    Returns:
        bytes: The data converted
    """
    return pickle.load(BytesIO(data))
