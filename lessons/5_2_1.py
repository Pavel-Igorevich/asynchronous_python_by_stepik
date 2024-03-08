import asyncio


log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5}
]


async def fetch_log(event):
    if all(key in event for key in ['event', 'delay']):
        return f"Событие: '{event['event']}' обработано с задержкой {event['delay']} сек."
    else:
        raise TypeError("Incorrect event dictionary!")


async def main():
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    results = await asyncio.gather(*tasks)
    [print(f"{output_str}") for output_str in results]

if __name__ == '__main__':
    asyncio.run(main())
