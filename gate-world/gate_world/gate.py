from __future__ import annotations

from dataclasses import replace
from typing import Iterable

from .models import ActionType, FutureBranch, PlayerAction, SimulationResult, WorldState


class GateMaster:
    """Creates *possible* futures without mutating the active world."""

    def explore(self, world: WorldState, actions: Iterable[PlayerAction]) -> SimulationResult:
        action_list = list(actions)
        branches: list[FutureBranch] = []
        for action in action_list:
            projected = self._project(world, action)
            branches.append(
                FutureBranch(
                    branch_id=f"{action.action.value}-{len(branches)+1}",
                    title=self._title(action.action),
                    probability_hint=self._probability_hint(action),
                    projected_state=projected.snapshot(),
                    trigger=f"player:{action.player_id} action:{action.action.value}",
                )
            )
        return SimulationResult(branches=branches)

    def _project(self, world: WorldState, action: PlayerAction) -> WorldState:
        intensity = max(1, min(action.intensity, 10))
        if action.action is ActionType.SAVE_VILLAGE:
            return replace(
                world,
                village_security=min(100, world.village_security + 20 * intensity),
                village_population=min(1000, world.village_population + 5 * intensity),
                war_pressure=max(0, world.war_pressure - 3 * intensity),
            )
        if action.action is ActionType.HELP_MERCHANTS:
            return replace(
                world,
                merchant_trust=min(100, world.merchant_trust + 15 * intensity),
                war_pressure=max(0, world.war_pressure - intensity),
            )
        return replace(
            world,
            village_security=max(0, world.village_security - 10 * intensity),
            village_population=max(0, world.village_population - 8 * intensity),
            war_pressure=min(100, world.war_pressure + 8 * intensity),
        )

    @staticmethod
    def _title(action: ActionType) -> str:
        return {
            ActionType.SAVE_VILLAGE: "村が繁栄する未来",
            ActionType.IGNORE_VILLAGE: "村が衰退する未来",
            ActionType.HELP_MERCHANTS: "交易都市へ成長する未来",
        }[action]

    @staticmethod
    def _probability_hint(action: PlayerAction) -> float:
        return round(0.5 + min(action.intensity, 10) * 0.04, 2)
