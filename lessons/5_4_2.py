import asyncio

EVENTS = {
    ("Квест на поиск сокровищ", "Найди скрытые сокровища!"): 10,
    ("Побег от дракона", "Беги быстрее, дракон на хвосте!"): 5
}


async def countdown(name, seconds):
    for second in range(seconds, 0, -1):
        print(f"{name[0]}: Осталось {second} сек. {name[1]}")
        await asyncio.sleep(1)
    print(f"{name[0]}: Задание выполнено! Что дальше?")


async def main():
    tasks = [asyncio.create_task(countdown(name=name, seconds=seconds)) for name, seconds in EVENTS.items()]
    await asyncio.gather(*tasks)

asyncio.run(main())
