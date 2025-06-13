from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'consumer-group-1',
    'auto.offset.reset': 'earliest'  # legge anche i messaggi vecchi
}

consumer = Consumer(conf)

topic = 'foobar'
consumer.subscribe([topic])

print(f"In ascolto su topic '{topic}'...")

try:
    while True:
        msg = consumer.poll(1.0)  # timeout in secondi
        if msg is None:
            continue
        if msg.error():
            print(f' Errore: {msg.error()}')
        else:
            print(f' Ricevuto: {msg.key().decode()} => {msg.value().decode()}')
except KeyboardInterrupt:
    print("Interrotto da tastiera.")
finally:
    consumer.close()

