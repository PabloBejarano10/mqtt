from paho.mqtt.client import Client
import sys
from time import sleep

def descifrar_mensaje(mensaje):
    lista = mensaje.split(',')
    lista[0] = int(lista[0])    
    return lista

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    try:
        lista = descifrar_mensaje(str(msg.payload)[2:-1])
        sleep(lista[0])
        client.publish(lista[1], lista[2])
        print(f"PUBLICADO en {lista[1]}")
    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    client = Client()
    client.on_message = on_message

    print(f'Connecting on channels clients/temporizador on {broker}')
    client.connect(broker)

    client.subscribe('clients/temporizador')

    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
