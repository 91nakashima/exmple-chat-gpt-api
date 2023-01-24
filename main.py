"""
ドキュメンテーション
https://beta.openai.com/docs/introduction

API リファレンス
https://beta.openai.com/docs/api-reference/introduction
"""


import openai
from key import OPENAI_KEY


"""
https://beta.openai.com/account/api-keys

ここからAPI keyを取得できます。
"""
openai.api_key = OPENAI_KEY


# res = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="何か言って",
#     max_tokens=100,
#     temperature=0
# )
# print(res)

# openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.

"""
res = openai.Completion.create(
    model="text-davinci-003",
    prompt="何か言って",
    max_tokens=100,
    temperature=0
)

print(res)

{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\u304f\u3060\u3055\u3044\n\n\u304a\u75b2\u308c\u69d8\u3067\u3059\uff01\u4eca\u65e5\u3082\u4e00\u65e5\u9811\u5f35\u308a\u307e\u3057\u3087\u3046\uff01"
    }
  ],
  "created": 1674526135,
  "id": "cmpl-6c31zSvfIJZkzahT8KzwvePPlhYqY",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 42,
    "prompt_tokens": 8,
    "total_tokens": 50
  }
}

ください

お疲れ様です！今日も一日頑張りましょう！
"""


"""
res = openai.Completion.create(
    model="text-davinci-003",
    prompt="何か言って",
    max_tokens=7,
    temperature=0
)

print(res)

{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": "\u304f\u3060\u3055\u3044\n\n" # ください
    }
  ],
  "created": 1674525576,
  "id": "cmpl-6c2syZJsxYvwsShbJldpuXh1n3auf",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 6,
    "prompt_tokens": 8,
    "total_tokens": 14
  }
}
"""


"""
res = openai.Completion.create(
    model="text-davinci-003",
    prompt="pythonとは",
    max_tokens=7,
    temperature=0
)

print(res)

{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": "\n\nPython\u306f\u3001\u30aa" # Pythonは、オ
    }
  ],
  "created": 1674525656,
  "id": "cmpl-6c2uG9iTD7tftqbnYjurTplfZXaqw",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 6,
    "prompt_tokens": 3,
    "total_tokens": 9
  }
}
"""
