# Il consumo di acqua quotidiano di una famiglia è una variabile aleatoria di media e deviazione standard entrambe uguali a 0.75 m3

import distribuzioni.distribuzione_normale as dn

# Sia U il consumo complessivo in un periodo di 61 giorni (due mesi). 
# Determinare media e deviazione standard di U e la probabilità che U sia maggiore di 60 m3

mu = 0.75
sigma = 0.75
n = 61

mu_totale = dn.normalizzazione_media(mu, n)
sigma_totale = dn.normalizzazione_deviazione_standard(sigma, n)

print(f"Media totale: {mu_totale}, Deviazione standard totale: {sigma_totale}")

prob = dn.prob_inferiore_a_soglia(mu_totale, sigma_totale, 60)
print(f"Probabilità che il consumo complessivo sia maggiore di 60 m3: {1 - prob:.4f}")

# Sia V il consumo complessivo in un anno. Determinare a,b tali che P(a≤V≤b)≈80%

n = 365

mu_totale = dn.normalizzazione_media(mu, n)
sigma_totale = dn.normalizzazione_deviazione_standard(sigma, n)

print(f"Media totale: {mu_totale}, Deviazione standard totale: {sigma_totale}")

a, b = dn.intervallo_di_confidenza(mu_totale, sigma_totale, 0.80)
print(f"Intervallo di confidenza: [{a:.4f}, {b:.4f}]")

# Ripetere il punto precedente sostituendo V con W, il consumo complessivo di un periodo di una sola settimana, 
# assumendo questa volta che il consumo quotidiano abbia distribuzione esponenziale.

import distribuzioni.distribuzione_esponenziale as de

mu = de.caclolo_media_normalizzata(mu, 7)
sigma = de.calcolo_deviazione_standard_normalizzata(sigma, 7)

print(f"Media totale: {mu}, Deviazione standard totale: {sigma}")

a, b = de.intervallo_di_confidenza(mu, sigma, 0.80)
print(f"Intervallo di confidenza: [{a:.4f}, {b:.4f}]")




