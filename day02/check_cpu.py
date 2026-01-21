
import psutil

# check cpu threshold
def check_cpu_threshold():
    user_cpu = int(input("Enter the CPU threshold: "))
    print(psutil.virtual_memory())
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > user_cpu:
       
        print("Current cpu usags: ",current_cpu)
        print("Hight cpu alert email sent")
    else: 
        print("Current cpu usags: ",current_cpu)
    print(user_cpu)

check_cpu_threshold()