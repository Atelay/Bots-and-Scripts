from time import time
import asyncio

from olx_parser.get_pages_url import OLXPageParser, URLSaver
from olx_parser.olx_crawler import AdsDataExtractor, AdsURLsReader
from olx_parser.config import URLS_FILE_PATH, user_agents


async def main():

    # Getting URL
    url = input("Hello, please send me the link to your OLX search query.\n")
    parser = OLXPageParser()
    saver = URLSaver()
    urls_list = await parser.get_all_page_urls(url)
    saver.save_urls_to_file(urls_list)
    print("The list of URLs has been obtained. Starting to collect data.")

    # Start crawler
    urls = AdsURLsReader(URLS_FILE_PATH).read_urls()
    data = AdsDataExtractor(urls, user_agents)
    data.extract_data()


if __name__ == "__main__":
    x = time()
    asyncio.run(main())
    y = time()
    print(round(y - x, 2))
