# Frontend Flask 

## Descrizione

Questa è l'applicazione **frontend** del sistema a microservizi.  
È sviluppata in **Flask** e si occupa di interrogare il servizio **backend** via HTTP per visualizzare i dati provenienti da un database PostgreSQL, all'interno di una tabella HTML.

Fa parte di un sistema distribuito su Kubernetes composto da:
- Frontend (questo componente)
- Backend Flask
- Database PostgreSQL

---

## 1. Dockerfile

Il seguente `Dockerfile` crea l'immagine del frontend Flask che verrà successivamente implementato all'interno del Deployment frontend:

## 2. Script Python `frontend.py`

L'applicazione interroga l'endpoint /data del backend, riceve i dati in formato JSON e li visualizza in una tabella HTML.