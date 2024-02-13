# Un'azienda meccanica produce componenti che vende in confezioni da 100 pezzi. 
# Questi pezzi non vengono testati prima di essere confezionati, e si stima che la probabilità che un pezzo sia difettoso sia del 7% o meno. 
# L'azienda dichiara un livello minimo di qualità (LMQ) di 15, ovvero che ciascuna confezione non contiene più di 15 componenti difettosi.

import distribuzioni.distribuzione_binomiale as db

# Qual è la probabilità approssimata che una confezione contenga più di 15 difettosi?
n = 100
p = 0.07
lqm = 15

mu = db.media(n, p)
sigma = db.deviazione_standard(n, p)

print(f"valore di mu: {mu}")
print(f"valore di sigma: {sigma}")

probabilita_piu_di_k_successi = db.probabilita_piu_di_k_successi(mu=mu, sigma=sigma, k=lqm)
print(f"probabilità di avere più di 15 difettosi: {probabilita_piu_di_k_successi}")


# Quale LQM possiamo dichiarare, invece di 15, se accettiamo una probabilità del 10% che una confezione non rispetti tale limite?
alpha = 0.10
k = db.trova_k(mu, sigma, alpha)
print(f"valore di k: {k}")


# Stiamo trattando un grosso ordine di 100 confezioni (10000 pezzi) e vorremmo poter dichiarare che non più di una percentuale z dei componenti sono difettosi.
# Quanto basso possiamo prendere z se accettiamo una probabilità di sbagliarci del 10%?
n = 10000
p = 0.07
alpha = 0.10

limite_superiore = db.limite_superiore_confidenza(p, n, alpha)
print(f"limite superiore: {limite_superiore}")