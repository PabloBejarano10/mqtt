from paho.mqtt.client import Client

"""
Para comprobar que puedo tanto recibir como enviar mensajes, 
este script lo que hará es recibir un mensaje que he mandado 
con el programa 1_publish.py que se encuentra en los apuntes
y lo estará enviando y recibiendo continuamente. 

Ademas, para que podamos desuscribirnos del topic y asi cortar
el bucle infito que se crea, he añadido una i fque si el mensaje 
recibido es 'adios' se desuscribirá del topic. 
"""

def on_message(client, userdata, msg):
    print("MESSAGE:", msg.topic, msg.payload)
    client.publish('clients/pablo', msg.payload)
    if msg.payload == b'adios':
        print ('unsubscribe', msg.topic)
        client.unsubscribe(msg.topic)


def main(broker, topic):
    
    client = Client()

    client.on_message = on_message

    print(f'Connecting on channels {topic} on {broker}')

    client.connect(broker)
    client.subscribe(topic)
    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
        sys.exit(1)
    broker = sys.argv[1]
    topic = sys.argv[2]
    main(broker, topic)
