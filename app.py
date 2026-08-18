from ollama import chat
import subprocess
import argparse
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


if 1 >= len(sys.argv[1:]) >= 3:
    print("usage: python app.py prompt input [output]")
    print("!!! You can also specify the input and output paths in the prompt. !!!")
    sys.exit(1)


def main():
    FFMPEG_COMMAND_ERRORS = [
        "Unrecognized option",
        "Option not found",
        "Missing argument",
        "Invalid argument",
        "Invalid value",
        "Error parsing options",
        "Unable to find a suitable output format",
        "Unknown encoder",
        "Unknown decoder",
        "Unknown filter",
        "No such filter",
        "Stream specifier",
        "matches no streams",
        "Could not find codec parameters",
        "Codec not currently supported in container",
        "Error initializing output stream",
        "Invalid duration specification",
        "Invalid time duration",
    ]
    while True:
        try:

            response = chat(
                model=OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"config: {prompt}\n\ninput_file: {input_path}\n\noutput_file: {output_path}",
                    },
                ],
            )

            ffmpeg_config = response.message.content
            print(f"command: {ffmpeg_config}")

            if ffmpeg_config == "False":
                print("Wrong input")
                return

            #ffmpeg_config = split(ffmpeg_config)

            print(subprocess.run(ffmpeg_config, check=True, capture_output=True, text=True))
            print("DONE")
            return

        except subprocess.CalledProcessError as error:
            print(error)
            if any(e in error.stderr for e in FFMPEG_COMMAND_ERRORS):
                #print("Invalid FFmpeg command. Generating again...")
                
                continue

            print("Invalid FFmpeg command. Generating again...")


if __name__ == "__main__":
    with open("SYSTEM_PROMPT.txt", "r", encoding="utf-8") as file:
        SYSTEM_PROMPT = file.read()

    main()
