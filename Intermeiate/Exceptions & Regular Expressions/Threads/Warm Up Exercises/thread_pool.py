import concurrent.futures
import time


def process_task(task):
    print(f"Processing task {task}")
    time.sleep(1)
    print(f"Completed task {task}")


with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks = [1, 2, 3, 4, 5]

    # results = executor.map(process_task, tasks)

    # concurrent.futures.Future = print(executor.submit(process_task, 1))

    results = [executor.submit(process_task, task) for task in tasks]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    concurrent.futures.wait(results)
