import os
import sys
from display.render import (
    COLOR_RESET,
    THEMES,
    WALL_COLORS,
    play_game_mode,
    render_maze,
)
from mazegen.maze import (
    MazeGenerator,
    validate_maze,
    MazeGeneratorError
)
from config import parse_config
from utils.file_io import save_maze_to_file
from utils.input import safe_input


def print_menu(
    show_solution: bool,
    current_color_name: str,
    current_theme_id: int,
    show_pattern_color: bool
) -> None:
    """コンソールに操作メニューを出力します。

    現在の設定状態（経路表示、壁の色、パターン強調、テーマ）を反映した
    対話型メニューを表示します。

    Args:
        show_solution (bool): 最短経路を表示するかどうかのフラグ。
        current_color_name (str): 現在設定されている壁のカラー表示名。
        current_theme_id (int): 現在選択されているテーマの ID。
        show_pattern_color (bool): 『42』パターンを強調表示するかどうかのフラグ。

    Returns:
        None
    """
    solution_status = "ON" if show_solution else "OFF"
    pattern_status = "ON" if show_pattern_color else "OFF"
    theme_info = THEMES.get(current_theme_id, {})
    theme_name = theme_info.get("name", f"Theme {current_theme_id}")

    print("\n" + "=" * 40)
    print("【A-Maze-ing 操作メニュー】")
    print("1. 迷路を再生成する")
    print(f"2. 最短経路の表示切り替え (現在: {solution_status})")
    print(f"3. 壁の色を変更する (現在: {current_color_name})")
    print(f"4. 『42』パターンの強調色切り替え (現在: {pattern_status})")
    print(f"5. 🎨 テーマ/フォントを変更する (現在: {theme_name}) [Bonus]")
    print("6. 🎮 プレイヤー操作モードで遊ぶ [Bonus]")
    print("7. 終了")
    print("=" * 40)


def change_wall_color(current_color_code: str) -> str:
    """壁の表示色を変更するサブメニューを呼び出します。

    利用可能なカラー一覧を表示し、ユーザーの入力に応じて
    新しい ANSI カラーコードを返します。

    Args:
        current_color_code (str): 現在使用されているANSIカラーコード。

    Returns:
        str: ユーザーが選択した新しいANSIカラーコード。入力が無効な場合は
            変更前の `current_color_code` を返します。
    """
    print("\n--- 壁の色の選択 ---")

    for key, val in WALL_COLORS.items():
        name, code = val
        print(f"{key}: {code}{name}{COLOR_RESET}")

    c_input = safe_input(f"色の番号を選んでください (1-{len(WALL_COLORS)}): ")

    if c_input.isdigit():
        choice = int(c_input)
        if choice in WALL_COLORS:
            selected_name, selected_code = WALL_COLORS[choice]
            print(f"\n壁の色を『{selected_name}』に変更しました。")
            return selected_code

    print("\n無効な入力です。変更されませんでした。")
    return current_color_code


def change_theme(current_theme_id: int) -> int:
    """テーマ/フォントを変更するサブメニューを呼び出します。

    利用可能なテーマ一覧を表示し、ユーザーの入力に応じて
    選択されたテーマIDを返します。

    Args:
        current_theme_id (int): 現在使用されているテーマのID。

    Returns:
        int: ユーザーが選択した新しいテーマID。入力が無効な場合は
            変更前の `current_theme_id` を返します。
    """
    print("\n--- テーマ/フォントの選択 ---")

    for theme_id, theme_info in THEMES.items():
        name = theme_info.get("name", f"Theme {theme_id}")
        wall_char = theme_info.get("wall", "██")
        print(f"{theme_id}: {name} (壁の文字: {wall_char})")

    t_input = safe_input(f"テーマの番号を選んでください (1-{len(THEMES)}): ")

    if t_input.isdigit():
        choice = int(t_input)
        if choice in THEMES:
            print(f"\nテーマを『{THEMES[choice].get('name')}』に変更しました。")
            return choice

    print("\n無効な入力です。変更されませんでした。")
    return current_theme_id


def get_color_name(color_code: str) -> str:
    """ANSIカラーコードに対応する色名を取得します。

    Args:
        color_code (str): 検索対象のANSIカラーコード。

    Returns:
        str: 一致する色の表示名。該当するものがない場合は `"Custom"` を返します。
    """
    for key, val in WALL_COLORS.items():
        name, code = val
        if code == color_code:
            return name
    return "Custom"


def clear_screen() -> None:
    """実行環境のOSに合わせて端末画面をクリアします。

    POSIX（Linux/macOS）の場合は `clear`、Windows の場合は `cls` を実行します。

    Args:
        None

    Returns:
        None
    """
    os.system("clear" if os.name == "posix" else "cls")


def main() -> None:
    """メインプログラム実行ルーチン。

    コマンドライン引数から設定ファイルを読み込み、迷路の初期生成および
    インタラクティブな操作メニューのループ処理を行います。

    Args:
        None

    Returns:
        None
    """
    if not len(sys.argv) == 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        return
    try:
        config = parse_config(sys.argv[1])
        generator = MazeGenerator(
            config.width,
            config.height,
            config.entry,
            config.exit,
            config.perfect,
            config.seed
        )
        maze = generator.generate()
        validate_maze(maze)
        save_maze_to_file(maze, config.output_file)
    except MazeGeneratorError as e:
        print(f"{e}")
        return
    show_solution = False
    current_color_code = WALL_COLORS[1][1]  # デフォルト色 (ANSI)
    current_theme_id = 1                    # デフォルトテーマID
    show_pattern_color = True   # 『42』パターンの色強調フラグ
    is_first_render: bool = True  # 初回だけclearしないように

    while True:
        # 初回だけ画面クリアをスキップする
        if not is_first_render:
            clear_screen()
        else:
            is_first_render = False  # 次回以降はクリアを実行するように変更
        try:
            solution = maze.solve() if show_solution else None
        except MazeGeneratorError as e:
            print(f"{e}")
            solution = None

        print(
            render_maze(
                maze,
                show_solution=show_solution,
                solution_path=solution,
                wall_color_code=current_color_code,
                theme_id=current_theme_id,
                show_pattern_color=show_pattern_color,
            )
        )

        current_color_name = get_color_name(current_color_code)
        print_menu(
            show_solution,
            current_color_name,
            current_theme_id,
            show_pattern_color,
            )

        max_choice = "7"
        choice = safe_input(f"操作を選択してください (1-{max_choice}): ").strip()

        if choice == "1":
            if config.seed is None:
                config.seed = 0
            else:
                config.seed += 1
            # シード値変更および再生成処理
            try:
                # 設定パラメータに基づいて生成器を作成（環境の設計に合わせて調整）
                generator = MazeGenerator(
                    config.width,
                    config.height,
                    config.entry,
                    config.exit,
                    config.perfect,
                    config.seed,
                )
                new_maze = generator.generate()

                # マップデータの検証
                validate_maze(new_maze)

                # 検証に成功した場合のみ更新
                maze = new_maze
                save_maze_to_file(maze, config.output_file)

            except MazeGeneratorError as e:
                # 無効なマップが検出された場合の画面表示
                print("\n" + "❌ " * 15)
                print(f"【マップエラー】 {e}")
                print("❌ " * 15 + "\n")
                safe_input("Enterキーを押してメニューに戻ります...")

        elif choice == "2":
            show_solution = not show_solution
            # 経路表示
        elif choice == "3":
            # 壁の色変更
            current_color_code = change_wall_color(current_color_code)
        elif choice == "4":
            # 『42』パターンの強調表示 ON/OFF
            show_pattern_color = not show_pattern_color
        elif choice == "5":
            # テーマ/フォント変更 (Bonus)
            current_theme_id = change_theme(current_theme_id)
        elif choice == "6":
            # プレイヤー操作モード (Bonus)
            play_game_mode(
                            maze,
                            wall_color_code=current_color_code,
                            theme_id=current_theme_id,
                            )
        elif choice == "7":
            print("プログラムを終了します。")
            sys.exit(0)
        else:
            safe_input(
                f"1~{max_choice}の番号を入力してください。"
                "Enterキーを押して進みます..."
            )


if __name__ == "__main__":
    main()
