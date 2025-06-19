# Kubernetes Private Docker Registry Authentication

## Descrizione

Questo progetto mostra come configurare un **Docker Registry privato** in Kubernetes con autenticazione, e come utilizzare un **Secret** di tipo `dockerconfigjson` per permettere ai Pod di effettuare il pull delle immagini private.

---

## 1. Configurazione Docker Registry

### `config.yml`

Configurazione JSON per autenticare l’accesso al registry:

```json
{
  "auths": {
    "my-registry.example:5000": {
      "username": "myuser",
      "password": "1234"
    }
  }
}
```

## 2. Manifest per Docker Registry

### `docker-registry.yml``

Configura un registry locale sulla porta 5000 con autenticazione basata su htpasswd.

```yaml
version: 0.1
log:
  fields:
    service: registry
storage:
  filesystem:
    rootdirectory: /var/lib/registry
http:
  addr: :5000
  headers:
    X-Content-Type-Options: [nosniff]
auth:
  htpasswd:
    realm: basic-realm
    path: /auth/htpasswd
```

## 3. Secret Kubernetes per autenticazione

### `dockerconfigjson.yml`

Il campo `.dockerconfigjson` contiene la configurazione codificata in base64 equivalente a `config.yml`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-registry-secret
  namespace: default   # Cambia il namespace se necessario
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: ewogICJhdXRocyI6IHsKICAgICJteS1yZWdpc3RyeS5leGFtcGxlOjUwMDAiOiB7CiAgICAgICJ1c2VybmFtZSI6ICJteXVzZXIiLAogICAgICAicGFzc3dvcmQiOiAiMTIzNCIsCiAgICB9CiAgfQp9Cg==
```


## 4. Pod test per pull immagine privata

### `podtest.yml`

Qui il pod usa il secret `my-registry-secret` per autenticarsi al tuo registry privato quando fa il pull dell’immagine.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pull-registry
spec:
  containers:
  - name: test-container
    image: localhost:5000/la-tua-immagine:tag
  imagePullSecrets:
  - name: my-registry-secret
```

---

## Verifica

Se l’autenticazione e il pull dell’immagine funzionano, il Pod sarà in stato Running. In caso di errore, nella descrizione del Pod troverai dettagli sul problema di pull.

```bash
kubectl get pods test-pull-registry
kubectl describe pod test-pull-registry
```

---


## Conclusione

Con questa configurazione puoi gestire immagini Docker private in Kubernetes usando un registry locale con autenticazione e un Secret dockerconfigjson per consentire ai Pod di scaricare le immagini in sicurezza.
