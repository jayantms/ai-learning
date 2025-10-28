import asyncio 

async def fetch_data1(delay: int, routineNo: int): 
    print(f"Fetching data for routine {routineNo}...")
    await asyncio.sleep(delay) 
    print(f"Data fetched for routine {routineNo}...")
    return {"data": f"Sample data from routine {routineNo}"} 


### Started tasks in parallel and awaited sequentially
async def main1(): 
    print("Starting main coroutine...")
    task1 = asyncio.create_task(fetch_data1(1, 2))
    task2 = asyncio.create_task(fetch_data1(2, 3))
    task3 = asyncio.create_task(fetch_data1(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"Received results - {result1}, {result2}, {result3}")


## Started tasks 2, 3 in parallel, collected results and then started task 1. 
async def main2(): 
    print("Starting main coroutine...")
    task1 = asyncio.create_task(fetch_data1(1, 2))
    task2 = asyncio.create_task(fetch_data1(2, 3))

    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch_data1(3, 1))

    result3 = await task3

    print(f"Received results - {result1}, {result2}, {result3}")    


### Using asyncio.gather to run all tasks in parallel and collect results 
async def main3(): 
    print("Starting main coroutine...")

    results = await asyncio.gather(fetch_data1(1, 2), fetch_data1(2, 3), fetch_data1(3, 1)) 

    for result in results: 
        print(f"Received result - {result} ")

### 
async def main3(): 
    print("Starting main coroutine...")

    tasks = []

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data1(1, 2))
        task2 = tg.create_task(fetch_data1(2, 3))
        task3 = tg.create_task(fetch_data1(3, 1))
        tasks.extend([task1, task2, task3])

    results = [task.result() for task in tasks] 

    for result in results: 
        print(f"Received result - {result} ")


### 
async def main3(): 
    print("Starting main coroutine...")

    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data1(sleep_time, i))
            tasks.append(task)

    results = [task.result() for task in tasks] 

    for result in results: 
        print(f"Received result - {result} ")


asyncio.run(main3()) 



