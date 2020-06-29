#! /usr/bin/python3
from os import getlogin,getcwd
import psutil

class betikfetch():
    def __init__(self):
        __author__ = "raifpy"
        
        self.core = psutil.cpu_count()
        self.frequance = psutil.cpu_freq().current
        self.percent = psutil.cpu_percent()

        mem = psutil.virtual_memory()
        self.mem_total = mem.total
        self.mem_used = mem.used
        swap_mem = psutil.swap_memory()
        self.swap_total = swap_mem.total
        self.swap_used = swap_mem.used
        self.temp = psutil.sensors_temperatures()["acpitz"][0].current                      # Can Error
        self.fan = psutil.sensors_fans()[list(psutil.sensors_fans().keys())[0]][0].current  # Can Error
        self.battery = [psutil.sensors_battery().percent,"√"] if psutil.sensors_battery().power_plugged else [psutil.sensors_battery().percent,"χ"] # Can Error
        del swap_mem
        del mem
    
    @staticmethod
    def colorItButReverse(var , var_type ,medium,ladder,value):
        var = var_type(var)
        if var > medium:    
            return f"\033[32m{var}{value}\033[0m"
        elif var <= medium and var > medium-ladder:
            return f"\033[33m{var}{value}\033[0m"
        else:
            return f"\033[31m{var}{value}\033[0m"

    
    @staticmethod
    def colorIt(var , var_type ,medium,ladder,value):
        var = var_type(var)
        if var < medium:
            return f"\033[32m{var}{value}\033[0m"
        elif var >= medium and var < medium+ladder:
            return f"\033[33m{var}{value}\033[0m"
        else:
            return f"\033[31m{var}{value}\033[0m"


if __name__ == "__main__":
    info = betikfetch()
    cpuusage_value = info.colorIt(info.percent , float , 40.0 , 30,"%")
    cpucore_value = info.colorItButReverse(info.core,int,4,1,"")
    cpufreq_value = info.frequance
    mem_total_value_str = str(info.mem_total/1000000000)[:4]
    mem_used_value_str = str(info.mem_used/1000000000)[:4]
    mem_used_value = info.colorIt(mem_used_value_str,float,float(mem_total_value_str)/2,1,"G")
    mem_total_value = info.colorItButReverse(mem_total_value_str,float,4,1,"G")
    swap_total_value_str = str(info.swap_total/1000000000)[:4]
    swap_used_value_str = str(info.swap_used/1000000000)[:4]
    swap_total_value = info.colorIt(swap_total_value_str,float,0.1,99999,"G")
    swap_used_value = info.colorIt(swap_used_value_str,float,0.5,1,"G")
    temp_value_str = str(info.temp)
    temp_value = info.colorIt(temp_value_str,float,70,10,"℃")
    fan_value = info.colorIt(info.fan,int,5000,1000," RPM")
    login_value = f"\033[4m{getlogin()}\033[0m"
    battery_value = info.colorItButReverse(info.battery[0],int,15,15,"% "+info.battery[1])
    


    cpuusage =f"CPU Usage : {cpuusage_value}"
    cpucore = f"CPU CORE  : {cpucore_value}"
    cpufreq = f"CPU FREQ  : { int(info.frequance)/1000.0    }"
    mem = f"Mem Usage : {mem_used_value} / {mem_total_value}"
    swap =f"Swp Usage : {swap_used_value} / {swap_total_value}"
    login=f"Login : {login_value}"
    tempe=f"Temperatu : {temp_value}"
    fansp=f"Fan Sped  : {fan_value}"
    batte=f"Battery   : {battery_value}"
    location = f"Location  : \033[4m{getcwd()}\033[0m"
    #mount=f"Mountd Pr : {len(info.disk_partions)}"
    veri = f"""
    {cpuusage}\t\t{cpucore}\t\t{cpufreq}\n
    {tempe}\t\t{fansp}\t{batte}\n
    {mem}\t{swap}   {login}\n
    {location}

    """
    print(veri)
    
