# Gestione dei Kubernetes Secret

## Obiettivo

In questo documento vengono descritti tre tipi diversi di **Kubernetes Secret** utilizzati per:
- l’**autenticazione a un registry Docker privato** (`dockercfg`)
- la **gestione delle credenziali del database** (`Opaque`)
- la **configurazione di un Service Account con token** (`service-account-token`)

---

## 1. Secret Docker Config (`kubernetes.io/dockercfg`)

Utilizzato per autenticare il cluster Kubernetes a un registry Docker privato.

#### Utilizzo nel Pod

Può essere referenziato in un Pod per accedere a un'immagine privata:
  ```yaml
  imagePullSecrets:
  - name: secret-dockercfg
  ```
## 2. Secret Opaque: Credenziali Database

Questo Secret contiene username e password per il database, codificati in formato base64.

Per poter effettuare la decodifica di tali valori:

  ```bash
  echo YWRtaW4= | base64 -d    # admin
  echo UyFCXCpkJHpEc2I9 | base64 -d  # S!B\$*d\$Dsb=
  ```

## 3. Secret per Service Account (kubernetes.io/service-account-token)

Questo tipo di Secret viene generato automaticamente da Kubernetes per associare un token a un ServiceAccount.

#### Utilizzo

I Secret di tipo kubernetes.io/service-account-token vengono gestiti internamente dal sistema per fornire accesso sicuro alle API Kubernetes. Non è necessario montarli manualmente, ma possono essere visualizzati o utilizzati da strumenti esterni che necessitano autenticazione via token.

---

## Verifica

```bash
kubectl get secrets
```

---

## Conclusione

Questi Secret Kubernetes permettono di gestire in modo sicuro:
- credenziali di autenticazione
- accesso a registry Docker privat i
- token di ServiceAccount per accesso API