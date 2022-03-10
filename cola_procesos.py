# Librerías 
import simpy 
import random 
import statistics 
import itertools

# Variables 
Capacity = 1 
Instrucciones_Rand = [1,10]
memory = 100 
Process = 25 
Interval = 10 
totalTime = 0 
times = []
RANDOM_SEED = 8 
Inter = 10  
SIM_TIME=1000 
RAM_SIZE= 100
CPU_QUANTITY= 1

def proceso(name, env, RAM, CPU):
    instrucciones = random.randint(*Instrucciones_Rand)
    print('%s Proceso entrando en cola %.1f' % (name, env.now))
    with RAM.request() as req:
        start = env.now
      
        yield req

       
       

       
        yield env.timeout()

        print('%s finished refueling in %.1f seconds.' % (name,
                                                          env.now - start))


def ready_Proceso(env, RAM,CPU):

def running_Proceso(env, RAM, CPU):

def simulacion_cola():
    
    
def creacion_Proceso(env, RAM, CPU):
    for i in itertools.count():
        yield env.timeout(random.expovariate(1.0 / Inter))
        env.process(proceso('Proceso %d' % i, env, RAM, CPU))

# Comenzar simulación
print("Procesando en CPU")
random.seed(RANDOM_SEED)


#Crear environment
env = simpy.Environment()
RAM = simpy.Container(env, init=RAM_SIZE, capacity=RAM_SIZE) 
CPU = simpy.Resource(env,CPU_QUANTITY)
#RAM = RAM.get(memory) 
#RAM  =RAM.put(memory) 
env.process(simulacion_cola, CPU))
env.process(creacion_Proceso(env, RAM, CPU))

#correr simulación
env.run(until=SIM_TIME)