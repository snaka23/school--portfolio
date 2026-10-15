from dataclasses import dataclass, field
import random


@dataclass
class Cell:
    """迷路の1マスが持つ、東西南北の壁の有無を表すクラス。

    Attributes:
        north: 北側の壁があれば True。
        east: 東側の壁があれば True。
        south: 南側の壁があれば True。
        west: 西側の壁があれば True。
    """
    north: bool
    east: bool
    south: bool
    west: bool


class MazeGeneratorError(Exception):
    """迷路の生成、検証に失敗した際に送出する例外。"""
    def __init__(self, message: str = "Invalid Maze data.") -> None:
        """例外を作成する。

        Args:
            message: エラーの内容を表すメッセージ。
        """
        self.message = message
        super().__init__(self.message)


@dataclass
class Maze:
    """生成済みの迷路データ。

    Attributes:
        width: 迷路の幅(セル数)。
        height: 迷路の高さ(セル数)。
        entry: 入口の座標 (x, y)。
        exit: 出口の座標 (x, y)。
        cells: 迷路の壁情報。cells[y][x] で参照する。
        pattern_cells: 「42」パターンを構成するセルの座標集合。
        pattern_drawn: 「42」パターンを描画できたかどうか。
    """
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    cells: list[list[Cell]]
    pattern_cells: frozenset[tuple[int, int]] = field(
        default_factory=frozenset)
    pattern_drawn: bool = False

    def solve(self) -> list[str]:
        """entryからexitまでの最短経路をBFSで求める。

        Returns:
            entryからexitまでの移動方向('N'/'E'/'S'/'W')のリスト。

        Raises:
            MazeGeneratorError: entryからexitへ到達する経路が
                存在しない場合。
        """
        queue: list[tuple[int, int]] = [self.entry]
        visited: set[tuple[int, int]] = {self.entry}
        came_from: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
        while queue:
            current = queue.pop(0)
            current_x, current_y = current
            neighbors = _open_neighbors(self, current_x, current_y)
            candidates: list[tuple[int, int]] = []
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                if neighbor in self.pattern_cells:
                    continue
                candidates.append(neighbor)
            if not candidates:
                continue
            for candidate in candidates:
                visited.add(candidate)
                queue.append(candidate)
                candidate_x, candidate_y = candidate
                if candidate_x == current_x:
                    if candidate_y > current_y:
                        came_from[candidate] = ((current), "S")
                    else:
                        came_from[candidate] = ((current), "N")
                else:
                    if candidate_x > current_x:
                        came_from[candidate] = ((current), "E")
                    else:
                        came_from[candidate] = ((current), "W")
            if self.exit in came_from:
                break
        if self.exit not in came_from:
            raise MazeGeneratorError("no path exists from entry to exit")
        reversed_path: list[str] = []
        path: list[str] = []
        place = self.exit
        while True:
            previous, direction = came_from[place]
            reversed_path.append(direction)
            place = previous
            if place == self.entry:
                break
        while reversed_path:
            step = reversed_path.pop()
            path.append(step)
        return path


class MazeGenerator:
    """迷路を生成するクラス。

    Attributes:
        width: 迷路の幅(セル数)。
        height: 迷路の高さ(セル数)。
        perfect: True なら完全迷路(ループなし)、False ならループのある
            プレイ可能な盤面を生成する。
        rng: 再現性のために保持する乱数生成器。

    Example:
        基本的な使い方(サイズ・シードなどのカスタムパラメータを渡し、
        生成された構造と最短経路(解)にアクセスする):

        >>> generator = MazeGenerator(
        ...     width=20, height=15,
        ...     entry=(0, 0), exit=(19, 14),
        ...     perfect=True, seed=42,
        ... )
        >>> maze = generator.generate()  # 生成された構造にアクセス
        >>> path = maze.solve()          # 少なくとも1つの解にアクセス
    """
    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        perfect: bool,
        seed: int | None = None
    ) -> None:
        """引数を検証し、生成に使う値として保持する。

        Args:
            width: 迷路の幅(セル数)。1以上である必要がある。
            height: 迷路の高さ(セル数)。1以上である必要がある。
            entry: 入口の座標 (x, y)。
            exit: 出口の座標 (x, y)。entryと異なる必要がある。
            perfect: True なら完全迷路、False ならプレイ可能な盤面を
                生成する。
            seed: 乱数シード。Noneなら非決定的な乱数になる。

        Raises:
            MazeGeneratorError: width/heightが0以下、entryとexitが
                同じ、またはentry/exitが盤面の範囲外の場合。
        """
        if width <= 0 or height <= 0:
            raise MazeGeneratorError("width and height must be positive")
        self.width = width
        self.height = height
        if entry == exit:
            raise MazeGeneratorError("entry and exit are same")
        self.entry_x, self.entry_y = entry
        if not (
            0 <= self.entry_x < self.width
            and 0 <= self.entry_y < height
        ):
            raise MazeGeneratorError("entry is not valid")
        self.exit_x, self.exit_y = exit
        if not (
            0 <= self.exit_x < self.width
            and 0 <= self.exit_y < height
        ):
            raise MazeGeneratorError("exit is not valid")
        self.perfect = perfect
        self.rng = random.Random(seed)

    def generate(self) -> Maze:
        """新しい迷路を生成して返す。

        Returns:
            生成された Maze。

        Raises:
            MazeGeneratorError: perfect=Falseで、独立ループが2本未満
                のまま生成が終わった場合。
        """
        cells: list[list[Cell]] = []
        pattern_cells = self._pattern_cells()
        if not pattern_cells:
            print(
                "'42' pattern omitted "
                "(maze too small or entry/exit overlaps it)"
            )
        for _ in range(self.height):
            cell: list[Cell] = []
            for _ in range(self.width):
                cell.append(Cell(True, True, True, True))
            cells.append(cell)
        visited: set[tuple[int, int]] = {(self.entry_x, self.entry_y)}
        stack: list[tuple[int, int]] = [(self.entry_x, self.entry_y)]
        while stack:
            current = stack[-1]
            current_x, current_y = current
            neighbors = [
                (current_x, current_y + 1),
                (current_x + 1, current_y),
                (current_x - 1, current_y),
                (current_x, current_y - 1)
            ]
            candidates: list[tuple[int, int]] = []
            for neighbor in neighbors:
                neighbor_x, neighbor_y = neighbor
                if not (
                    0 <= neighbor_x < self.width
                    and 0 <= neighbor_y < self.height
                ):
                    continue
                if neighbor in visited:
                    continue
                if neighbor in pattern_cells:
                    continue
                candidates.append(neighbor)
            if not candidates:
                stack.pop()
            else:
                next_cell = self.rng.choice(candidates)
                next_x, next_y = next_cell
                if next_x == current_x:
                    if next_y > current_y:
                        cells[next_y][next_x].north = False
                        cells[current_y][current_x].south = False
                    else:
                        cells[next_y][next_x].south = False
                        cells[current_y][current_x].north = False
                else:
                    if next_x > current_x:
                        cells[next_y][next_x].west = False
                        cells[current_y][current_x].east = False
                    else:
                        cells[next_y][next_x].east = False
                        cells[current_y][current_x].west = False
                stack.append(next_cell)
                visited.add(next_cell)
        if not self.perfect:
            self._add_loops(cells)
            self._ensure_corners_and_center_open(cells)
            if self._count_loops(cells) < 2:
                raise MazeGeneratorError(
                    "maze has fewer than 2 independent loops "
                    "(a playable board needs at least 2)"
                )
        return Maze(
            self.width,
            self.height,
            (self.entry_x, self.entry_y),
            (self.exit_x, self.exit_y),
            cells,
            pattern_cells,
            bool(pattern_cells)
        )

    def _find_dead_ends(
        self, cells: list[list[Cell]]
    ) -> list[tuple[int, int]]:
        """開いている壁が1本だけのセル(行き止まり)の座標一覧を返す。

        Args:
            cells: 迷路の壁情報(cells[y][x])。

        Returns:
            行き止まりセルの (x, y) 座標のリスト。
        """
        dead_ends: list[tuple[int, int]] = []
        for y in range(self.height):
            for x in range(self.width):
                cell = cells[y][x]
                wall = (cell.north, cell.east, cell.west, cell.south)
                if wall.count(False) == 1:
                    dead_ends.append((x, y))
        return dead_ends

    def _is_3x3_open(self, cells: list[list[Cell]], x: int, y: int) -> bool:
        """左上座標(x, y)の3x3ブロックが、内部の12本の壁すべて開いて
        いる(完全に空洞になっている)かどうかを返す。

        Args:
            cells: 迷路の壁情報(cells[y][x])。
            x: 3x3ブロックの左上セルのx座標。
            y: 3x3ブロックの左上セルのy座標。

        Returns:
            ブロックが完全に空洞なら True。
        """
        for dy in range(3):
            for dx in range(2):
                if cells[y + dy][x + dx].east:
                    return False
        for dy in range(2):
            for dx in range(3):
                if cells[y + dy][x + dx].south:
                    return False
        return True

    def _candidate_blocks(
        self,
        x: int,
        y: int,
        next_x: int,
        next_y: int
    ) -> list[tuple[int, int]]:
        """(x, y)と(next_x, next_y)の間の壁を取り除いた場合に影響を
        受けうる3x3ブロックの左上座標一覧を返す。

        Args:
            x: 1つ目のセルのx座標。
            y: 1つ目のセルのy座標。
            next_x: 隣接するセルのx座標。
            next_y: 隣接するセルのy座標。

        Returns:
            影響を受けうる3x3ブロックの左上座標のリスト。
        """
        blocks: list[tuple[int, int]] = []
        x_candidate: tuple[int, ...]
        y_candidate: tuple[int, ...]
        if x == next_x:
            lo_y = min(y, next_y)
            x_candidate = (x - 2, x - 1, x)
            y_candidate = (lo_y - 1, lo_y)
        else:
            lo_x = min(x, next_x)
            x_candidate = (lo_x - 1, lo_x)
            y_candidate = (y - 2, y - 1, y)
        for bx in x_candidate:
            for by in y_candidate:
                if (
                    0 <= bx and bx + 2 < self.width
                    and 0 <= by and by + 2 < self.height
                ):
                    blocks.append((bx, by))
        return blocks

    def _set_wall(
        self,
        cells: list[list[Cell]],
        x: int,
        y: int,
        next_x: int,
        next_y: int,
        value: bool
    ) -> None:
        """(x, y)と(next_x, next_y)が共有する壁を、両側とも value に
        設定する。

        Args:
            cells: 迷路の壁情報(cells[y][x])。この場で書き換える。
            x: 1つ目のセルのx座標。
            y: 1つ目のセルのy座標。
            next_x: 隣接するセルのx座標。
            next_y: 隣接するセルのy座標。
            value: 壁に設定する値(True=壁あり、False=壁なし)。
        """
        if x == next_x:
            if y > next_y:
                cells[y][x].north = value
                cells[next_y][next_x].south = value
            else:
                cells[y][x].south = value
                cells[next_y][next_x].north = value
        else:
            if x > next_x:
                cells[y][x].west = value
                cells[next_y][next_x].east = value
            else:
                cells[y][x].east = value
                cells[next_y][next_x].west = value

    def _can_remove_wall(
        self,
        cells: list[list[Cell]],
        x: int,
        y: int,
        next_x: int,
        next_y: int,
    ) -> bool:
        """(x, y)と(next_x, next_y)の間の壁を取り除く。ただし取り除く
        ことで3x3ブロックが完全に空洞になる場合は壁を元に戻し、
        False を返す。

        Args:
            cells: 迷路の壁情報(cells[y][x])。この場で書き換える。
            x: 1つ目のセルのx座標。
            y: 1つ目のセルのy座標。
            next_x: 隣接するセルのx座標。
            next_y: 隣接するセルのy座標。

        Returns:
            壁を取り除けたなら True。3x3の空洞ができるため元に
            戻したなら False。
        """
        candidate_blocks = self._candidate_blocks(x, y, next_x, next_y)
        self._set_wall(cells, x, y, next_x, next_y, False)
        for blocks in candidate_blocks:
            bx, by = blocks
            if self._is_3x3_open(cells, bx, by):
                self._set_wall(cells, x, y, next_x, next_y, True)
                return False
        return True

    def _add_loops(self, cells: list[list[Cell]]) -> None:
        """すべての行き止まりについて、壁を1本開けられないか試す。
        「42」パターンや3x3の空洞を作らずに開けられる場合はループに
        変わる。

        Args:
            cells: 迷路の壁情報(cells[y][x])。この場で書き換える。
        """
        dead_ends = self._find_dead_ends(cells)
        pattern_cells = self._pattern_cells()
        for x, y in dead_ends:
            cell = cells[y][x]
            directions: list[tuple[int, int]] = []
            if cell.north:
                directions.append((x, y - 1))
            if cell.east:
                directions.append((x + 1, y))
            if cell.west:
                directions.append((x - 1, y))
            if cell.south:
                directions.append((x, y + 1))
            self.rng.shuffle(directions)
            for dx, dy in directions:
                if not (
                    0 <= dx < self.width
                    and 0 <= dy < self.height
                ):
                    continue
                if (dx, dy) in pattern_cells:
                    continue
                if self._can_remove_wall(cells, x, y, dx, dy):
                    break

    def _ensure_open(self, cells: list[list[Cell]], x: int, y: int) -> None:
        """(x, y)が完全に閉じていて「42」パターンの一部でもない場合、
        (パターンに属さない隣接セルへの)壁を1本開ける。

        Args:
            cells: 迷路の壁情報(cells[y][x])。この場で書き換える。
            x: 対象セルのx座標。
            y: 対象セルのy座標。
        """
        cell = cells[y][x]
        pattern_cells = self._pattern_cells()
        if (x, y) in pattern_cells:
            return
        if not (cell.north and cell.east and cell.west and cell.south):
            return
        directions = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for next_x, next_y in directions:
            if not (0 <= next_x < self.width and 0 <= next_y < self.height):
                continue
            if (next_x, next_y) in pattern_cells:
                continue
            if self._can_remove_wall(cells, x, y, next_x, next_y):
                return

    def _ensure_corners_and_center_open(self, cells: list[list[Cell]]) -> None:
        """四隅と中央のセルは、「42」パターンの一部である場合を除き、
        完全に閉じたままにならないようにする。

        Args:
            cells: 迷路の壁情報(cells[y][x])。この場で書き換える。
        """
        coners_and_center = [
            (0, 0),
            (0, self.height - 1),
            (self.width - 1, 0),
            (self.width - 1, self.height - 1),
            (self.width // 2, self.height // 2)
        ]
        for x, y in coners_and_center:
            self._ensure_open(cells, x, y)

    def _pattern_cells(self) -> frozenset[tuple[int, int]]:
        """迷路の中央に配置する「42」パターンが占める座標一覧を返す。
        余白を含めてもパターンが収まらないほど盤面が小さい場合、
        またはentry/exitがパターンと重なる場合は空集合を返す。

        Returns:
            「42」パターンを構成するセルの座標集合。描画できない
            場合は空集合。
        """
        pattern_width = 7
        pattern_height = 5
        margin = 1
        _PATTERN_42 = [
            "1000111",
            "1000001",
            "1110111",
            "0010100",
            "0010111"
        ]
        if self.width < pattern_width + margin * 2:
            return frozenset()
        if self.height < pattern_height + margin * 2:
            return frozenset()
        offset_x = -(-(self.width - pattern_width) // 2)
        offset_y = (self.height - pattern_height) // 2
        cells = set()
        for row_index, row in enumerate(_PATTERN_42):
            for col_index, ch in enumerate(row):
                if ch == "1":
                    cells.add((offset_x + col_index, offset_y + row_index))
        entry = (self.entry_x, self.entry_y)
        exit = (self.exit_x, self.exit_y)
        if entry in cells or exit in cells:
            return frozenset()
        return frozenset(cells)

    def _count_loops(self, cells: list[list[Cell]]) -> int:
        """迷路に含まれる独立ループの本数を返す。

        各セルの東・南の壁が開いている数を迷路グラフの辺として数え、
        全域木の辺数(連結しているセル数 - 1)を引くことで、独立した
        閉路(ループ)の本数を求める。

        Args:
            cells: 迷路の壁情報(cells[y][x])。

        Returns:
            独立ループの本数。
        """
        count_loops = 0
        pattern = len(self._pattern_cells())
        for x in range(self.width):
            for y in range(self.height):
                cell = cells[y][x]
                wall = [cell.east, cell.south]
                count_loops += wall.count(False)
        independent = count_loops - (self.width * self.height - pattern - 1)
        return independent


def _check_entry_exit(maze: Maze) -> None:
    """entry/exitが不正な場合に MazeGeneratorError を送出する。

    Args:
        maze: 検証対象の Maze。

    Raises:
        MazeGeneratorError: entryまたはexitが迷路の範囲外にある場合、
            またはentryとexitが同じセルの場合。
    """
    entry_x, entry_y = maze.entry
    exit_x, exit_y = maze.exit
    if not (0 <= entry_x < maze.width and 0 <= entry_y < maze.height):
        raise MazeGeneratorError("entry is not valid")
    if not (0 <= exit_x < maze.width and 0 <= exit_y < maze.height):
        raise MazeGeneratorError("exit is not valid")
    if maze.entry == maze.exit:
        raise MazeGeneratorError("entry and exit are same")


def _check_wall_consistency(maze: Maze) -> None:
    """隣接セル同士の壁情報が食い違う場合に MazeGeneratorError を送出する。

    Args:
        maze: 検証対象の Maze。

    Raises:
        MazeGeneratorError: あるセルの壁が、その壁を挟んで隣接する
            セル側の対応する壁と一致しない場合。
    """
    for x in range(maze.width):
        for y in range(maze.height):
            cell = maze.cells[y][x]
            directions = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            for next_x, next_y in directions:
                if not (
                    0 <= next_x < maze.width
                    and 0 <= next_y < maze.height
                ):
                    continue
                next_cell = maze.cells[next_y][next_x]
                if next_x == x:
                    if next_y == y - 1:
                        if cell.north != next_cell.south:
                            raise MazeGeneratorError(
                                "wall is not coherent between "
                                "neighbouring cells"
                            )
                    else:
                        if cell.south != next_cell.north:
                            raise MazeGeneratorError(
                                "wall is not coherent between "
                                "neighbouring cells"
                            )
                else:
                    if next_x == x - 1:
                        if cell.west != next_cell.east:
                            raise MazeGeneratorError(
                                "wall is not coherent between "
                                "neighbouring cells"
                            )
                    else:
                        if cell.east != next_cell.west:
                            raise MazeGeneratorError(
                                "wall is not coherent between "
                                "neighbouring cells"
                            )


def _check_border_walls(maze: Maze) -> None:
    """迷路の外周に開いた壁がある場合に MazeGeneratorError を送出する。

    Args:
        maze: 検証対象の Maze。

    Raises:
        MazeGeneratorError: 上下左右いずれかの端のセルで、外側を
            向いた壁が開いている場合。
    """
    for x in range(maze.width):
        cell = maze.cells[0][x]
        if not cell.north:
            raise MazeGeneratorError(
                "border wall is open (outer walls must stay closed)"
            )
        cell = maze.cells[maze.height - 1][x]
        if not cell.south:
            raise MazeGeneratorError(
                "border wall is open (outer walls must stay closed)"
            )
    for y in range(maze.height):
        cell = maze.cells[y][0]
        if not cell.west:
            raise MazeGeneratorError(
                "border wall is open (outer walls must stay closed)"
            )
        cell = maze.cells[y][maze.width - 1]
        if not cell.east:
            raise MazeGeneratorError(
                "border wall is open (outer walls must stay closed)"
            )


def _open_neighbors(maze: Maze, x: int, y: int) -> list[tuple[int, int]]:
    """(x, y)から壁を通って行ける隣接セルの座標一覧を返す。

    Args:
        maze: 対象の Maze。
        x: 対象セルのx座標。
        y: 対象セルのy座標。

    Returns:
        壁が開いている隣接セルの (x, y) 座標のリスト。
    """
    cell = maze.cells[y][x]
    open_neighbors: list[tuple[int, int]] = []
    if not cell.north and (0 <= x < maze.width and 0 <= y - 1 < maze.height):
        open_neighbors.append((x, y - 1))
    if not cell.east and (0 <= x + 1 < maze.width and 0 <= y < maze.height):
        open_neighbors.append((x + 1, y))
    if not cell.west and (0 <= x - 1 < maze.width and 0 <= y < maze.height):
        open_neighbors.append((x - 1, y))
    if not cell.south and (0 <= x < maze.width and 0 <= y + 1 < maze.height):
        open_neighbors.append((x, y + 1))
    return open_neighbors


def _check_connectivity(maze: Maze) -> None:
    """「42」パターン以外のセルにentryから到達できない場合に
    MazeGeneratorError を送出する。

    maze.entryから壁の開いている方向を辿るDFS(自前スタック)で
    到達可能なセルを集め、maze.pattern_cells以外の全セルが訪問済み
    かどうかを確認する。

    Args:
        maze: 検証対象の Maze。

    Raises:
        MazeGeneratorError: 「42」パターン以外のセルで、entryから
            到達できないものがある場合。
    """
    visited: set[tuple[int, int]] = {maze.entry}
    stack: list[tuple[int, int]] = [maze.entry]
    pattern_cells = maze.pattern_cells
    while stack:
        current = stack[-1]
        current_x, current_y = current
        neighbors = _open_neighbors(maze, current_x, current_y)
        candidate = None
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if neighbor in pattern_cells:
                continue
            candidate = neighbor
            break
        if not candidate:
            stack.pop()
            continue
        stack.append(candidate)
        visited.add(candidate)
    for x in range(maze.width):
        for y in range(maze.height):
            if (x, y) not in visited:
                if (x, y) not in pattern_cells:
                    raise MazeGeneratorError(
                        "cell is isolated (not reachable from entry)"
                    )


def validate_maze(maze: Maze) -> None:
    """迷路を検証し、最初に見つかった問題で MazeGeneratorError を送出する。

    entry/exit、壁の整合性、外周の壁、連結性の順にチェックする。

    Args:
        maze: 検証対象の Maze。

    Raises:
        MazeGeneratorError: 上記のいずれかのチェックに失敗した場合。
    """
    _check_entry_exit(maze)
    _check_wall_consistency(maze)
    _check_border_walls(maze)
    _check_connectivity(maze)
