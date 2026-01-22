from openai import OpenAI
import os

def analyze_error(error_log):
    prompt = f"""
You are a senior software engineer.

Analyze this log error and explain:
1. Root cause
2. How to fix it
3. Best practices to avoid it

ERROR LOG:
{error_log}
"""

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.output_text
