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
#-----------------------------------------------------
dict1 = {
    "p1": "azure",
    "p2": "aws",
    "region": "uswest"
}
dict2 = { "region": "useast"}
print(dict1 | dict2) # union will ovewrite the value of region of dict1
dict1["p1"] = "gcp" # updating key value
dict2["cost_center"] = "33" # adding new key value to dict
print(f"dict1: {dict1} dict2: {dict2}")
for value in dict1.values():
    print(value)
#----------------------------------------------------------------------------
import socket
# str1 is position parameter and str2 is keyword output will be terraform and chef
def check_fun(host,port=22,timeout=5):
        print(f" host: {host}  port: {port}")
        try:
             with socket.create_connection((host,port), timeout):
              print("pass")
              return True
        except Exception as e:
             print(f"error: {e}")
             
check_fun("www.google.com")

# Range function
for server in range(5): # 0 to 4
     print(server)
for server1 in range(5,8): # 5 - 7
     print(server1)
for server2 in range(5,30,5): # 5 to 30 with space of 5 
     print(server2)

#----------------------------------------
servers = ["web1", "web2", "web3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
if servers[1] == "web2":
    print("condition met")
# to iterate over index and item 
for ind, server in enumerate(servers):
    print(f"index: {ind} item: {server}")
# to zip lists and iterate over it 
for server, ip in zip(servers, ips):
    print(f"server: {server} ip: {ip}")
#----------------------------------------------------------

def example_func(*args, **kwargs):
 print("Positional arguments:", args) # tuple
 print("Keyword arguments:", kwargs) # dict

example_func(1, 2, 3, name="Alice", age=25)

#Calling functions by *args **kwargs
try:
  def check_call(host, port, timeout=10 ):
    print(f"{host} {timeout} {port}")
  params = ["host1", "22", "5", "False"]
  check_call(*params[:2]) #will update first two values of the params only
except Exception as e:
  print(e)

def fun_call( name, service, version=1.0 ): 
  print(f"name: {name} service: {service} version: {version}")
extra_params = {"name": "h1", "service": "httpd","version": "1.2" }
fun_call(**extra_params) #unpacking of the keyword args

#---- lamda function -------

square = lambda x: x*x #lambda arguments: expression
print(square(3))
print((lambda x: x*x)(3))

#transforming data with map
numbers = [1,2,3,4]
sum = list(map(lambda x: x+2, numbers)) #map(function, iterable)
print(sum)

ports = [22,443,5046,5985]
priviledge_ports = list(filter(lambda port: port < 1024, ports)) # filter(function , iterable)
print(priviledge_ports)

#-------------------------------------------

#Iterators provide sequential access to elements and are memory-efficient.
#Iterators
#An iterator is an object that allows sequential traversal through elements of an iterable (like lists, tuples, or sets) without exposing the underlying structure. It uses the iter() and next() functions and follows lazy evaluation, meaning it computes values only when needed.
#Example:

# Creating an iterator
iter_list = iter(['Python', 'is', 'awesome'])
print(next(iter_list)) # Output: Python
print(next(iter_list)) # Output: is
print(next(iter_list)) # Output: awesome

# Creating a generator
def square_numbers(n):
for i in range(1, n + 1):
yield i * i

gen = square_numbers(3)

print(next(gen)) # Output: 1
print(next(gen)) # Output: 4
print(next(gen)) # Output: 9
#Generators simplify iterator creation and are ideal for large datasets.
#Iterators are implemented using classes, while generators use functions.
#erators use yield to produce values, whereas iterators use iter() and next().
#Decorators enhance or modify the behavior of functions dynamically.
