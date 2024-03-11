import asyncio


async def check_access(data):
    await asyncio.sleep(data["Уровень секретности"])
    if data["Срок доступа"]:
        return f'Участник {data["Имя"]} {data["Фамилия"]} имеет действующий доступ. '\
               f'Продолжительность доступа: {data["Срок доступа"]}'
    else:
        raise ValueError(
            f'Ошибка доступа: У участника {data["Имя"]} {data["Фамилия"]} срок доступа истек или не указан.')


async def main():
    tasks = [
        asyncio.create_task(check_access(participant), name=f'{participant["Имя"]} {participant["Фамилия"]}')
        for participant in data
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

    for task in done:
        if task.exception() is not None:
            print(task.exception())
        else:
            print(task.result())

    if pending:
        for task in pending:
            print(f'Доступ участника {task.get_name()} отменен из-за критической ошибки.')
            task.cancel()


asyncio.run(main())
