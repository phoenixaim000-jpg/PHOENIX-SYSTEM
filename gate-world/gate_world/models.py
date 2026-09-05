from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ActionType(str, Enum):
    SAVE_VILLAGE = "save_village"
    IGNORE_VILLAGE = "ignore_village"
    HELP_MERCHANTS = "help_merchants"


@dataclass(frozen=True)
class PlayerAction:
    player_id: str
    action: ActionType
    intensity: int = 1


@dataclass
class WorldState:
    world_id: str = "prime"
    day: int = 1
    village_security: int = 50
    village_population: int = 100
    merchant_trust: int = 50
    war_pressure: int = 20
    flags: set[str] = field(default_factory=set)

    def snapshot(self) -> dict[str, Any]:
        return {
            "world_id": self.world_id,
            "day": self.day,
            "village_security": self.village_security,
            "village_population": self.village_population,
            "merchant_trust": self.merchant_trust,
            "war_pressure": self.war_pressure,
            "flags": sorted(self.flags),
        }


@dataclass(frozen=True)
class NPC:
    npc_id: str
    name: str
    role: str
    goal: str
    personality: str


@dataclass(frozen=True)
class MemoryEvent:
    event_id: str
    day: int
    actor_id: str
    event_type: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class FutureBranch:
    branch_id: str
    title: str
    probability_hint: float
    projected_state: dict[str, Any]
    trigger: str


@dataclass(frozen=True)
class Decision:
    actor: str
    action: str
    reason: str
    confidence: float


@dataclass
class SimulationResult:
    branches: list[FutureBranch]

