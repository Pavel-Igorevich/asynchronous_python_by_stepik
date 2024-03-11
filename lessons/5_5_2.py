import asyncio

max_cast_time = 3
spells = {
    "Огненный шар": 1,
    "Ледяная стрела": 2,
    "Ледяная стрела2": 3,
    "Щит молний": 4,
}
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student, spell, cast_time):
    try:
        await asyncio.wait_for(asyncio.shield(asyncio.sleep(cast_time)), timeout=max_cast_time + 0.1)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except asyncio.TimeoutError:
        await asyncio.sleep(cast_time - max_cast_time)
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student}"
              f" успешно завершает заклинание с помощью shield.")


async def main():
    tasks = []
    for student in students:
        for spell, cast_time in spells.items():
            tasks.append(
                asyncio.create_task(cast_spell(student, spell, cast_time))
            )
    await asyncio.gather(*tasks)


asyncio.run(main())
