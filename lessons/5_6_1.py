import asyncio


async def sensor_data(sensor_name):
    data = all_data_dict[sensor_name]
    return await asyncio.sleep(data['time'], result=f"{sensor_name}_data: {"".join(data['data'])}")


async def main():
    tasks = [asyncio.create_task(sensor_data(sensor)) for sensor in sorted(all_data_dict.keys())]
    result = await asyncio.gather(*tasks)
    if isinstance(result, list):
        result.insert(0, f"Результаты проведения теста типа {test_type}:")
    return result


asyncio.run(main())
