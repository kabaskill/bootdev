import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description='AI Agent')
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response= client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)
    text = response.text
    metadata = response.usage_metadata


    if metadata is not None:
        print("Prompt tokens: ", metadata.prompt_token_count)
        print("Response tokens: ", metadata.candidates_token_count)

    print(text)


if __name__ == "__main__":
    main()
