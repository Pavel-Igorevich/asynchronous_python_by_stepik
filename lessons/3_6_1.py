import asyncio


async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    fut = asyncio.ensure_future(set_future_result('Успех', 2))
    print(f"Состояние Future до выполнения: {fut.done()}")
    print("Задача запущена, ожидаем завершения...")
    await fut
    if fut.done():
        print(f"Состояние Future после выполнения: {fut.done()}")
        return fut.result()


async def main():
    result = await create_and_use_future()
    print("Результат из Future:", result)

asyncio.run(main())
