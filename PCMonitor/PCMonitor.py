
import psutil
from pypresence import Presence
import time
import os

pcmonitor_id = os.getenv('discord_client_id')

client_id = '841705865303162910'
RPC = Presence(client_id,pipe=0)  
RPC.connect() 

print("PCMonitor has been enabled!")



while True: 
    cpu_per = round(psutil.cpu_percent(),1) 
    
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%")  
    time.sleep(5) 