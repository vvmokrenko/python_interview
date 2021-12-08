import asyncio
import aiohttp

category_urls = ['http://127.0.0.1:8000/photo',
                 'http://127.0.0.1:8000/computery',
                 'http://127.0.0.1:8000/gadjety',
                 'http://127.0.0.1:8000/periferiya']


async def call_url(url):
    print(f'Загрузка страницы {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            pagedata = await response.text()
            print(f'Кол-во байт: {len(pagedata)} \n'
                  f' Содержимое: {pagedata}')
            return pagedata

pages = [call_url(url) for url in category_urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(pages))

