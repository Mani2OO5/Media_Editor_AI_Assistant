from ollama import chat
import subprocess
import argparse
from shlex import split
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("prompt")
parser.add_argument("input", nargs="?", default=None)
parser.add_argument("output", nargs="?", default=None)

OLLAMA_MODEL = "llama3.2"
SYSTEM_PROMPT = None

args = parser.parse_args()
prompt = args.prompt
input_path = args.input
output_path = args.output


if not 1 >= len(sys.argv[1:]) >= 3:
    print("usage: python prog.py prompt input [output]")
    print("!!! You can also specify the input and output paths in the prompt. !!!")
    sys.exit(1)


def main():
    response = chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"config: {prompt}\n\ninput_path: {input_path}\n\noutput_path: {output_path}",
            },
        ],
    )

    ffmpeg_config = response.message.content
    print(f"command: {ffmpeg_config}")

    if ffmpeg_config == "False":
        print("Wrong input")

    ffmpeg_config = split(ffmpeg_config)
    subprocess.run(ffmpeg_config)


if __name__ == "__main__":
    with open("SYSTEM_PROMPT.txt", "r", encoding="utf-8") as file:
        SYSTEM_PROMPT = file.read()

    main()
