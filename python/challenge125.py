import time
clocks = ["time","perf_counter","monotonic","process_time"]

for function in clocks:
    print("Information on " + function + " clock:")
    print(time.get_clock_info(function))
    print()