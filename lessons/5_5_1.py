import asyncio


async def run_lap(name, speed):
    time_needed = round(100 / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):
    runners = {
        "Молния Марк": 12.8,
        "Ветренный Виктор": 13.5,
        "Скоростной Степан": 11.2,
        "Быстрая Белла": 0.8,
    }
    try:
        tasks = [
            asyncio.wait_for(
                asyncio.create_task(run_lap(name, speed)),
                max_time
            ) for name, speed in runners.items()
        ]
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError as exc:
        pass

if __name__ == '__main__':
    asyncio.run(main())
