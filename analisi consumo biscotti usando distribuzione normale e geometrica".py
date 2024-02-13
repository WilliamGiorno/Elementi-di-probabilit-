# Un bambino fa colazione mangiando ogni giorno biscotti per un peso casuale, i dat con media 40 g e deviazione standard 10 g

import distribuzioni.distribuzione_normale as dn

# Determinare media e deviazione standard per il peso X dei biscotti consumati in un mese (30 giorni). 
# Determinare approssimativamente la probabilità che X sia inferiore a 1 Kg.
n = 30
mu = 40
sigma = 10
soglia_massima = 1000

mu_totale = dn.normalizzazione_media(mu, n)
sigma_totale = dn.normalizzazione_deviazione_standard(sigma, n)

print(f"Media totale: {mu_totale:.4f}, Deviazione standard totale: {sigma_totale:.4f}")

probabilita = dn.prob_inferiore_a_soglia(mu_totale, sigma_totale, soglia_massima)
print(f"Probabilità che il peso totale sia inferiore a 1 Kg: {probabilita:.4f}")

# Un singolo biscotto pesa 15 g. Il fratello del bambino mangia un primo biscotto con probabilità del 50%. 
# Se effettivamente lo mangia, ne mangia un secondo di nuovo con probabilità del 50%. 
# Fai poi lo stesso con il terzo, e così via. 
# Sia Z il peso dei biscotti mangiati complessivamente dai due fratelli in un mese. 
# Determinare a e b tali che P(a≤Z≤b)≈ 90%.

import distribuzioni.distribuzione_geometrica as dg

mu_2 = dg.calcola_media_per_quantita(15, 0.5)
sigma_2 = dg.calcola_deviazione_standard_per_quantita(15, 0.5)

mu_totale_2 = dn.normalizzazione_media(mu_2, n)
sigma_totale_2 = dn.normalizzazione_deviazione_standard(sigma_2, n)

print(f"Media: {mu_totale_2:.4f}, Deviazione standard: {sigma_totale_2:.4f}")

somma_media = dn.somma_media(mu_totale, mu_totale_2)
somma_deviazione_standard = dn.somma_deviazione_standard(sigma_totale, sigma_totale_2)

a, b = dn.intervallo_di_confidenza(somma_media, somma_deviazione_standard, 0.90)
print(f"Intervallo di confidenza: [{a:.4f}, {b:.4f}]")
