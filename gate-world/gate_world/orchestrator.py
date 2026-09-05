from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
from typing import Iterable

from .gate import GateMaster
from .models import Decision, MemoryEvent, NPC, PlayerAction, WorldState


class WorldMemory:
    def __init__(self) -> None:
        self._events: list[MemoryEvent] = []

    def record(self, event: MemoryEvent) -> None:
        self._events.append(event)

    def for_actor(self, actor_id: str) -> list[MemoryEvent]:
        return [e for e in self._events if e.actor_id == actor_id]

    def all(self) -> list[MemoryEvent]:
        return list(self._events)


class NPCSoulAI:
    def decide(self, npc: NPC, world: WorldState, memory: WorldMemory) -> Decision:
        memories = memory.for_actor(npc.npc_id)
        if npc.role == "merchant" and world.merchant_trust < 40:
            return Decision(npc.name, "raise_prices", "merchant trust is low", 0.82)
        if world.village_security < 30:
            return Decision(npc.name, "seek_shelter", "village security is low", 0.91)
        if memories:
            return Decision(npc.name, "continue_goal", f"remembered {len(memories)} event(s)", 0.75)
        return Decision(npc.name, "continue_goal", f"goal={npc.goal}", 0.65)


class WorldAI:
    def apply(self, world: WorldState, action: PlayerAction) -> WorldState:
        """Apply only validated game rules to the active world."""
        projected = GateMaster()._project(world, action)
        projected.day += 1
        return projected


class AIOrchestrator:
    def __init__(self) -> None:
        self.gate = GateMaster()
        self.memory = WorldMemory()
        self.npc_ai = NPCSoulAI()
        self.world_ai = WorldAI()

    def process_player_action(self, world: WorldState, action: PlayerAction):
        simulation = self.gate.explore(world, [action])
        active_world = self.world_ai.apply(world, action)
        self.memory.record(
            MemoryEvent(
                event_id=f"event-{len(self.memory.all()) + 1}",
                day=active_world.day,
                actor_id=action.player_id,
                event_type="player_action",
                payload={"action": action.action.value, "intensity": action.intensity},
            )
        )
        return active_world, simulation
