# Il numero di studenti che si iscrivono al secondo appello di Elementi di Probabilità è una variabile aleatoria di media 25 e deviazione standard 5

import distribuzioni.distribuzione_normale as dn

# L'aula A del plesso di matematica e informatica, ha 84 posti, ma all'esame se ne usano uno in quattro, 
# perciò sono sufficienti per accogliere fino a 21 studenti e non di più. 
# Determinare la probabilità che l'aula A non sia sufficiente per gli studenti iscritti.
mu = 25
sigma = 5
n = 21

probabilita = dn.prob_inferiore_a_soglia(mu, sigma, n)
print(f"La probabilità che l'aula A non sia sufficiente è {probabilita:.4f}")


# Si aggiungono alle iscrizioni anche un numero casuale di studenti di Istituzioni di Probabilità (media 1 e deviazione standard 1).
# Qual è la capacità minima di un'aula per cui vi sia il 90% o più di probabilità che essa sia sufficiente (sempre usando un posto su quattro)?
mu = dn.somma_deviazione_standard(mu, 1)
sigma = dn.somma_deviazione_standard(sigma, 1)
alpha = 0.90

calcola_dimensione_campione = dn.calcola_dimensione_campione(mu, sigma, alpha)
print(f"La capacità minima di un'aula per cui vi sia il 90% o più di probabilità che essa sia sufficiente è {calcola_dimensione_campione:.4f}")


# Ogni iscritto ha però una probabilità del 15% di non presentarsi all'appello. 
# Rispondere nuovamente al secondo punto con questa informazione aggiuntiva 
# (Servirà scegliere un modello sensato per le variabili aleatorio coinvolte.)

import distribuzioni.distribuzione_binomiale as db

p = 0.85
mu_presenti = db.media(n, p)
sigma_presenti = db.deviazione_standard(n, p)
print(f"La media e la deviazione standard del numero di studenti presenti sono {mu_presenti} e {sigma_presenti} rispettivamente.")

calcola_dimensione_campione = dn.calcola_dimensione_campione(mu_presenti, sigma_presenti, alpha)
print(f"La capacità minima di un'aula per cui vi sia il 90% o più di probabilità che essa sia sufficiente è {calcola_dimensione_campione:.4f}")