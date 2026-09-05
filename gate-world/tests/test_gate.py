import unittest

from gate_world.gate import GateMaster
from gate_world.models import ActionType, PlayerAction, WorldState
from gate_world.orchestrator import AIOrchestrator


class GateWorldTests(unittest.TestCase):
    def test_gate_does_not_mutate_active_world(self):
        world = WorldState()
        result = GateMaster().explore(
            world, [PlayerAction("p1", ActionType.SAVE_VILLAGE, 2)]
        )
        self.assertEqual(world.village_security, 50)
        self.assertEqual(result.branches[0].projected_state["village_security"], 90)

    def test_active_world_changes_only_after_apply(self):
        world = WorldState()
        active, _ = AIOrchestrator().process_player_action(
            world, PlayerAction("p1", ActionType.SAVE_VILLAGE, 1)
        )
        self.assertEqual(active.village_security, 70)
        self.assertEqual(active.day, 2)

    def test_memory_records_action(self):
        orchestrator = AIOrchestrator()
        orchestrator.process_player_action(
            WorldState(), PlayerAction("p1", ActionType.HELP_MERCHANTS, 1)
        )
        self.assertEqual(len(orchestrator.memory.for_actor("p1")), 1)


if __name__ == "__main__":
    unittest.main()
