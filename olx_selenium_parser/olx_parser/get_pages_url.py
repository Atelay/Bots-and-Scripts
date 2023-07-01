import asyncio
import os

import aiohttp
from bs4 import BeautifulSoup as bs

from olx_parser.config import DIR_NAME, COOKIES, HEADERS, URLS_FILE_PATH


class OLXPageParser:
    def __init__(self, cookies: dict = COOKIES, headers: dict = HEADERS):
        self.session = aiohttp.ClientSession(cookies=cookies, headers=headers)

    async def get_last_page(self, url: str) -> int:
        async with self.session.get(url=url, ssl=False) as response:
            soup = bs(await response.text(), "lxml")
            pagination_items = [
                i.get("aria-label")
                for i in soup.find_all("li", {"class": "pagination-item"})
            ]
            if not pagination_items:
                return 1
            last_page = pagination_items[-1].split()[-1]
        return int(last_page)

    async def get_page_urls(self, url: str, page: int):
        page_url = f"{url}/?page={page}"
        async with self.session.get(page_url, ssl=False) as response:
            soup = bs(await response.text(), "lxml")
            minicards = soup.find_all("div", class_="css-1sw7q4x")
            all_minicard: bs = (
                f"https://www.olx.ua/{i.find('a').get('href')}" for i in minicards[:-1]
            )
        return all_minicard

    async def get_all_page_urls(self, url):
        last_page = await self.get_last_page(url)
        fetch_page_tasks = (
            self.get_page_urls(url, i) for i in range(1, int(last_page) + 1)
        )
        page_results = await asyncio.gather(*fetch_page_tasks)
        articles_urls_list = {url for sublist in page_results for url in sublist}
        await self.session.close()
        return set(articles_urls_list)


class URLSaver:
    def __init__(self, dir_name=DIR_NAME):
        self.dir_name = dir_name

    def save_urls_to_file(self, urls_list):
        os.makedirs(self.dir_name, exist_ok=True)
        with open(URLS_FILE_PATH, "w", encoding="UTF-8") as file:
            [file.write(f"{url}\n") for url in urls_list]
