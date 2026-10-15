"""mazegen のユーティリティ関数群。

迷路データのファイル保存や、データ変換などの補助機能を提供します。
"""
from mazegen.maze import Cell, Maze


def cell_to_hex(cell: Cell) -> str:
    """Cellの壁情報を16進数1文字 ('0'-'F') に変換する。

    bit 0: North, bit 1: East, bit 2: South, bit 3: West
    """
    val = 0
    if cell.north:
        val |= 1
    if cell.east:
        val |= 2
    if cell.south:
        val |= 4
    if cell.west:
        val |= 8
    return f"{val:X}"


def save_maze_to_file(maze: Maze, filepath: str) -> None:
    """Mazeオブジェクトを指定されたパスに16進数フォーマットで書き出す。
    フォーマット仕様:
    - 1行目〜N行目: 各セルの壁情報を16進数表記したグリッド文字列
    - 空行
    - 入口座標 (x, y)
    - 出口座標 (x, y)
    - 解経路文字列 (例: NNEESSW...)
    """
    lines: list[str] = []

    for row in maze.cells:
        row_str = "".join(cell_to_hex(cell) for cell in row)
        lines.append(row_str)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n\n")
        f.write(f"{maze.entry[0]},{maze.entry[1]}\n")
        f.write(f"{maze.exit[0]},{maze.exit[1]}\n")
        f.write("".join(maze.solve()) + "\n")
