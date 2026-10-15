# display/render.py

import os
from typing import Dict, Optional, Tuple
from mazegen.maze import Maze
from utils.input import safe_input

# ANSIエスケープシーケンス（色定義）
COLOR_RESET = "\033[0m"
COLOR_PATH = "\033[32m"      # 緑
COLOR_ENTRY = "\033[35m"     # マゼンダ
COLOR_EXIT = "\033[31m"      # 赤

# 背景色定義
BG_GRAY = "\033[100m"         # 明るい灰色の背景（42パターン用）
EMPTY_PATH = "  "

WALL_COLORS = {
    1: ("デフォルト（ホワイト）", "\033[37m"),
    2: ("シアン", "\033[36m"),
    3: ("マゼンタ", "\033[35m"),
    4: ("ブルー", "\033[34m"),
    5: ("グリーン", "\033[32m"),
    6: ("イエロー", "\033[33m"),
}

# ボーナス機能：テーマ・テクスチャプリセット
THEMES: Dict[int, Dict[str, str]] = {
    1: {
        "name": "Classic White",
        "wall": "██",
        "path": "  ",
        "start": "██",
        "goal": "██",
        "solution": "  ",
        "color_sol": "\033[46m\033[30m",
        "player": " P",
        "reset": "\033[0m",
    },
    2: {
        "name": "Cyberpunk Neon",
        "wall": "▓▓",
        "path": "  ",
        "start": " S",
        "goal": " G",
        "solution": "★ ",
        "color_sol": "\033[93m",
        "player": "🤖",
        "reset": "\033[0m",
    },
    3: {
        "name": "Retro Terminal",
        "wall": "▒▒",
        "path": "  ",
        "start": " S",
        "goal": " G",
        "solution": "♦︎ ",
        "color_sol": "\033[32m",
        "player": "👾",
        "reset": "\033[0m",
    },
    4: {
        "name": "Brick & Forest (Emoji)",
        "wall": "🧱",
        "path": "  ",
        "start": "🚩",
        "goal": "🏆",
        "solution": "🐾",
        "player": "🏃",
        "color_wall": "",
        "color_sol": "",
        "reset": "\033[0m",
    },
}


def render_maze(
    maze: Maze,
    show_solution: bool = False,
    wall_color_code: str = "\033[35m",
    solution_path: Optional[list[str]] = None,
    theme_id: int = 1,
    player_pos: Optional[Tuple[int, int]] = None,
    show_pattern_color: bool = True,
) -> str:
    """Maze オブジェクトをターミナル表示用の装飾済み文字列に変換します。

    グリッドの構築、壁・通路の描画、42パターンの強調表示、最短経路の
    オーバーレイ描画、およびプレイヤー位置の描画を行います。

    Args:
        maze (Maze): レンダリング対象の迷路オブジェクト。
        show_solution (bool, optional): 最短経路を表示するかどうかのフラグ。
            Defaults to False.
        wall_color_code (str, optional): 壁の描画に使用するANSIカラーコード。
            Defaults to "\033[35m".
        solution_path (Optional[list[str]], optional):外部から渡される解の経路リスト
            （例: ['N', 'E', ...])。
            None の場合は `maze.solve()` が呼ばれます。 Defaults to None.
        theme_id (int, optional): 使用するテーマの ID。 Defaults to 1.
        player_pos (Optional[Tuple[int, int]], optional):描画するプレイヤーの現在座標 (x, y)。
            Defaults to None.
        show_pattern_color (bool, optional): 『42』パターン部分の背景色を強調表示するかどうかのフラグ。
            Defaults to True.

    Returns:
        str: ターミナルへ出力可能な、改行コードで結合された迷路のマルチライン文字列。
    """
    theme = THEMES.get(theme_id, THEMES[1])

    # 1. 2Dグリッド（幅 width*2 + 1, 高さ height*2 + 1）の作成
    grid_w: int = maze.width * 2 + 1
    grid_h: int = maze.height * 2 + 1
    canvas = [
        [theme["path"] for _ in range(grid_w)]
        for _ in range(grid_h)
    ]

    # 2. 壁埋め
    fallback_wall = theme.get("color_wall", "")
    c_wall = wall_color_code if wall_color_code else fallback_wall
    c_reset = str(theme.get("reset", COLOR_RESET))
    wall_char = f"{c_wall}{theme['wall']}{c_reset}"
    for y in range(grid_h):
        for x in range(grid_w):
            canvas[y][x] = wall_char

    # 3. 通路とパターンの描画
    pattern_set = set(
        maze.pattern_cells) if hasattr(maze, "pattern_cells") else set()

    for y in range(maze.height):
        for x in range(maze.width):
            gx, gy = x * 2 + 1, y * 2 + 1
            cell = maze.cells[y][x]
            is_pattern = (x, y) in pattern_set and show_pattern_color

            # セル本体
            if is_pattern:
                canvas[gy][gx] = f"{BG_GRAY}{EMPTY_PATH}{c_reset}"
            else:
                canvas[gy][gx] = EMPTY_PATH

            # 壁の穿孔（通路化）
            # 自分と隣接セルがともにパターン内の場合のみグレー背景、それ以外は普通の通路スペース
            if not cell.north and gy - 1 >= 0:
                is_north_pattern = (
                    x, y - 1) in pattern_set and show_pattern_color
                canvas[gy - 1][gx] = f"{BG_GRAY}{EMPTY_PATH}{c_reset}" if (
                    is_pattern and is_north_pattern) else EMPTY_PATH

            if not cell.south and gy + 1 < grid_h:
                is_south_pattern = (
                    x, y + 1) in pattern_set and show_pattern_color
                canvas[gy + 1][gx] = f"{BG_GRAY}{EMPTY_PATH}{c_reset}" if (
                    is_pattern and is_south_pattern) else EMPTY_PATH

            if not cell.east and gx + 1 < grid_w:
                is_east_pattern = (
                    x + 1, y) in pattern_set and show_pattern_color
                canvas[gy][gx + 1] = f"{BG_GRAY}{EMPTY_PATH}{c_reset}" if (
                    is_pattern and is_east_pattern) else EMPTY_PATH

            if not cell.west and gx - 1 >= 0:
                is_west_pattern = (
                    x - 1, y) in pattern_set and show_pattern_color
                canvas[gy][gx - 1] = f"{BG_GRAY}{EMPTY_PATH}{c_reset}" if (
                    is_pattern and is_west_pattern) else EMPTY_PATH

    # 4. ENTRY / EXIT 座標をあらかじめ計算
    entry_gx, entry_gy = maze.entry[0] * 2 + 1, maze.entry[1] * 2 + 1
    exit_gx, exit_gy = maze.exit[0] * 2 + 1, maze.exit[1] * 2 + 1

    # 5. 最短経路をオーバーレイ
    if show_solution:
        # テーマから色コードと表示文字を取得（未設定時はデフォルト値を使用）
        c_sol = theme.get("color_sol", "\033[46m\033[30m")
        sol_char = theme.get("solution", "  ")

        # 装飾文字列を生成（色指定があれば付与、絵文字等で色が不要な場合は文字のみ）
        sol_str = f"{c_sol}{sol_char}{c_reset}" if c_sol else sol_char

        curr_x, curr_y = maze.entry
        path_moves = (
            solution_path if solution_path is not None else maze.solve()
        )

        curr_gx, curr_gy = curr_x * 2 + 1, curr_y * 2 + 1

        for move in path_moves:
            next_x, next_y = curr_x, curr_y
            mid_gx, mid_gy = curr_gx, curr_gy

            if move == "N":
                next_y -= 1
                mid_gy -= 1
            elif move == "S":
                next_y += 1
                mid_gy += 1
            elif move == "E":
                next_x += 1
                mid_gx += 1
            elif move == "W":
                next_x -= 1
                mid_gx -= 1

            next_gx, next_gy = next_x * 2 + 1, next_y * 2 + 1

            # 1. 間のマス（通路）を描画
            is_mid_entry = (mid_gx, mid_gy) == (entry_gx, entry_gy)
            is_mid_exit = (mid_gx, mid_gy) == (exit_gx, exit_gy)
            if not (is_mid_entry or is_mid_exit):
                canvas[mid_gy][mid_gx] = sol_str

            # 2. 移動先のセル本体を描画
            is_next_entry = (next_gx, next_gy) == (entry_gx, entry_gy)
            is_next_exit = (next_gx, next_gy) == (exit_gx, exit_gy)
            if not (is_next_entry or is_next_exit):
                canvas[next_gy][next_gx] = sol_str

            curr_x, curr_y = next_x, next_y
            curr_gx, curr_gy = next_gx, next_gy

    # 6. ENTRY / EXIT を描画（スタート・ゴールアイコンで上書き）
    canvas[entry_gy][entry_gx] = f"{COLOR_ENTRY}{theme['start']}{c_reset}"
    canvas[exit_gy][exit_gx] = f"{COLOR_EXIT}{theme['goal']}{c_reset}"

    # 7. プレイヤー描画
    if player_pos is not None:
        px_g, py_g = player_pos[0] * 2 + 1, player_pos[1] * 2 + 1
        if 0 <= px_g < grid_w and 0 <= py_g < grid_h:
            c_player = str(theme.get("color_player", COLOR_PATH))
            canvas[py_g][px_g] = f"{c_player}{theme['player']}{c_reset}"
    lines = ["".join(row) for row in canvas]
    return "\n".join(lines) + COLOR_RESET


# ボーナス機能：プレイヤー操作モード（インタラクティブゲーム）
def play_game_mode(
    maze: Maze,
    wall_color_code: str = "",
    theme_id: int = 1,
) -> None:
    """標準入力 (W/A/S/D) を使用して迷路内をインタラクティブに操作するゲームモードを開始します。

    ユーザーの移動入力に従ってプレイヤー座標を更新し、壁への衝突を検知しながら
    ゴール到達までループ処理を行います。

    Args:
        maze (Maze): プレイ対象の迷路オブジェクト。
        wall_color_code (str, optional): 迷路描画用の ANSI 壁カラーコード。
            Defaults to "".
        theme_id (int, optional): 使用するテーマ ID。 Defaults to 1.

    Returns:
        None
    """
    px, py = maze.entry
    gx, gy = maze.exit

    print("\n🎮 プレイヤー操作モード開始！")
    print("移動: W (上), A (左), S (下), D (右) / Q (中断退出)")
    try:
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            rendered = render_maze(
                maze,
                wall_color_code=wall_color_code,
                theme_id=theme_id,
                player_pos=(px, py),
            )
            print(rendered)
            if (px, py) == (gx, gy):
                print("\n🎉 祝！ゴールに到達しました！ 🎉\n")
                safe_input("Enterキーを押してメニューに戻ります...")
                break

            move = safe_input("\n移動方向 (W/A/S/D/Q): ").strip().upper()
            if move == "Q":
                print("ゲームを中断しました。")
                break

            cell = maze.cells[py][px]
            if move == "W" and not cell.north and py > 0:
                py -= 1
            elif move == "S" and not cell.south and py < maze.height - 1:
                py += 1
            elif move == "D" and not cell.east and px < maze.width - 1:
                px += 1
            elif move == "A" and not cell.west and px > 0:
                px -= 1
    except (EOFError, KeyboardInterrupt):
        print("\nゲームを終了しました。")
