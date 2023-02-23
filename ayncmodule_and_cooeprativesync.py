"""
# https://realpython.com/python-async-features/
# version 1
import queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")

def main():

    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [2, 1]:
        work_queue.put(work)

    # Create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

if __name__ == "__main__":
    main()
"""

"""
# version 2
import time
import queue
from codetiming import Timer

def task(name, queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not queue.empty():
        delay = queue.get()
        print(f"Task {name} running")
        timer.start()
        time.sleep(delay)
        timer.stop()
        yield

def main():

    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [2, 1]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    done = False
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        while not done:
            for t in tasks:
                try:
                    next(t)
                except StopIteration:
                    tasks.remove(t)
                if len(tasks) == 0:
                    done = True

if __name__ == "__main__":
    main()
"""

"""
# version 3
import asyncio
from codetiming import Timer
from datetime import datetime

async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not work_queue.empty():
        delay = await work_queue.get()
        print(f"Task {name} running")
        print("Today's date before sleep :", datetime.now())
        timer.start()
        await asyncio.sleep(delay)
        timer.stop()
        print("Today's date after sleep for {}: {}".format(name,datetime.now()))

async def main():

    # Create the queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for work in [150, 80]:
        await work_queue.put(work)

    # Run the tasks
    print("Today's date:", datetime.now())
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )

if __name__ == "__main__":
    asyncio.run(main())
"""

import asyncio
import aiohttp
from codetiming import Timer

async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()

async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        await work_queue.put(url)

    # Run the tasks
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue)),
        )

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # you need to set this else it will return RuntimeError: Event loop is closed
    asyncio.run(main())
