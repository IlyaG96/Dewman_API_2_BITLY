from click_counter import *
from dotenv import load_dotenv
from argparse import ArgumentParser
import os


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    headers = {"Authorization": f"Bearer {TOKEN}"}
    parser = ArgumentParser(description='Enter URL')
    parser.add_argument('url', help="Enter URL")
    url = parser.parse_args().url
    print(run_script(url, headers))
