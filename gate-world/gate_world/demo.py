from .models import ActionType, NPC, PlayerAction, WorldState
from .orchestrator import AIOrchestrator


def main() -> None:
    world = WorldState()
    npc = NPC("npc-001", "ミナ", "merchant", "protect the market", "cautious")
    orchestrator = AIOrchestrator()

    action = PlayerAction("player-001", ActionType.SAVE_VILLAGE, intensity=2)
    active_world, simulation = orchestrator.process_player_action(world, action)
    decision = orchestrator.npc_ai.decide(npc, active_world, orchestrator.memory)

    print("=== GATE WORLD MVP ===")
    print("ACTIVE WORLD:", active_world.snapshot())
    print("POSSIBLE FUTURE:", simulation.branches[0].projected_state)
    print("NPC DECISION:", decision)
    print("MEMORY EVENTS:", len(orchestrator.memory.all()))


if __name__ == "__main__":
    main()
