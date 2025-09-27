import os
from azure.ai.evaluation import AzureOpenAIModelConfiguration
from dotenv import load_dotenv
from azure.ai.evaluation import CoherenceEvaluator

load_dotenv()

model_config = AzureOpenAIModelConfiguration(
    azure_endpoint=os.environ["AZURE_ENDPOINT"],
    api_key=os.environ.get("AZURE_API_KEY"),
    azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
    api_version=os.environ.get("AZURE_API_VERSION"),
)

# 
coherence_eval = CoherenceEvaluator(model_config=model_config, threshold=3)
coherence_eval_result = coherence_eval(
    query="""
地球温暖化の主な原因をいくつか説明してください。
""", 
    response="""
地球温暖化の主な原因は人間活動によるものです。
化石燃料を燃やすと二酸化炭素が出ます。
これは主要な温室効果ガスです。森林破壊も大きな問題です。
木は二酸化炭素を吸収しますが、伐採するとそれが減ります。
工業的な農作業からもメタンなどのガスが発生します。
これらがすべて地球の気温を上げています。
"""
)

result = f"""

Coherence Evaluation Result:
- Coherence Reason: {coherence_eval_result['coherence_reason']}
- GPT Coherence: {coherence_eval_result['gpt_coherence']}
- Coherence Value: {coherence_eval_result['coherence']}
- Coherence Result: {coherence_eval_result['coherence_result']}
- Coherence Threshold: {coherence_eval_result['coherence_threshold']}
"""

print(result)

print(
"""
ここから下は解説です。
CoherenceEvaluatorは、簡単に言うと「回答がどれだけ分かりやすく、筋道が通っているか」という一貫性を測るものです。

CoherenceEvaluatorが測定するもの
- 論理的・順序的な提示（アイデアの論理的かつ順序的なプレゼンテーション）:
- 思考のトレーニングの追跡（読者がライターの思考のトレーニングに簡単に従って理解できるようにします）:

- 一貫性の高い応答の特徴:
  - 質問に直接対処していること。
  - 文と段落の間に明確なつながりがあること。
    - 適切な遷移（トランジション）、つまり「しかしながら」「その一方で」「したがって」のような接続詞や表現がうまく使われていること。

""")
