import asyncio


async def status_check(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        await asyncio.sleep(0.1)
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    names = ('CPU', 'Память', 'Дисковое пространство')
    tasks = [asyncio.create_task(status_check(status_list), name=name) for name in names]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
