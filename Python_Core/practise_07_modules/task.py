import time

print(f"Starting the excution and going to sleep for 3 sec ...")
start_time = time.perf_counter()
time.sleep(3)
after_sleep_time = time.perf_counter()

print(f"The start time is {start_time} the execution takes {after_sleep_time - start_time}")
