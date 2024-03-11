import asyncio


async def coroutine_1():
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.1)
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.2)
    print("Третье сообщение от корутины 1")
    await asyncio.sleep(0.3)
    print("Четвертое сообщение от корутины 1")


async def coroutine_2():
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.11)
    print("Второе сообщение от корутины 2")
    await asyncio.sleep(0.21)
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.31)
    print("Четвертое сообщение от корутины 2")


async def coroutine_3():
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(0.111)
    print("Второе сообщение от корутины 3")
    await asyncio.sleep(0.211)
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(0.311)
    print("Четвертое сообщение от корутины 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())
