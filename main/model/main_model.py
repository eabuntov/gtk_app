import asyncio
import aiohttp

async def fetch_data(urls: list) -> list:
        tasks = [asyncio.create_task(fetch_api(url)) for url in urls]
        return [await task for task in tasks]
async def fetch_api(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            bstr = await response.content.read()
            return bstr.decode()

def fetch_apis() -> list:
    return asyncio.run(fetch_data(["https://paycon.su/api1.php",
                                    "https://paycon.su/api2.php"]))