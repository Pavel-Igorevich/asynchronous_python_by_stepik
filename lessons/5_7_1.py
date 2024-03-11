import asyncio


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [
        asyncio.create_task(
            simulate_processing(delay),
            name=process_name
        ) for process_name, delay in processors_delays.items()
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    if done:
        for task in done:
            print(f"Первый завершенный процесс: {task.get_name()}")
        for task in pending:
            task.cancel()


asyncio.run(main())
