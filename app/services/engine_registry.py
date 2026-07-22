from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EngineDefinition:
    name: str
    description: str
    category: str


class EngineRegistry:
    def __init__(self) -> None:
        self._engines: dict[str, EngineDefinition] = {}

    def register(self, definition: EngineDefinition) -> None:
        self._engines[definition.name] = definition

    def list(self) -> list[EngineDefinition]:
        return sorted(self._engines.values(), key=lambda item: item.name)

    def get(self, name: str) -> EngineDefinition | None:
        return self._engines.get(name)
