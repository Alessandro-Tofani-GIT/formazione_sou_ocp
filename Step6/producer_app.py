from confluent_kafka import Producer
import time

conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

topic = 'foobar'

def delivery_report(err, msg):
    if err:
        print(f' Errore nella consegna: {err}')
    else:
        print(f' Messaggio inviato: {msg.key()}: {msg.value()}')

print("Inizio invio messaggi su topic 'foobar'...")

try:
    for i in range(10):
        key = f'id-{i}'
        value = f'messaggio numero {i}'
        producer.produce(topic, key=key, value=value, callback=delivery_report)
        producer.poll(0)  # Richiede il polling per inviare
        time.sleep(1)
    producer.flush()
except KeyboardInterrupt:
    print("Interrotto da tastiera.")

