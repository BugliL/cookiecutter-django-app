
# Per ogni operazione eseguibile sui modelli di competenza dell'applicazione, questo modulo 
# deve esporre un metodo da poter chiamare.

# Al fine di garantire la compatibilità in futuro, i metodi del modulo Proxy dovranno ritornare
# strutture dati native di Python (Liste, Dizionari, ecc...) evitando categoricamente istanze 
# di classi ORM o oggetti di altro tipo.