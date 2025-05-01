import pytest
from enum import Enum

from qadence_commons import Protocol, StrEnum


def test_protocol_to_dict() -> None:
    proto = Protocol(protocol="readout", options={"a": 1})
    d = proto._to_dict()
    assert d["protocol"] == "readout"
    assert d["options"] == {"a": 1}


def test_protocol_from_dict() -> None:
    d = {"protocol": "readout", "options": {}}

    proto = Protocol._from_dict(d)
    assert isinstance(proto, Protocol)
    assert proto.protocol == "readout"


def test_protocol_list() -> None:
    names = Protocol.list()
    assert isinstance(names, list)
    assert "_to_dict" in names or "list" in names


def test_strenum_list_and_str() -> None:
    class Color(StrEnum):
        RED = "red"
        BLUE = "blue"

    assert Color.list() == ["red", "blue"]
    assert str(Color.RED) == "red"
    assert str(Color.BLUE) == "blue"
