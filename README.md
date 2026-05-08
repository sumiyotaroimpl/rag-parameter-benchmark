# Local LLM Fine-tuning

無料ローカルLLMを用いたRAG（検索拡張生成）と、生成パラメータ（Temperature, Seed等）が回答の精度・安定性に与える影響を検証するプロジェクトです。

## 関連資料
本リポジトリのコードは、以下の技術検証・実装プロセスに基づいています。詳細な環境構築手順やプロンプトの考察については、各記事をご参照ください。

- [【ローカルLLM】無料で使えるローカルLLM | RAG環境で一番「嘘をつかない」モデルはどれ？](https://ramble.impl.co.jp/12542/)
- [【ローカルLLM】無料で使えるローカルLLM | TemperatureとSeedでブレないRAGを構築](https://ramble.impl.co.jp/12579/)

## ファイル構成
検証のステップと役割ごとにスクリプトを分割しています。
- `test_faq.py`
  - 1つ目の記事で紹介されているスクリプトです。5つのモデルに対し、3つのテスト問題に回答させます。
- `test_phase1.py`
  - 2つ目の記事で紹介されているスクリプトです。3つのモデルに対して、1つの質問に3回回答させることで、Temperatureの設定による回答の揺らぎを観察します。
- `test_phase2.py`
  - top_pの調整による3モデルの回答の変化を観察します。
- `add_test1.py`
  - top_pの調整による3モデルの回答の変化を観察します。他のスクリプトとは異なり、テーマは労働基準法ではありません。また、プロンプトによる「記載がありません」の制御を取り払ったものとなっています。プロンプトによる制限とパラメータ制御の影響力の差を観察することができます。

## セットアップ
本リポジトリのコードを実行するには、Ollamaの環境構築と、Pythonの依存ライブラリのインストールが必要です。

### 1. Ollamaとモデルの準備（macOS環境の例）
```bash
# Ollamaのインストールと起動
brew install ollama
brew services start ollama

# Llama 3.1（8B）
ollama pull llama3.1:8b
# Qwen 2.5（7B-Instruct）
ollama pull qwen2.5:7b-instruct
# Gemma 2（9B）
ollama pull gemma2:9b
# Mistral-nemo（12B）
ollama pull mistral-nemo:12b
# Phi-3.5（3.8B）
ollama pull phi3.5:3.8b
```

### 2. 仮想環境の構築・アクティベート
仮想環境の利用を推奨します。
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Pythonパッケージのインストール
```bash
pip install -r requirements.txt
```

### 4. 実行
`python` コマンドで実行することが可能です。
```bash
python ***.py
```

## 主な使用ライブラリ
- ollama

## ⚠️注意
- 複数のモデルをダウンロードするため、容量にご注意ください。