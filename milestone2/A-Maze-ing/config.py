from mazegen.maze import MazeGeneratorError
from dataclasses import dataclass


def _read_pairs(path: str) -> dict[str, str]:
    """設定ファイルから 'KEY=VALUE' の行を読み込み、辞書にして返す。

    空行と '#' で始まる行は無視する。

    Args:
        path: 設定ファイルのパス。

    Returns:
        キーと値の対応を持つ辞書。

    Raises:
        MazeGeneratorError: ファイルを開けない、または読み込めない場合。
    """
    pairs: dict[str, str] = {}
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, _, value = line.partition("=")
                pairs[key.strip()] = value.strip()
    except OSError:
        raise MazeGeneratorError(f"could not open config file: {path}")
    return pairs


def _check_required_keys(pairs: dict[str, str]) -> None:
    """必須の設定キーが1つでも欠けている場合に MazeGeneratorError を送出する。

    Args:
        pairs: `_read_pairs` で読み込んだキーと値の辞書。

    Raises:
        MazeGeneratorError: WIDTH、HEIGHT、ENTRY、EXIT、OUTPUT_FILE、
            PERFECTのいずれかが pairs に存在しない場合。
    """
    key_name = (
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
    )
    for key in key_name:
        if key not in pairs:
            raise MazeGeneratorError(f"Missing required key: {key}")


def _parse_int(pairs: dict[str, str], key: str) -> int:
    """pairs[key] を int としてパースする。

    Args:
        pairs: 設定値の辞書。
        key: パース対象のキー名。

    Returns:
        パースした整数値。

    Raises:
        MazeGeneratorError: 値が数値として解釈できない場合。
    """
    try:
        num = int(pairs[key])
    except ValueError:
        raise MazeGeneratorError(f"{key} is not numeric")
    return num


def _parse_coord(pairs: dict[str, str], key: str) -> tuple[int, int]:
    """pairs[key] の 'x,y' 形式の座標文字列をパースする。

    Args:
        pairs: 設定値の辞書。
        key: パース対象のキー名。

    Returns:
        パースした (x, y) 座標。

    Raises:
        MazeGeneratorError: カンマがない、または数値として解釈できない
            場合。
    """
    if "," in pairs[key]:
        try:
            x, _, y = pairs[key].partition(",")
            num_x = int(x)
            num_y = int(y)
        except ValueError:
            raise MazeGeneratorError(
                f"{key} must be in 'x,y' format (e.g. 0,0)"
            )
    else:
        raise MazeGeneratorError(f"{key} must be in 'x,y' format (e.g. 0,0)")
    return (num_x, num_y)


def _check_output_writable(output_file: str) -> None:
    """output_file が書き込み用に開けない場合に MazeGeneratorError を
    送出する。

    Args:
        output_file: 書き込み可否を確認する出力ファイルのパス。

    Raises:
        MazeGeneratorError: ファイルを書き込みモードで開けない場合。
    """
    try:
        with open(output_file, "a", encoding="utf-8"):
            pass
    except OSError:
        raise MazeGeneratorError(f"OUTPUT_FILE is not writable: {output_file}")


def _parse_bool(pairs: dict[str, str], key: str) -> bool:
    """pairs[key]('True' または 'False') を bool としてパースする。

    Args:
        pairs: 設定値の辞書。
        key: パース対象のキー名。

    Returns:
        パースした真偽値。

    Raises:
        MazeGeneratorError: 値が 'True' でも 'False' でもない場合。
    """
    if pairs[key] == "True":
        return True
    elif pairs[key] == "False":
        return False
    else:
        raise MazeGeneratorError(f"{key} must be 'True' or 'False'")


def _parse_optional_int(pairs: dict[str, str], key: str) -> int | None:
    """pairs[key] を int としてパースする。キーが無ければ None を返す。

    Args:
        pairs: 設定値の辞書。
        key: パース対象のキー名。

    Returns:
        パースした整数値。キーが存在しなければ None。

    Raises:
        MazeGeneratorError: キーは存在するが数値として解釈できない場合。
    """
    if key not in pairs:
        return None
    try:
        num = int(pairs[key])
    except ValueError:
        raise MazeGeneratorError(f"{key} is not numeric")
    return num


@dataclass
class Config:
    """迷路の生成と出力に必要な、パース済みの設定値。

    Attributes:
        width: 迷路の幅(セル数)。
        height: 迷路の高さ(セル数)。
        entry: 入口の座標 (x, y)。
        exit: 出口の座標 (x, y)。
        output_file: 出力ファイルのパス。
        perfect: True なら完全迷路、False ならプレイ可能な盤面。
        seed: 乱数シード。指定がなければ None。
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None = None


def parse_config(path: str) -> Config:
    """設定ファイルを読み込んで検証し、値を Config として返す。

    Args:
        path: 設定ファイルのパス。

    Returns:
        パース済みの Config。

    Raises:
        MazeGeneratorError: ファイルが読めない、必須キーが欠けている、
            または値の形式が不正な場合。
    """
    try:
        maze_dict = _read_pairs(path)
        _check_required_keys(maze_dict)
        width = _parse_int(maze_dict, "WIDTH")
        height = _parse_int(maze_dict, "HEIGHT")
        entry = _parse_coord(maze_dict, "ENTRY")
        exit = _parse_coord(maze_dict, "EXIT")
        output_file = maze_dict["OUTPUT_FILE"]
        _check_output_writable(output_file)
        perfect = _parse_bool(maze_dict, "PERFECT")
        seed = _parse_optional_int(maze_dict, "SEED")
    except MazeGeneratorError as e:
        raise MazeGeneratorError(f"{e}")
    return Config(
        width,
        height,
        entry,
        exit,
        output_file,
        perfect,
        seed
    )
