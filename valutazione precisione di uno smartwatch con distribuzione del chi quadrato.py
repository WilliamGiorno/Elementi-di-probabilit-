# Si vuole misurare la precisione con cui uno smartwatch rileva il passo di corsa 
# (il passo e la velocita espressa in secondi per chilometro). Viene svolto un esperimento in cui
# l’oggetto viene portato ad un passo assolutamente costante, per 10 intervalli di 1 km. 
# Per ciascun intervallo si rileva il passo medio misurato, trovando i dati seguenti (in secondi per km),
# 301 289 299 311 299 288 304 313 303 299
# Si ipotizza che i dati siano normali, con media µ e deviazione standard σ, e che quest’ultima misuri la precisione dello strumento.

import distribuzioni.distribuzione_chi_quadrato as dcq

# Si stimi σ con un intervallo di confidenza unilaterale sinistro (ovvero del tipo σ ≤ U) con il 95% di confidenza e anche con un intervallo di confidenza bilaterale al 95%.
campione = [301, 289, 299, 311, 299, 288, 304, 313, 303, 299]
alpha = 0.05
n = len(campione)
df = n - 1 

mu = dcq.media_campionaria(campione)
sigma = dcq.deviazione_standard_campionaria(campione)
print(f"Media campionaria: {mu} e deviazione standard campionaria: {sigma} s/km")

limite_inferiore_S = dcq.limite_inferiore_S(alpha, n, sigma)  # Usa la deviazione standard campionaria per calcolare il limite
print(f"Limite inferiore per la deviazione standard con confidenza del 95%: {limite_inferiore_S:.2f} s/km")

limite_inferiore_bilat, limite_superiore_bilat = dcq.limite_inferiore_e_superiore_bilaterale(alpha, n, sigma)
print(f"Intervallo bilaterale per la deviazione standard con confidenza del 95%: [{limite_inferiore_bilat:.2f}, {limite_superiore_bilat:.2f}] s/km")

# L’azienda produttrice sostiene che σ sia minore di 5 s/km. Si verifichi tramite il
# calcolo del p-value se ciò sia plausibile.
sigma_test = 5

p_value = dcq.test_chi_quadrato(campione, sigma_test)
print(f"P-value: {p_value:.4f}")

chi_quadrato = dcq.calcola_chi_quadrato(campione, sigma_test)

print(dcq.conferma_ipotesi(chi_quadrato, p_value, alpha, campione))

# Si determini la potenza del test precedente, nel caso σ sia pari a 10 s/km.
sigma_test = 10

potenza_test_chi_quadrato = dcq.potenza_test_chi_quadrato(campione, sigma_test)
print(f"Potenza del test: {potenza_test_chi_quadrato:.4f}")