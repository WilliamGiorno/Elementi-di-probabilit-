# Un'azienda che produce tabacchi vuole tenere sotto controllo statistico la quantità di nicotina contenuta in ogni sigaretta. 
# In particolare è importante che la deviazione standard di questo indicatore non superi il livello di 0.3 mg

import distribuzioni.distribuzione_chi_quadrato as dcq

# È dato il seguente campione di 10 sigaret- te (riportante i mg di nicotina contenuti):
# 1.2 1.1 1.1 1.3 1.4 1.3 1.0 1.2 1.1 1.3
# Vi è evidenza statistica che o sia maggiore di 0.3 mg? Vi è evidenza statistica che sia minore di tale valore? (Per rispondere si può usare il p-value.)

campione = [1.2, 1.1, 1.1, 1.3, 1.4, 1.3, 1.0, 1.2, 1.1, 1.3]
sigma = 0.3

p_value = dcq.test_chi_quadrato(campione, sigma)
print(f"p_value: {p_value}")

chi_quadrato = dcq.calcola_chi_quadrato(campione, sigma)
print(f"chi_quadrato: {chi_quadrato}")

print(dcq.conferma_ipotesi(chi_quadrato, p_value, 0.3, campione))


# Si vuole realizzare un test che verifichi al 20% di significatività l'ipotesi nulla che sigma≥0.3 usando campioni di 8 sigarette. 
# Si determini come vada fissata per tale test la regione critica relativa alla deviazione standard campionaria S.

alpha = 0.20

# Determinazione del valore critico chi-quadrato e calcolo del limite inferiore per S
limite_S = dcq.limite_inferiore_S(alpha, len(campione), sigma)
print(f"Limite inferiore per la deviazione standard campionaria (S): {limite_S:.4f}")

print(dcq.conferma_ipotesi(chi_quadrato, p_value, limite_S, campione))