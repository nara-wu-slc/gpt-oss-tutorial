# gpt-oss-tutorial
gpt-oss を研究室のマシンで使うためのチュートリアル

`/path/to/gpt-oss` に環境を作るとしたときの内容です。

# 環境作り

## 環境構築するディレクトリを作成して移動
```
mkdir -p /path/to/gpt-oss
cd /path/to/gpt-oss
```

## Pythonの環境作り
```
uv venv --python 3.12
source .venv/bin/activate
```

## gpt-oss, torch, transformersのインストール
```
uv pip install gpt-oss
uv pip install torch
uv pip install transformers
uv pip install accelerate
```

## サンプルプログラムの取得
```
curl -O https://raw.githubusercontent.com/nara-wu-slc/gpt-oss-tutorial/refs/heads/main/sample.py
```

# 実行

## 仮想環境の呼び出し
```
source /path/to/gpt-oss/.venv/bin/activate
```

## サンプルプログラムの実行
```
python3 /path/to/gpt-oss/sample.py
```
