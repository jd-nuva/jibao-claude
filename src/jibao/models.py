"""Pydantic models for game state.

Parses the JSON from the game driver into typed Python objects
for the strategy and probability engines.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel


class Screen(StrEnum):
    """What screen the game is currently showing."""

    MONSTER = "monster"
    ELITE = "elite"
    BOSS = "boss"
    HAND_SELECT = "hand_select"
    COMBAT_REWARDS = "combat_rewards"
    CARD_REWARD = "card_reward"
    MAP = "map"
    REST_SITE = "rest_site"
    SHOP = "shop"
    EVENT = "event"
    CARD_SELECT = "card_select"
    RELIC_SELECT = "relic_select"
    TREASURE = "treasure"
    OVERLAY = "overlay"
    MENU = "menu"

    @property
    def is_combat(self) -> bool:
        return self in (Screen.MONSTER, Screen.ELITE, Screen.BOSS, Screen.HAND_SELECT)


class Card(BaseModel):
    index: int
    id: str
    name: str
    type: str
    cost: int | None = None
    description: str = ""
    upgraded: bool = False
    keywords: list[str] = []


class Enemy(BaseModel):
    entity_id: str
    name: str
    current_hp: int
    max_hp: int
    block: int = 0
    powers: list[dict] = []
    intents: list[dict] = []


class Player(BaseModel):
    character: str = ""
    current_hp: int = 0
    max_hp: int = 0
    block: int = 0
    energy: int = 0
    gold: int = 0
    powers: list[dict] = []
    relics: list[dict] = []
    potions: list[dict] = []
    hand: list[Card] = []
    draw_pile_count: int = 0
    discard_pile_count: int = 0
    exhaust_pile_count: int = 0


class GameState(BaseModel):
    """Top-level game state. Fields vary by screen type."""

    screen: Screen
    player: Player | None = None
    enemies: list[Enemy] = []
    raw: dict = {}

    @classmethod
    def from_api(cls, data: dict) -> GameState:
        screen = Screen(data.get("state_type", "menu"))
        player = Player(**data["player"]) if "player" in data else None
        enemies = [Enemy(**e) for e in data.get("enemies", [])]
        return cls(screen=screen, player=player, enemies=enemies, raw=data)
