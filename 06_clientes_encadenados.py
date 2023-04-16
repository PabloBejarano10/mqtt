from paho.mqtt.client import Client
import sys

"""
Para este ejercicio he decidido que si el numero recibido en clients/pablo es primo se imprime por pantalla la tamperatura leida
del topic temperature/t1 esperando sleep(10). Una vez pasado este tiempo en el canal aparece b'stop' y se desuscribe del 
canal temperature/t1 
"""

def es_primo(numero):
    """
    Recibe un entero y devuelve un booleano diciendo si es primo o no 
    """
    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
        
    return True

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    try:
        if msg.payload == b'stop':
            client.unsubscribe('temperature/t1')

        if msg.topic == 'clients/pablo':
            n = int(msg.payload)

            if es_primo(n):
                client.publish('clients/temporizador', '10,clients/pablo,stop')
                client.subscribe('temperature/t1')
        
        if msg.topic == 'temperature/t1':
            t = int(msg.payload)
            print(f"La temperatra actual es de {t}")


    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    client = Client()
    client.on_message = on_message

    print(f'Connecting on channels clients/pablo on {broker}')
    client.connect(broker)

    client.subscribe('clients/pablo')

    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)