
import os
from azure.ai.evaluation import AzureOpenAIModelConfiguration
from dotenv import load_dotenv
from azure.ai.evaluation import GroundednessEvaluator

load_dotenv()

model_config = AzureOpenAIModelConfiguration(
    azure_endpoint=os.environ["AZURE_ENDPOINT"],
    api_key=os.environ.get("AZURE_API_KEY"),
    azure_deployment=os.environ.get("AZURE_DEPLOYMENT_NAME"),
    api_version=os.environ.get("AZURE_API_VERSION"),
)

groundedness_eval_result = GroundednessEvaluator(model_config=model_config, threshold=3) 

try:
    groundedness_result = groundedness_eval_result(
        query=".NETは Linux で問題なく動きますか？", 
        context="""
        C#（正確には.NET）はクロスプラットフォームに正式に対応しているため、Linux上での稼働は「やろうと思えばできる」ものではなく、
        「Linux上で動かすのが当たり前」となっています。""",
        response="""
        「C#（.NET）が Linux でも動かせる」というのはそう。ただし、「やろうと思えばできる」と「Linux の上で動かすのが当たり前」では話が違う。
        """
    )
    result = f"""
    groundedness Evaluation Result:
    - groundedness Reason: {groundedness_result['groundedness_reason']}
    - groundedness Value: {groundedness_result['groundedness']}
    - groundedness Result: {groundedness_result['groundedness_result']}
    - groundedness Threshold: {groundedness_result['groundedness_threshold']}
    """
    print(result)

    groundedness_result = groundedness_eval_result(
        query=".NETは Linux で問題なく動きますか？", 
        context="""
        C#（正確には.NET）はクロスプラットフォームに正式に対応しているため、Linux上での稼働は「やろうと思えばできる」ものではなく、
        「Linux上で動かすのが当たり前」となっています。""",
        response="""
        C#(.NET)はLinux上で動作しません。
        """
    )
    result = f"""
    groundedness Evaluation Result:
    - groundedness Reason: {groundedness_result['groundedness_reason']}
    - groundedness Value: {groundedness_result['groundedness']}
    - groundedness Result: {groundedness_result['groundedness_result']}
    - groundedness Threshold: {groundedness_result['groundedness_threshold']}
    """
    print(result)
except Exception as e:
    print(f"Error during evaluation: {e}")
    exit(1)
