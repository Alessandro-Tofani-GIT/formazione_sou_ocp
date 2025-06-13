# Kafka Python Producer & Consumer

Questa repository contiene due semplici applicazioni Python per interagire con Apache Kafka:

- **producer_app.py**: crea un topic chiamato `foobar` e invia messaggi come producer.
- **consumer_app.py**: si iscrive al topic `foobar` come consumer e legge i messaggi.

---

## Prerequisiti

- Apache Kafka in esecuzione su `localhost:9092`
- Python 3.6+ installato
- Libreria Python `confluent-kafka`

---

## Installazione

1. Clona la repository o copia gli script Python.

2. Installa la libreria confluent-kafka:

---

## Come funziona

- Kafka crea automaticamente il topic foobar
- Il producer invia messaggi con chiave id-N e valore messaggio numero N
- Il consumer legge i messaggi dal topic foobar e stampa chiave e valore.


---

## Risorse utili

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Kafka Python Client](https://github.com/confluentinc/confluent-kafka-python)
- [Kafka Quickstart](https://kafka.apache.org/quickstart)



