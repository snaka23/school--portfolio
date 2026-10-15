"""標準入力処理に関するユーティリティモジュール。"""

import sys


def safe_input(prompt: str) -> str:
    """ユーザーからの入力を安全に取得する関数。

    EOFError や KeyboardInterrupt (Ctrl+C / Ctrl+D) が発生した場合は
    強制終了せずメッセージを表示してプログラムを終了します。

    Args:
        prompt (str): 入力待ちの際に画面に表示するプロンプト文字列。

    Returns:
        str: 前後の空白が削除されたユーザー入力文字列。
    """
    try:
        # 1. ユーザーからの文字入力を受け取り、前後の不要な空白を削除して返す
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        # 2. 特殊な割り込みや入力終了が発生した場合にここへ飛ぶ
        print("\nプログラムを終了します。")
        sys.exit(0)
