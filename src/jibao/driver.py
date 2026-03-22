"""Game driver — STS2MCP HTTP client.

STS2MCP is to StS2 what CDP is to Chrome. This wraps it.
Direct HTTP, no MCP overhead.
"""

from __future__ import annotations

import httpx

DEFAULT_URL = "http://localhost:15526"
API_PATH = "/api/v1/singleplayer"


class GameDriver:
    """Synchronous driver for STS2MCP's HTTP API."""

    def __init__(self, base_url: str = DEFAULT_URL) -> None:
        self.base_url = base_url
        self._http = httpx.Client(base_url=base_url, timeout=10)

    # -- Read state --

    def state(self, fmt: str = "json") -> dict | str:
        """Get current game state. fmt='json' returns dict, 'markdown' returns str."""
        r = self._http.get(API_PATH, params={"format": fmt})
        r.raise_for_status()
        return r.json() if fmt == "json" else r.text

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

    def close(self) -> None:
        self._http.close()
