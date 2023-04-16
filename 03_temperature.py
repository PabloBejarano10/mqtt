from paho.mqtt.client import Client
import sys
from time import sleep

def mean(lista):
    if len(lista) == 0:
        return None
    else:
        suma = sum(lista)
        media = suma / len(lista)
        return media

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    n = len('temperature/')

    try:
        sensor = msg.topic[n:]
        
        if sensor in userdata['temp']:
            userdata['temp'][sensor].append(int(msg.payload))
        else:
            userdata['temp'][sensor]=[int(msg.payload)]
        
    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    #inicializamos userdata['temp'] como un diccionario vacío
    userdata = {'temp' : {}}
    client = Client(userdata = userdata)
    client.on_message = on_message

    print(f'Connecting on channels of temperature on {broker}')
    client.connect(broker)
    client.subscribe('temperature/#')
    client.loop_start()

    while True:
        sleep(10)
        all_temps = []
        all_max_temp = []
        all_min_temp = []

        for key,temp in userdata['temp'].items():
            media = mean(temp)
            maximo = max(temp)
            all_max_temp.append(maximo)
            minimo = min(temp)
            all_min_temp.append(minimo)

            print(f'La temperatura media es {key}: {media},')
            print(f'la temperatura maxima es {key}: {maximo},')
            print(f'la temperatura minima es {key}: {minimo}')
            
            all_temps += temp          
            userdata['temp'][key]=[]

        media_total = mean(all_temps)
        maximo_total = max(all_max_temp)
        minimo_total = min(all_min_temp)

        print(f'La temperatura media es: {media_total},')
        print(f'la temperatura maxima es: {maximo_total},')
        print(f'la temperatura minima es: {minimo_total}')


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)