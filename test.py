#python fundamentals
import math
server_name = "ser1"
cpu_cores = 4
memory_gb = 8.0
total_mem = 500
used_mem = 350
Uppername = server_name.upper()
mem_percentage_used = (used_mem / total_mem)*100
print(f"server name: {Uppername}, cpu cores: {cpu_cores}")
list_check = ['ansible', 'chef', 'd2c', '33']
print(list_check)
print(list_check[1:-1])
list_check.insert(1, "puppet")
list_check.pop(3)
for item in list_check:
    print(item)
#----------------------------------------------------
host_port = (80,8080) # tuple
print(f"host ports: {host_port[1]}")
servers = { "s1" , "s2" , "s3"}
servers2 = { "s3", "s4"} # sets
print(type(servers))
ports = { (80,8080), (5985,5986,22)} # set of tuples
print((80, 443) in ports) # checking if tuple is in the set
print(f"printing union of sets {ports.union(servers)}")
print(f"printing intersection of sets {servers.intersection(servers2)}")
