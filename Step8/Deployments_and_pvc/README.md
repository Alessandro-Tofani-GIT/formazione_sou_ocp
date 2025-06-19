#  Kubernetes Application Deployment

##  Obiettivo

Questo progetto distribuisce un'architettura a tre livelli su Kubernetes, composta da:

-  **Frontend**: interfaccia utente accessibile dall'esterno
-  **Backend**: servizio applicativo che gestisce la logica
-  **Database**: PostgreSQL per la persistenza dei dati

Lo scopo è anche **configurare Network Policies** (non ancora incluse nel manifest) per limitare le comunicazioni secondo specifiche regole di sicurezza.

---

##  Descrizione del Manifest

Il manifest include definizioni di **Deployment** e **Service** per ciascuna delle tre componenti.

---

###  Frontend

- **Nome Deployment**: `frontend`
- **Immagine**: `frontend:34.1`
- **Comando**: `python /app/frontend.py`
- **Porta container**: `5000`
- **Variabile d'ambiente**:  
  `BACKEND_URL=http://backend-service:5001/data`
- **Replica**: 1

####  Service associato: `frontend`

- **Tipo**: `LoadBalancer`
- **Porta esterna**: `8080` → `5000` (container)
- **Accessibilità**: da internet tramite IP pubblico del LoadBalancer

---

###  Backend

- **Nome Deployment**: `backend-deployment`
- **Immagine**: `backend:25.1`
- **Comando**: `python /app/backend.py`
- **Porta container**: `5001`
- **Replica**: 1
- **Variabile d'ambiente**:
  ```env
  DATABASE_URL=postgresql://user:password@db-service:5432/mydb
  ```

####  Service associato: `backend-service`
- **Tipo**: `ClusterIP` (interno)
- **Porta esposta**: `5001`
- **Accessibilità**: `interna al cluster` 


---

### Database

- **Nome Deployment**: `db-deployment`
- **Immagine**: `postgres:15`
- **Porta container**: `5432`
- **Replica**: `1`
- **Variabili d'ambiente**:  
  ```env
  POSTGRES_USER=user
  POSTGRES_PASSWORD=password
  POSTGRES_DB=mydb
  ````
- **Persistenza dati**: `tramite PVC (db-pvc)`
- **Script di inizializzazione**:`montato da ConfigMap (db-init-script)`

#### Service associato: `db-service`
- **Tipo**: `ClusterIP`
- **Porta esposta**: `5432`
- **Accessibilità**: `solo all'interno del cluster (dal backend)`

