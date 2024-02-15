# Su un campione di 50 intervistati, 19 preferirebbero una donna al Quierinale, 9 preferirebbero un uomo e 22 non hanno preferenze. 
# Siano p_{d}*e*p_{u} rispettivamente le frazioni di persone nella popolazione che risponderebbero di preferire una donna e un uomo.

import distribuzioni.distribuzione_binomiale as db

# Si verifichi se vi sia evidenza statistica che pa sia minore del 50%. In particolare sifornisca il p-value di questo test.
n = 50  
preferiscono_donna = 19
preferiscono_uomo = 9

p_hat = preferiscono_donna / n

p_value = db.calcola_p_value(p_hat=p_hat, p_0=0.5, n=n)
print(f"p-value: {p_value:.4f}")

print(db.discussione_valore_p(p_value, alpha=0.05))

# Si verifichi se vi sia evidenza statisticache p_{d} sia maggiore di p_{u}
p_d = preferiscono_donna / n
p_u = preferiscono_uomo / n

p_value = db.confronta_proporzioni(p_hat_1=p_d, p_hat_2=p_u, n_casi_1=preferiscono_donna, n_casi_2=preferiscono_uomo, n_interviste=n)
print(f"p-value: {p_value:.4f}")

print(db.discussione_valore_p(p_value, alpha=0.05))