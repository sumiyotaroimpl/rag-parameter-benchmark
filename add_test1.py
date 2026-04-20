import ollama
import time

# テスト対象のモデルリスト
MODELS=[
    "gemma2:9b",
    "llama3.1:8b",
    "qwen2.5:7b-instruct",
]

# AIが事前知識として「絶対に知っている」が、「ドキュメントには書かれていない」状態を作る
CONTEXT_TEXT = """
【日本の山に関する資料】
富士山は日本で最も高い山であり、静岡県と山梨県にまたがっています。
古くから霊峰として信仰の対象となっており、多くの登山客が訪れます。
"""

# テスト用のプロンプト
SYSTEM_PROMPT = "あなたは厳密なアシスタントです。必ず【ドキュメント】の内容のみに基づいて回答してください。"

# テストケース（ハルシネーションテストのためテスト３を使用）
TEST_QUERIE = "富士山の標高は何メートルですか？"
full_prompt = f"【ドキュメント】 \n{CONTEXT_TEXT}\n\n 【質問】 \n{TEST_QUERIE}"


def run_topp_test(model, p_val):
    print(f" [条件: Top_p = {p_val}]")
    # 可能性は残しつつ（temperature: 0.1）もランダム性は排除（seed: 42（固定））
    options = {
        'temperature': 0.8,
        'top_p': p_val,
    }
    
    start_time = time.time()
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': full_prompt},
            ],
            options=options,
        )
        answer = response['message']['content'].strip()
        elapsed_time = time.time() - start_time
        print(f"回答: {answer}")
        print(f"\n[処理時間: {elapsed_time:.2f}秒]")
    except Exception as e:
        print(f"エラー発生: {e}")

def run_add1_tests():
    print("=== 追加１：Top_pによるハルシネーション制限テスト ===\n")

    for model in MODELS:
        print(f"▼▼▼ 実行モデル: {model} ▼▼▼")
        # Top_pの値を変動させてテスト
        # 1.0(制限なし) -> 0.5（上位50%で打ち切り） -> 0.1（上位10%のみ）
        for p_val in [1.0, 0.5, 0.1]:
            run_topp_test(model, p_val)
        print("-" * 50)

if __name__ == "__main__":
    run_add1_tests()