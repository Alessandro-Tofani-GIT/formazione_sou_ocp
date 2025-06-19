#  Esercizio Kubernetes: Architettura a 3 Livelli con Network Policies

##  Obiettivo

L'obiettivo di questo esercizio è distribuire tre applicazioni su un cluster Kubernetes (frontend, backend e database), configurando **Network Policy** per garantire un accesso controllato e sicuro tra i componenti.

---

##  Componenti dell'Applicazione

### 1.  Frontend

- **Tipo:** Web App (es. Flask)
- **Ruolo:** Interfaccia utente
- **Esposizione:** Rende il servizio disponibile all'esterno del cluster (LoadBalancer o NodePort)
- **Label:** `app=frontend`

### 2.  Backend

- **Tipo:** Servizio API (es. Flask)
- **Ruolo:** Logica di business, riceve richieste dal frontend
- **Esposizione:** Interna al cluster
- **Label:** `app=backend`

### 3.  Database

- **Tipo:** PostgreSQL o simile
- **Ruolo:** Gestione e conservazione dati
- **Esposizione:** Interna al cluster, nessuna comunicazione in uscita
- **Label:** `app=database`

---

##  Requisiti

- Cluster Kubernetes funzionante (es. Minikube, Kind, GKE, ecc.)
- `kubectl` configurato
- Le immagini Docker delle app disponibili (oppure creazione di app semplici con **Flask**)

---

##  Network Policy

###  Frontend

-  **Traffico in uscita**: consentito solo verso i pod `app=backend`
-  **Traffico in entrata**: negato, **eccetto** da fonti esterne (tipo LoadBalancer ingress)

###  Backend

-  **Traffico in uscita**: consentito solo verso i pod `app=database`
-  **Traffico in entrata**: consentito solo da pod `app=frontend`
-  **Altro traffico**: negato

###  Database

-  **Traffico in entrata**: negato
-  **Traffico in uscita**: negato

---

##  Assegnazione delle Label

Ogni `Deployment` deve avere la seguente label assegnata:

```yaml
metadata:
  labels:
    app: frontend  # oppure backend / database
```






