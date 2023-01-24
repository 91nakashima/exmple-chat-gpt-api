

"""
AttributeError: module 'whisper' has no attribute 'load_model'

pip uninstall whisper
pip install git+https://github.com/openai/whisper.git
"""

import whisper
model = whisper.load_model("base")
result = model.transcribe("/assetes/20230106.m4a")
print(result["text"])
