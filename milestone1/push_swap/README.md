*This project has been created as part of the 42 curriculum by nshuhei, snakagaw*

# push_swap

## Description

push_swap は、制限されたスタック操作のみを使用して整数列をソートするプログラムです。

本プロジェクトでは、入力データの状態に応じて複数のソート戦略を使い分けること、アルゴリズムの計算量を実感することを目的としています。

実装した戦略は以下の4種類です。

- Simple Strategy (O(n²))
- Medium Strategy (O(n√n))
- Complex Strategy (O(n log n))
- Adaptive Strategy

Adaptive Strategy は入力の乱れ度（Disorder）を計測し、自動的に最適な戦略を選択します。

---
## Algorithm Selection and Justification

### Simple Strategy (O(n²)) - Selection Sort

Simple戦略では Selection Sort を採用した。

Selection Sort は未整列部分から最小値を探索し、正しい位置へ配置する単純なアルゴリズムである。push_swap では「最小値を見つけてスタックBへ移動し、最後にスタックAへ戻す」という形で自然に実装できる。

このアルゴリズムを選択した理由は以下の通りである。

- 実装が容易で理解しやすい
- 動作が予測しやすい
- 小規模データでは十分な性能を発揮する
- 課題で要求される O(n²) の計算量クラスを明確に示せる

大規模データには適していないが、他の戦略との比較基準となるシンプルな実装として採用した。

---

### Medium Strategy (O(n√n)) - Chunk Sort

Medium戦略では Chunk Sort を採用した。

Chunk Sort は値を複数の範囲（Chunk）に分割し、各Chunkに属する要素をスタックBへ移動した後、適切な順序でスタックAへ戻す手法である。

このアルゴリズムを選択した理由は以下の通りである。

- スタックBを効率的な作業領域として利用できる
- 一度に探索する範囲を限定できる
- push_swap の操作のみで実装できる
- O(n²) の戦略より少ない操作数を実現できる
- push_swap において広く利用されている実績のある手法である

また、要素数に応じてチャンクを分割することで、課題で要求される O(n√n) の計算量クラスを満たすことを目的としている。

---

### Complex Strategy (O(n log n)) - Radix Sort

Complex戦略では LSD Radix Sort を採用した。

ソート開始前に各値を順位情報（index）へ変換し、その後は各ビットを下位ビットから順番に処理する。現在のビット値に応じて要素をスタックBへ移動し、各ビット処理終了後にスタックAへ戻すことで整列を行う。

このアルゴリズムを選択した理由は以下の通りである。

- 入力の並び方による性能差が小さい
- 実装が比較的単純である
- push_swap の操作体系と非常に相性が良い
- 大規模データでも安定した操作数を維持できる
- 100個および500個の入力に対して良好な結果が期待できる

特に push_swap の評価では実際の操作数が重要であり、入力データに依存しにくい Radix Sort は安定した性能を発揮できるため採用した。


## Features

- 不正な入力の検出
- 重複値の検出
- インデックス圧縮
- Disorder（乱れ度）の計測
- 4種類のソート戦略
- Adaptive Strategy
- ベンチマーク機能

---

## Algorithms

### Simple Strategy

小規模入力や整列済みに近い入力を想定した O(n²) のアルゴリズムです。

### Medium Strategy

チャンク分割を利用した O(n√n) のアルゴリズムです。

インデックス範囲ごとにスタックBへ退避し、順序を整えながらスタックAへ戻します。

### Complex Strategy

基数ソート（Radix Sort）を利用した O(n log n) のアルゴリズムです。

大規模入力や乱れの大きい入力を想定しています。

### Adaptive Strategy

ソート開始前に Disorder を計測し、その値に応じて戦略を選択します。

| Disorder | 選択戦略 |
|----------|----------|
| < 0.2 | Simple |
| 0.2 ～ 0.5 | Medium |
| ≥ 0.5 | Complex |

---

## Disorder

Disorder は入力列の乱れ具合を表す指標です。

値の範囲は以下の通りです。

```text
0.0 = 完全に整列済み
1.0 = 完全な逆順
```

スタック内の全ての要素ペアについて逆転している組み合わせを数えます。

```text
double	compute_disorder(t_stack *a)
{
	size_t	i;
	size_t	j;
	double	mistakes;
	double	total_pairs;

	i = 0;
	j = 0;
	mistakes = 0;
	total_pairs = 0;
	while (i < stack_size(a))
	{
		j = i + 1;
		while (j < stack_size(a))
		{
			total_pairs++;
			if (stack_at(a, i)->value > stack_at(a, j)->value)
				mistakes++;
			j++;
		}
		i++;
	}
	return (mistakes / total_pairs);
}
```

---

## Benchmark

`--bench` オプションを指定すると、ソート結果に加えて統計情報を標準エラー出力へ表示します。

表示内容：

- Disorder
- 使用した戦略
- 理論計算量
- 総操作数
- 各命令の実行回数

実行例：

```bash
./push_swap --bench $(shuf -i 1-500 -n 500 | tr '\n' ' ')
```

出力例（500個のランダムな入力の場合）：

```text
[bench] disorder:  49.93%
[bench] strategy:  Adaptive / O(n√n)
[bench] total_ops: 7997
[bench] sa: ...  sb: ...  ss: ...  pa: ...  pb: ...
[bench] ra: ...  rb: ...  rr: ... rra: ... rrb: ...  rrr:...
```

※ 要素数が5個以下の場合は、選択された戦略に関係なく小規模ソート（2〜5個専用）が使われます。

---

## Instructions

### Build

```bash
make
```

### Clean

```bash
make clean
```

### Rebuild

```bash
make re
```

### Execute

```bash
./push_swap 4 2 1 3
```

戦略を明示的に指定する場合（オプションは数値より前に置きます。戦略オプションを指定しない場合は `--adaptive` として動作します）：

```bash
./push_swap --simple 4 2 1 3
./push_swap --medium 4 2 1 3
./push_swap --complex 4 2 1 3
./push_swap --adaptive 4 2 1 3
```

---

## Performance

課題で要求されている目標値は以下の通りです。

| Size | Pass | Good | Excellent |
|--------|--------|--------|--------|
| 100 | < 2000 | < 1500 | < 700 |
| 500 | < 12000 | < 8000 | < 5500 |

---

## Error Handling

以下の場合は標準エラー出力へ `ERROR` を表示します。

- 整数以外の入力
- int範囲外の値
- 重複値
- 不正なオプション
- 異なる戦略オプションの同時指定（例: `--simple --medium`）

---

## Resources
### References

- push_swap Subject
- Radix Sort Documentation
- Stack Sorting Articles

### AI Usage

以下の用途でAIを利用しました。

- アルゴリズムの比較検討
- 計算量の確認
- リファクタリング案の検討
- README作成補助

最終的な実装内容については全て確認・理解したうえで採用しています。

---

## Contributions

### nshuhei

- パーサ実装
- Disorder計測
- Benchmark機能
- テスト

### snakagaw

- ソートアルゴリズム実装
- スタック操作実装
- 最適化
- テスト