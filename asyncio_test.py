import time
from datetime import datetime
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print('Tugas {}: Menghitung factorial({})'.format(name, i))
        await tidur()
        f *= i

    print('Tugas {}: factorial({}) adalah {}\n'.format(name, number, f))


async def tidur():
    print('TIDUR {}\n'.format(datetime.now()))
    await asyncio.sleep(1)


start = time.time()
loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(factorial("A", 10)),
    asyncio.ensure_future(factorial("B", 4)),
    asyncio.ensure_future(factorial("C", 3)),
    asyncio.ensure_future(factorial("D", 2)),
    asyncio.ensure_future(factorial("E", -2)),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


end = time.time()
print("Total time: {}".format(end - start))
