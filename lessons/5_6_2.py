import asyncio


# Корутина для отправки запроса.
async def equipment_request(request):
    req_num = request.split(' ')[0]
    await asyncio.sleep(1)
    return f"{req_num} is Ok!"


# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [asyncio.create_task(equipment_request(request=data)) for data in equipment_list]
    await asyncio.gather(*tasks)
    print(f"На отправку {len(equipment_list)} запросов потребовалось {query_time()} секунд!")
