from dataclasses import dataclass


@dataclass
class MessageContextModel:
    type: str
    title: str
    message: str
