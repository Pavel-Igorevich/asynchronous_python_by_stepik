import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине"
]


async def analyze_news(keyword, list_news, delay):
    for news in list_news:
        if keyword in news:
            print(f"Найдено соответствие для '{keyword}': {news}")
            await asyncio.sleep(delay)


async def main():
    keywords = ("COVID-19", "игр", "новый вид")
    tasks = [asyncio.create_task(analyze_news(keyword, news_list, 0.1)) for keyword in keywords]
    await asyncio.gather(*tasks)


asyncio.run(main())
