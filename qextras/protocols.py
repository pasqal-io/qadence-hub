from __future__ import annotations

import importlib

from qextras.types import qadence_available_protocols


def available_protocols() -> dict:
    """Return the available protocols."""

    qextras: dict = dict()

    for protocol in qadence_available_protocols:
        module = importlib.import_module(f"qextras.{protocol}.protocols")
        ProtocolCls = getattr(module, protocol.capitalize())
        qextras[protocol] = ProtocolCls

    return qextras


class Protocol:
    """Generic class for protocols."""

    def __init__(self, protocol: str, options: dict = dict()) -> None:
        self.protocol: str = protocol
        self.options: dict = options

    def _to_dict(self) -> dict:
        return {"protocol": self.protocol, "options": self.options}

    @classmethod
    def _from_dict(cls, d: dict) -> Protocol:
        return cls(d["protocol"], **d["options"])

    @classmethod
    def list(cls) -> list:
        return list(filter(lambda el: not el.startswith("__"), dir(cls)))
