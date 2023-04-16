from paho.mqtt.client import Client
import sys

"""
1.- La primera tarea que he realizado es que compruebe que
    es entero o real y una vez hecho esto lo publique en 
    numbers/real o numbers/entero

2.- La segunda tarea consiste en ver si es primo o no y 
    en caso de serlo se publicará en numbers/prime

"""

def es_real(numero):
    """
    Como los mensajes se transmiten como listas de bytes basta
    comprobar que el byte del punto (b'.') aparece o no en la 
    lista de bytes para distinguir los reales de los enteros
    """
    return b'.' in numero

def es_primo(numero):
    """
    Recibe un entero y devuelve un booleano diciendo si es primo o
    no 
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
        if  es_real(msg.payload):
            client.publish('clients/numbers/real', msg.payload)
        else:
            client.publish('clients/numbers/entero', msg.payload)
        
        if es_primo(int(msg.payload)):
            client.publish('clients/numbers/prime', msg.payload)

    except ValueError:
        pass

    except Exception as e:
        raise e

def main(broker):
    userdata = {'suma' : 0}
    client = Client(userdata = userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)

    client.subscribe('numbers')

    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)