import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

base_url = 'https://arbuz.kz/ru/almaty/catalog/cat/225253-kulinariya#/'
Headers = {"User-Agent": UserAgent().random}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url,headers=Headers) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = bs(r, "html.parser")
            items = soup.find_all("article", {"class": 'product-item product-card'})
            f = open('data.txt', 'w')
            for item in items:
                title = item.find("a", {"class": "product-card__title"})
                link = title.get("href")
                price = item.find("b").text.strip()
                f.write(f"Название: {title.text.strip()}, https://arbuz.kz/{link}, {price}\n")
                print(f"Название: {title.text.strip()}, https://arbuz.kz/{link}, {price}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
