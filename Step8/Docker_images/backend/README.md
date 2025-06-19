# Backend Flask + PostgreSQL 

## Descrizione

Questo backend è un'applicazione Flask in esecuzione su un container Docker, che si connette a un database PostgreSQL per fornire un endpoint `/data` che restituisce un elenco di oggetti contenuti nella tabella `items`.

Fa parte di un sistema a microservizi su Kubernetes con:
- Un'applicazione **frontend**
- Un **backend Flask**
- Un **database PostgreSQL**

## 1. Dockerfile

Il seguente Dockerfile cea l'immagine utilizzata all'interno del Deployment backend.

## 2. Script Python `backend.py`

Il backend si connette al database PostgreSQL utilizzando una variabile d'ambiente DATABASE_URL e restituisce i dati dalla tabella items.


