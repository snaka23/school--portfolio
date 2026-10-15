*This project has been created as part of the 42 curriculum by snakagaw.*

## Description(説明)
Born2beRootは、42カリキュラムにおけるシステム管理課題です。VirtualBox上にDebianサーバーをインストールし、以下の要件を満たす仮想マシンを構築します。
- LVM + 暗号化パーティションによるディスク構成
- 強力なパスワードポリシー
- sudoの厳格化
- SSHをポート4242で稼働させ、rootでの直接ログインを禁止
- UFWファイアウォールでポート4242のみを許可
- サーバーの状態を10分ごとに全端末へ表示するmonitoring.shスクリプト(cronで自動実行)

## Instructions(手順)
このプロジェクトの成果物は「動作する仮想マシン」そのものであり、提出するのは`README.md`と`signature.txt`のみです。以下は同じ環境を再現する場合の手順の概要です。
### 1. 仮想マシンの作成
- VirtualBoxで新規VMを作成
- Debian netinstのISOをテキストモードでインストール(要件の指定があったため)
### 2. インストール時の設定
- hostname: `snakagaw42`
- 手動パーティショニング: /boot(非暗号化) + LVM on 暗号化ボリューム(root/swap/home)
### 3. インストール後の設定(必須パート)

| 項目 | 内容 |
|---|---|
| ユーザー/グループ | `snakagaw`を`user42`・`sudo`グループへ追加 |
| パスワードポリシー | `/etc/login.defs`(期限30日/最短2日/警告7日前)、`/etc/security/pwquality.conf`(`libpam-pwquality`の設定、10文字以上・大小英数字必須・同一文字4連続禁止・ユーザー名禁止・前回との差分7文字以上)、`/etc/pam.d/common-password`(rootにも同ポリシーを適用しつつ`difok`のみ除外する分岐設定)。ただし`login.defs`の期限設定は新規作成ユーザーにのみ適用されるため、インストール時に作成済みの`root`・`snakagaw`には`chage -M 30 -m 2 -W 7 ユーザー名`で個別に反映する必要がある(`chage -l`で確認したところ初期値`99999`日のままだった) |
| sudo厳格化 | `sudo visudo -f /etc/sudoers.d/b2b`で新規ファイルを作成し、試行3回制限・カスタムエラーメッセージ・入出力ログ(`/var/log/sudo/`)・TTY必須(`requiretty`)・secure_path制限を設定。`sudoers`関連ファイルは直接`nano`等で編集せず、必ず`visudo`経由で編集する(保存時に自動で構文チェックされ、構文ミスによる`sudo`/ログイン不能事故を防げるため) |
| SSH | `/etc/ssh/sshd_config`で`Port 4242`・`PermitRootLogin no` |
| ファイアウォール | `sudo apt install ufw` → `sudo ufw allow 4242`(有効化前に許可ルールを先に追加、順番が重要)→ `sudo ufw enable` でポート4242のみ許可、他は拒否 |
| monitoring.sh | `/usr/local/bin/monitoring.sh`に配置、cron(`*/10 * * * *`と`@reboot`)で自動実行 |

### 4. 動作確認

```bash
hostname                              # snakagaw42
groups snakagaw                       # user42, sudo を含む
sudo ss -tunlp | grep ssh             # 0.0.0.0:4242
sudo ufw status verbose               # 4242のみALLOW
sudo /usr/local/bin/monitoring.sh     # 監視スクリプトの手動実行
sudo crontab -l                       # cron登録確認
```

### 5. ホストマシンからのSSH接続(任意)
VMはデフォルトでNATモードのネットワークのため、外部から直接アクセスできない。VirtualBoxのポートフォワーディング機能で、ホストの任意のポートをVMの4242番へ転送する。

```bash
VBoxManage controlvm snakagaw42 natpf1 "ssh,tcp,,2222,,4242"
ssh -p 2222 snakagaw@localhost
```

### 6. 提出物
- `signature.txt`: VMをシャットダウンした最終状態で、ディスクイメージ(`.vdi`)のsha1ハッシュを計算して記載
  ```bash
  sha1sum snakagaw42.vdi
  ```

## Project description(プロジェクト説明)

### OS選択: Debian

今回は`Debian`(最新安定版)を選択しました。

**長所**: `apt`によるパッケージ管理が扱いやすく学習コストが低い。ドキュメント・情報量が多く初心者向け。
**短所**: Debianにも強制アクセス制御(MAC)機能はAppArmorとして備わっているが、企業の商用環境(RHEL/Rocky系)ではSELinuxの方が主流のため、実務で使う機会という点ではRockyを選ぶより経験値になりにくい。

初めてのシステム管理課題であり、課題文でも初心者にはDebianが推奨されていたため、Debianを選択しました。Rocky Linuxとの詳しい比較は下記「比較」セクションを参照してください。

### 設計上の主な選択

- **パーティショニング**: `/boot`(非暗号化, ext4)+ LVM on LUKS暗号化ボリューム(`root`/`swap`/`home`の3論理ボリューム)。起動時にパスフレーズなしで読める必要がある`/boot`だけを暗号化の外に出し、それ以外をLVM+暗号化で保護する構成にした。
- **セキュリティポリシー**: パスワード期限・複雑さの強制に加え、root自身のパスワード変更にもポリシーを適用(`pam_succeed_if`でrootのみ`difok`(前回との差分チェック)を除外する分岐処理を実装)。
- **ユーザー管理**: 一般ユーザー`snakagaw`を`user42`・`sudo`グループへ所属させ、root直接操作を避けsudo経由での権限昇格に統一。
- **インストールしたサービス**: OpenSSH server、UFW、libpam-pwquality、sudo。グラフィカル環境は一切インストールしていない。

### monitoring.shの仕組み

`monitoring.sh`(`/usr/local/bin/monitoring.sh`に配置、cronで10分ごと・起動時に自動実行)は、以下11項目の情報を各コマンドで取得し、最後に`wall`(ログイン中の全端末へ一斉表示するコマンド)でまとめてブロードキャストするbashスクリプト。

| 表示項目 | 取得コマンド | やっていること |
|---|---|---|
| OSアーキテクチャ・カーネルバージョン | `uname -a` | カーネル名・ホスト名・バージョン・アーキテクチャをまとめて取得 |
| 物理CPU数 | `lscpu \| grep "^Socket(s):" \| awk '{print $2}'` | CPUソケット数(物理CPU数)を抽出 |
| 仮想CPU数 | `nproc` | システムが認識している論理プロセッサ数を取得 |
| RAM使用率 | `free -m \| awk 'NR==2 {printf "%s/%sMB (%.2f%%)", $3, $2, $3*100/$2}'` | メモリ使用状況の`Mem:`行から使用中/合計を取り出し使用率を計算 |
| ディスク使用率 | `df -m \| grep '^/dev/' \| awk '{used+=$3; total+=$2} END {printf "%s/%sMB (%d%%)", used, total, used*100/total}'` | 実ディスク区画(`/`, `/home`, `/boot`)の使用量を合算し使用率を計算 |
| CPU使用率 | `vmstat 1 2 \| tail -1 \| awk '{printf "%d%%", 100-$15}'` | 1秒間隔で2回計測し、idle(待機率)の逆数から使用率を算出 |
| 最終再起動日時 | `uptime -s` | システム起動時刻を、ロケールに依存しない`YYYY-MM-DD HH:MM:SS`形式で取得 |
| LVM使用の有無 | `lsblk \| grep -c lvm` | `lsblk`の出力に`lvm`という文字列を含む行があるかで判定 |
| アクティブな接続数 | `ss -ta \| grep ESTAB \| wc -l` | 確立済み(ESTABLISHED)のTCP接続数をカウント |
| ログイン中ユーザー数 | `who -q \| tail -1 \| awk -F= '{print $2}'` | `who -q`が出力する合計行(`# users=N`)から`N`を取り出す |
| IPv4・MACアドレス | `hostname -I \| awk '{print $1}'` / `ip a \| grep "link/ether" \| awk '{print $2}'` | 割り当てIPの先頭1つと、`link/ether`行からMACアドレスを取得 |
| sudo実行回数 | `grep -c COMMAND /var/log/sudo/sudo.log` | `/etc/sudoers.d/b2b`の`log_input`/`log_output`で生成されるログから`COMMAND=`を含む行数をカウント |

スクリプト自体はroot権限のcrontabから実行されるため、スクリプト内部で`sudo`は使用していない。

### 比較

**Debian vs Rocky Linux**
- Debianは`apt`/`aptitude`によるパッケージ管理、コミュニティ主導の安定ディストリビューション。
- Rockyは企業用向けの商用Linuxの無償クローンで、SELinuxによる強制アクセス制御がデフォルトで有効。設定はDebianより複雑になりがち。

**AppArmor vs SELinux**
- AppArmor(Debian)はファイルパスベースでアプリケーションごとに許可する操作をプロファイルとして定義する。設定がシンプルで導入しやすい。
- SELinux(Rocky)はラベル(コンテキスト)ベースのより厳密で強制力の強いアクセス制御。柔軟だが設定・デバッグが難しい。

**UFW vs firewalld**
- UFW(Debian)は`ufw allow <port>`のようなシンプルなコマンドでルールを追加できる、iptablesのフロントエンド。
- firewalld(Rocky)はゾーン(zone)という概念でネットワークの信頼度ごとにルールをまとめて管理する、より柔軟だがやや複雑な仕組み。

**VirtualBox vs UTM**
- VirtualBoxはOracle製でWindows/Mac/Linuxに対応するクロスプラットフォームの仮想化ソフト。Intel/AMD系CPUでの実績が長い。
- UTMは主にApple Silicon(M1/M2など)向けの仮想化ソフトで、QEMUをベースにしている。VirtualBoxがApple Siliconに正式対応していない場合の代替として使われる。

今回はホストマシンがIntel系のUbuntuだったため、VirtualBoxを使用した。

## Tips / Troubleshooting(補足)

作業中に発生した、再現しやすい2つのトラブルとその対処法をまとめます。

### cronの`@reboot`が発火したか確認する方法

`@reboot`はログイン前の早いタイミングで実行されるため、`wall`の表示を見逃しやすい。cron自体のログで確認する:

```bash
sudo journalctl -u cron -b --no-pager | grep monitoring.sh
```

起動直後の実行ログが1件あれば`@reboot`は成功。その後10分おきに増えていれば`*/10`の周期実行も正常。

## Resources(参考資料)

- Born2beRoot 課題文: [原文PDF](B2B.pdf) / [日本語訳](B2B_ja.md)
- [Debian公式ドキュメント](https://www.debian.org/doc/)
- [Debian Handbook](https://debian-handbook.info/)
- `man crontab(5)`, `man sudoers(5)`, `man sshd_config(5)`, `man pam_pwquality(8)`
- 用語集: `GLOSSARY.md`

### AIの利用について

本プロジェクトの構築作業(パーティショニング、パスワードポリシー、sudo設定、SSH、UFW、`monitoring.sh`)はすべて自分の手でVM内のコマンドを実行して行った。Claude(Claude Code)は以下の用途で利用した:

- 課題文(英語)の日本語訳・専門用語の解説(`GLOSSARY.md`)
- 各設定の「なぜそうするのか」という背景の説明・質問への回答
- 作業内容を教科書形式のノートとして整理する手伝い(`STUDY_01`〜`04`, `PROGRESS.md`)
- 本`README.md`の構成

コマンドの実行結果やエラーの解釈はAIに聞きながら進めたが、実際の設定変更・コマンド入力・動作確認はすべて自分で行った。
