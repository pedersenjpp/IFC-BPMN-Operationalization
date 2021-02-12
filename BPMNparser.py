from bs4 import BeautifulSoup

XMLfile = open("Example-process.bpmn","r")
XMLcontent = XMLfile.read()

soup = BeautifulSoup(XMLcontent,'html.parser')
tasks = soup.find_all("task")
startevents = soup.find_all("startevent")
endevents = soup.find_all("endevent")
exclusivegateways = soup.find_all("exclusivegateway")

""" To Change attributes of inputs. Use this line of command"""
# tasks[0].attrs['name'] = 'Box XML'

"""Use this line of command to parse the xml name, and do something dependant on it"""
T = S = E = G = 0
for task in tasks: 
    T +=1
    if task.attrs['name'].startswith("T2") is True:
        OldTask = task.attrs['name']
        NewTask = task.attrs['name'] = "T3 - New Task"

for startevent in startevents: 
    S +=1

for endevent in endevents:
    E +=1

for exclusivegateway in exclusivegateways:
    G +=1

log = "\n{} has ben changed to {}".format(OldTask, NewTask)

print("Number of tasks: {:d} \nNumber of startevent: {:d} \nNumber of endevent: {:d} \nNumber of gateways: {:d}".format(T,S,E,G))
print(log)