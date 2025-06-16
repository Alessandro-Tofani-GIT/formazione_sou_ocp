# Deployment su Kubernetes

Questo progetto contiene i manifest Kubernetes per il deploy di un'applicazione che restituisce "**Welcome in Ocp_Support!**", con relativo Service di tipo LoadBalancer e un Ingress per esporre il servizio esternamente.

---

## Contenuto

- **Deployment**: crea 3 repliche di Pod con alessandrotofani/task4_test:50.0
- **Service**: espone i Pod tramite LoadBalancer sulla porta 80
- **Ingress**: instrada le richieste HTTP per il dominio `supporto.ocp.local` al Service
- **Ingress Controller**: gestisce le richieste HTTP/HTTPS in ingresso e applica le regole definite negli Ingress  

---

## 1. Deployment

Il Deployment crea 3 repliche di Pod con l’immagine `alessandrotofani/task4_test:50.0` e assegna le seguenti label:

- `app: web`
- `region: EU`
- `environment: dev`

## 2. Service (LoadBalancer)

Il Service di tipo LoadBalancer espone i Pod all’esterno del cluster sulla porta 80, selezionando i Pod con le label:

- `app: web`
- `environment: dev`

## 3. Ingress

L’Ingress espone il servizio HTTP esterno tramite il dominio **supporto.ocp.local** e instrada tutte le richieste verso il Service **nginx-service**.

---

## Verifiche

- Verifica i Pod creati:

```bash
kubectl get pods -l app=web,region=EU,environment=dev
```

- Controlla lo stato del Service:

```bash
kubectl get svc nginx-service
```

- Controlla lo stato dell’Ingress:

```bash
kubectl get ingress ingress-nginx
```

---

## Requisiti

Per eseguire correttamente i manifest e far funzionare il deployment, il service e l’ingress, assicurati di avere:

- Un cluster Kubernetes funzionante (minimo versione 1.19+ consigliata).
- `kubectl` configurato e connesso al cluster.
- Un **Ingress Controller** installato e attivo nel cluster, ad esempio (`nginx-ingress-controller`)
- Modificare il file `/etc/hosts` per far puntare il dominio `supporto.ocp.local` all’IP dell’Ingress Controller.

## Configurazione dell'host locale

Per poter accedere al servizio tramite il nome di dominio `supporto.ocp.local`, è necessario aggiungere una voce nel file `/etc/hosts` del tuo computer locale.
Apri il file `/etc/hosts` con privilegi di amministratore:

```bash
sudo nano /etc/hosts
```

Aggiungi la seguente riga alla fine del file:

```bash
127.0.0.1 supporto.ocp.local
```



---

## Conclusioni

Questa configurazione Kubernetes consente di esporre un’applicazione Nginx in modo scalabile e sicuro:

- Il **Deployment** garantisce alta disponibilità creando più repliche di Pod.
- Il **Service LoadBalancer** espone il traffico esterno verso i Pod in modo bilanciato.
- L’**Ingress** permette di gestire il traffico HTTP/HTTPS in ingresso, facilitando il routing basato su hostname e path.

La corretta installazione e configurazione dell’Ingress Controller e del DNS sono fondamentali per il corretto funzionamento dell’Ingress.





