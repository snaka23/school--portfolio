# school--portfolio

学校のカリキュラムで取り組んだ課題をまとめたリポジトリです。
C 言語の基礎から始まり、アルゴリズム、システム管理、Python までを段階（milestone）ごとに整理しています。

## 構成

```
school--portfolio/
├── milestone0/
│   └── libft/            # C標準ライブラリ関数の再実装
├── milestone1/
│   ├── ft_printf/        # printf の再実装
│   ├── get_next_line/    # ファイルを1行ずつ読み込む関数
│   └── push_swap/        # 2つのスタックを使ったソート
└── milestone2/
    ├── python_module/
    │   └── 00 〜 10/     # Python の練習課題（モジュールごと）
    ├── Born2beroot/      # Born2beRoot（Debian サーバー構築）
    └── A-Maze-ing/       # A-Maze-ing（迷路生成・解析アプリ）
```

## milestone0 — C 言語の基礎

| 課題 | 内容 | 使用技術 |
|---|---|---|
| [libft](milestone0/libft/README.md) | `strlen` や `memcpy` などの標準関数と、`split`・`itoa`・連結リスト操作などの追加関数を自作し、静的ライブラリ `libft.a` にまとめた | C, Makefile |

## milestone1 — C 言語の応用

| 課題 | 内容 | 使用技術 |
|---|---|---|
| [ft_printf](milestone1/ft_printf/README.md) | 書式指定子 `%c %s %p %d %i %u %x %X %%` に対応した `ft_printf` を実装し、`libftprintf.a` にまとめた | C, 可変長引数 (`va_list`) |
| [get_next_line](milestone1/get_next_line/README.md) | ファイルディスクリプタから1行ずつ読み込む関数。静的変数で読み残しを保持する | C, `read()`, 静的変数 |
| [push_swap](milestone1/push_swap/README.md) | 2つのスタックと決められた操作だけを使い、できるだけ少ない手数で整数を並べ替える。5 個以下は専用の小規模ソート、それより多い場合はオプションで選んだアルゴリズム（シンプルソート / チャンクソート / 基数ソート）を使う。adaptive モードでは、入力の乱れ具合に応じて自動で切り替える | C, ソートアルゴリズム |

## milestone2 — システム管理と Python

### 練習課題（`python_module/00` 〜 `10`）

| No. | テーマ | 主な内容 |
|---|---|---|
| 00 | Python の基本 | 入出力、計算、条件分岐、ループと再帰 |
| 01 | クラスとオブジェクト指向 | クラス、カプセル化、継承 |
| 02 | 例外処理 | `try` / `except` / `finally`、`raise`、独自例外 |
| 03 | データ構造 | リスト、タプル、集合、辞書、ジェネレータ、内包表記 |
| 04 | ファイル操作 | ファイルの読み書き、ストリーム、`with` 文 |
| 05 | 抽象クラスとポリモーフィズム | `abc`、データ処理パイプライン |
| 06 | モジュールとパッケージ | `import` の仕組み、パッケージ構成（`alchemy/`）、循環 import |
| 07 | デザインパターン | Factory パターン、Strategy パターン |
| 08 | 開発環境 | 仮想環境、パッケージ管理（`requirements.txt` / `pyproject.toml`）、`.env` による設定 |
| 09 | データ検証 | pydantic によるモデル定義とバリデーション |
| 10 | 関数型プログラミング | lambda、高階関数、スコープとクロージャ、`functools`、デコレータ |

### プロジェクト

| 課題 | 内容 | 使用技術 |
|---|---|---|
| [Born2beRoot](milestone2/Born2beroot/README.md) | VirtualBox 上に Debian サーバーを構築。暗号化 LVM、パスワードポリシー、sudo の厳格化、SSH（ポート 4242）、UFW、cron による監視スクリプトを設定 | Debian, LVM, SSH, UFW, cron, Bash |
| [A-Maze-ing](milestone2/A-Maze-ing/README.md) | 設定ファイルから迷路を自動生成し、最短経路の探索とファイル出力を行うアプリ。迷路生成部分は再利用できるパッケージ `mazegen` として分離した（共同制作: soinagak） | Python, DFS（バックトラッカー）, BFS, pyproject.toml |

## 使い方

各課題のディレクトリに移動して、それぞれの README の手順に従ってください。
C の課題は `make` でビルドします（get_next_line は Makefile がないため、`cc` で直接コンパイルします）。

```bash
git clone git@github.com:snaka23/school--portfolio.git
cd school--portfolio/milestone0/libft
make
```
