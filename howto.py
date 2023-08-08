#!/usr/bin/env python
import openai
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# get openai key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# exit if no key
if not OPENAI_API_KEY:
    print("Please set OPENAI_API_KEY environment variable.")
    sys.exit(1)

# exit if no args
if len(sys.argv) < 3:
    print("Usage: python howto.py <system> <arg>")
    sys.exit(1)

system = sys.argv[1]
arg = ' '.join(sys.argv[2:])

print(f"system: {system}, message: {arg}")

r = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # model="gpt-4",
    messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
        {"role": "user", "content": f"Answer with only the actual code without any intro or explanation. What is the {system} code to {arg}, create all necessary files with as implemataion as possible?"},
    ]
)

text = r["choices"][0]["message"]["content"]
if text.startswith('`') and text.endswith('`'):
    text = text[1:-1]

print(text)
