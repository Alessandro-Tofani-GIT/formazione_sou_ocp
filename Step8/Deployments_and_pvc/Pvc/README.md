# Gestione di PersistentVolumeClaim e ConfigMap nel Database

## Obiettivo

In questo modulo aggiuntivo dell'esercizio, si introduce:
- un **PersistentVolumeClaim** per la persistenza dei dati del database;
- una **ConfigMap** contenente uno script SQL per l'inizializzazione del database con una tabella `items` e alcuni dati di esempio.

---

## 1. PersistentVolumeClaim (PVC)

Il PVC viene utilizzato per garantire la **persistenza dei dati** del database, anche in caso di riavvio o ricreazione del pod.

---

## 2. ConfigMap con script di inizializzazione

La ConfigMap `db-init-script` contiene uno script SQL che crea una tabella e inserisce alcuni valori iniziali.


## Conclusione

In questa maniera si ha una configurazione persistente di dati sul database, con un'inizializzazione automatica dei dati grazie alla ConfigMap.
