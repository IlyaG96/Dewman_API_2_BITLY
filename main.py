from click_counter import run_script
from dotenv import load_dotenv
from argparse import ArgumentParser
import os


if __name__ == '__main__':
    load_dotenv()
    BITLY_TOKEN = os.getenv("BITLY_TOKEN")
    headers = {"Authorization": f"Bearer {BITLY_TOKEN}"}
    parser = ArgumentParser(description='Enter URL')
    parser.add_argument('url', help="Enter URL")
    url = parser.parse_args().url
    print(run_script(url, headers))
