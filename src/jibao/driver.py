"""Game driver — STS2MCP HTTP client.

STS2MCP is to StS2 what CDP is to Chrome. This wraps it.
Direct HTTP, no MCP overhead.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import httpx

DEFAULT_URL = "http://localhost:15526"
API_PATH = "/api/v1/singleplayer"

ORBS_FULL_SOUND = Path(__file__).parent.parent.parent / "assets" / "audio" / "blitz_final.mp3"


class GameDriver:
    """Synchronous driver for STS2MCP's HTTP API."""

    def __init__(self, base_url: str = DEFAULT_URL) -> None:
        self.base_url = base_url
        self._http = httpx.Client(base_url=base_url, timeout=10)
        self._orbs_were_full = False

    # -- Read state --

    def state(self, fmt: str = "json") -> dict | str:
        """Get current game state. fmt='json' returns dict, 'markdown' returns str."""
        r = self._http.get(API_PATH, params={"format": fmt})
        r.raise_for_status()
        result = r.json() if fmt == "json" else r.text
        if isinstance(result, dict):
            self._check_orbs_full(result)
        return result

    def _check_orbs_full(self, data: dict) -> None:
        """Play sound when orb slots go from not-full to full."""
        orb_slots = data.get("orb_slots", 0)
        orb_empty = data.get("orb_empty_slots", orb_slots)
        is_full = orb_slots > 0 and orb_empty == 0
        if is_full and not self._orbs_were_full and ORBS_FULL_SOUND.exists():
            subprocess.Popen(
                ["afplay", str(ORBS_FULL_SOUND)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        self._orbs_were_full = is_full

    # -- Execute actions --

    def act(self, action: str, **kwargs: object) -> dict:
        """Post an action to the game. Returns the API response."""
        body = {"action": action, **kwargs}
        r = self._http.post(API_PATH, json=body)
        r.raise_for_status()
        return r.json()

    def play_card(self, card_index: int, target: str | None = None) -> dict:
        kw: dict[str, object] = {"card_index": card_index}
        if target:
            kw["target"] = target
        return self.act("play_card", **kw)

    def end_turn(self) -> dict:
        return self.act("end_turn")

    def use_potion(self, slot: int, target: str | None = None) -> dict:
        kw: dict[str, object] = {"slot": slot}
        if target:
            kw["target"] = target
        return self.act("use_potion", **kw)

    def choose_map_node(self, index: int) -> dict:
        return self.act("choose_map_node", index=index)

    def choose_rest_option(self, index: int) -> dict:
        return self.act("choose_rest_option", index=index)

    def select_card_reward(self, card_index: int) -> dict:
        return self.act("select_card_reward", card_index=card_index)

    def skip_card_reward(self) -> dict:
        return self.act("skip_card_reward")

    def shop_purchase(self, index: int) -> dict:
        return self.act("shop_purchase", index=index)

    def choose_event_option(self, index: int) -> dict:
        return self.act("choose_event_option", index=index)

    def proceed(self) -> dict:
        return self.act("proceed")

    def claim_reward(self, index: int) -> dict:
        return self.act("claim_reward", index=index)

    def select_card(self, index: int) -> dict:
        return self.act("select_card", index=index)

    def confirm_selection(self) -> dict:
        return self.act("confirm_selection")

    def cancel_selection(self) -> dict:
        return self.act("cancel_selection")

    def discard_potion(self, slot: int) -> dict:
        return self.act("discard_potion", slot=slot)

    def open_chest(self) -> dict:
        return self.act("open_chest")

    def open_shop(self) -> dict:
        return self.act("open_shop")

    def open_map(self) -> dict:
        return self.act("open_map")

    def combat_select_card(self, card_index: int) -> dict:
        return self.act("combat_select_card", card_index=card_index)

    def combat_confirm_selection(self) -> dict:
        return self.act("combat_confirm_selection")

    def select_relic(self, index: int) -> dict:
        return self.act("select_relic", index=index)

    def skip_relic_selection(self) -> dict:
        return self.act("skip_relic_selection")

    def claim_treasure_relic(self, index: int) -> dict:
        return self.act("claim_treasure_relic", index=index)

    def advance_dialogue(self) -> dict:
        return self.act("advance_dialogue")

    def close(self) -> None:
        self._http.close()
