import time
# print(time.gmtime(0)) #epoch

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1],time_here.tm_mon)
# print("Day:",time_here[2],time_here.tm_mday)

from time import monotonic as my_timer
import random

input("Press enter to start")
letters="abcdefghijklmnopqrstuvwxyz"

wait_time = random.randint(1, 5)
time.sleep(wait_time)
start_time = my_timer()
key=random.choice(letters)
keypressed=input("Press enter {} to stop".format(key))
while (keypressed!=key):
    keypressed=input("Please try again")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))