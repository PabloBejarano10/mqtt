from paho.mqtt.client import Client
import sys

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    try:
        t = int(msg.payload)
        if not userdata['conectado_a_humidity']:
            if t > userdata['K_0']:
                print(f'Cota K_0 alcanzada {t}, suscribiendo a humidity...')
                client.subscribe('humidity')
                userdata['conectado_a_humidity'] = True
        else:
            if msg.topic=='humidity':
                h = int(msg.payload)
                if h > userdata['K_1']:
                    print(f'Cota K_0 alcanzada {h}, cancelando suscripción a humidity...')
                    client.unsubscribe('humidity')
                    userdata['conectado_a_humidity'] = False
            elif msg.topic == 'temperature/t1':
                t = int(msg.payload)
                if t <= userdata['K_0']:
                    print(f'temperatura {t} por debajo de la cota K_0, cancelando suscripción a humidity...')
                    userdata['conectado_a_humidity'] = False
                    client.unsubscribe('humidity')

    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    userdata = {'K_0' : 15,
                'K_1' : 75,
                'conectado_a_humidity' : False}
    
    print(f"La cota para la temperatura es {userdata['K_0']} y para la humedad es {userdata['K_1']}")
    
    client = Client(userdata = userdata)
    client.on_message = on_message

    print(f'Connecting on channels temperature/t1 on {broker}')
    client.connect(broker)

    client.subscribe('temperature/t1')

    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
