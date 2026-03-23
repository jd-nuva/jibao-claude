"""鸡煲claude CLI — 跟尖塔对话

Usage:
    jb state              # 当前状态 (markdown)
    jb state --json       # 当前状态 (json)
    jb play 2             # 打第2张牌
    jb play 0 JAW_WORM_0  # 打第0张牌指定目标
    jb end                # 结束回合
    jb potion 0           # 用药水
    jb potion 0 TARGET    # 用药水指定目标
    jb toss 0             # 丢弃药水
    jb path 3             # 选路
    jb pick 1             # 拿卡
    jb skip               # 跳过卡牌奖励
    jb shop 2             # 买东西
    jb event 0            # 选事件选项
    jb rest 0             # 休息点选项
    jb proceed            # 进入地图
    jb claim 1            # 领奖励
    jb select 5           # 选卡 (card_select 画面)
    jb confirm            # 确认选择
    jb cancel             # 取消选择
    jb chest              # 开宝箱
    jb openshop           # 打开商店
    jb relic 0            # 选遗物
    jb skiprelic          # 跳过遗物
    jb treasure 0         # 拿宝箱遗物
    jb hselect 0          # 战斗中选牌
    jb hconfirm           # 战斗中确认选牌
"""

from __future__ import annotations

import json
import sys

from jibao.driver import GameDriver


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)

    driver = GameDriver()
    cmd = sys.argv[1]
    args = sys.argv[2:]

    try:
        match cmd:
            case "state":
                fmt = "json" if "--json" in args else "markdown"
                result = driver.state(fmt)
                if isinstance(result, dict):
                    print(json.dumps(result, indent=2))
                else:
                    print(result)

            case "play":
                # Support both index and name: `jb play 2` or `jb play Claw+`
                try:
                    idx = int(args[0])
                    target = args[1] if len(args) > 1 else None
                    print(json.dumps(driver.play_card(idx, target), indent=2))
                except ValueError:
                    # args[0] is a card name, not an index
                    card_name = args[0]
                    target = args[1] if len(args) > 1 else None
                    print(json.dumps(driver.play_card_by_name(card_name, target), indent=2))

            case "end":
                print(json.dumps(driver.end_turn(), indent=2))

            case "potion":
                slot = int(args[0])
                target = args[1] if len(args) > 1 else None
                print(json.dumps(driver.use_potion(slot, target), indent=2))

            case "toss":
                print(json.dumps(driver.discard_potion(int(args[0])), indent=2))

            case "path":
                print(json.dumps(driver.choose_map_node(int(args[0])), indent=2))

            case "pick":
                print(json.dumps(driver.select_card_reward(int(args[0])), indent=2))

            case "skip":
                print(json.dumps(driver.skip_card_reward(), indent=2))

            case "shop":
                print(json.dumps(driver.shop_purchase(int(args[0])), indent=2))

            case "event":
                print(json.dumps(driver.choose_event_option(int(args[0])), indent=2))

            case "rest":
                print(json.dumps(driver.choose_rest_option(int(args[0])), indent=2))

            case "proceed":
                print(json.dumps(driver.proceed(), indent=2))

            case "claim":
                print(json.dumps(driver.claim_reward(int(args[0])), indent=2))

            case "select":
                print(json.dumps(driver.select_card(int(args[0])), indent=2))

            case "confirm":
                print(json.dumps(driver.confirm_selection(), indent=2))

            case "cancel":
                print(json.dumps(driver.cancel_selection(), indent=2))

            case "chest":
                print(json.dumps(driver.open_chest(), indent=2))

            case "openshop":
                print(json.dumps(driver.open_shop(), indent=2))

            case "relic":
                print(json.dumps(driver.select_relic(int(args[0])), indent=2))

            case "skiprelic":
                print(json.dumps(driver.skip_relic_selection(), indent=2))

            case "treasure":
                print(json.dumps(driver.claim_treasure_relic(int(args[0])), indent=2))

            case "hselect":
                print(json.dumps(driver.combat_select_card(int(args[0])), indent=2))

            case "hconfirm":
                print(json.dumps(driver.combat_confirm_selection(), indent=2))

            case _:
                print(f"Unknown command: {cmd}")
                print(__doc__.strip())
                sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        driver.close()
