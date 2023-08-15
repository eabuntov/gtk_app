import asyncio
import aiohttp
import csv

from config import APIS, CSV_PATH


async def fetch_data(urls: tuple) -> list:
    tasks = [asyncio.create_task(fetch_api(url)) for url in urls]
    return [await task for task in tasks]


async def fetch_api(url: str) -> list:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json(content_type='text/html')


class MainModel:

    def __init__(self, urls: tuple = APIS,
                 path: str = CSV_PATH):
        self.urls = urls
        self.path = path

    def fetch_apis(self) -> list:
        return asyncio.run(fetch_data(self.urls))

    def csv_reader(self) -> str:
        with open(self.path, encoding="utf8") as f:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for row in reader:
                yield f"{row[1]} {row[3]}"
