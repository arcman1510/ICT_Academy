--QUERY 1. Qual è il numero di progetti a cui partecipa ogni
--professore ordinario. Per ogni professore ordinario,
--restituire nome, cognome, numero di progetti nei quali è
--coinvolto [3 punti]

Select p.nome, p.cognome, count(a.persona)
From Persona p, AttivitaProgetto a
Where p.id = a.persona
and p.posizione ='Professore Ordinario'
group by p.cognome, p.nome
having count (a.persona) >= 1


--QUERY 2. Qual è il numero medio di ore delle attività progettuali
--svolte da ogni ricercatore. Per ogni ricercatore, restituire
--nome, cognome e numero medio di ore delle sue attività
--progettuali (in qualsivoglia progetto) [3 punti]




--QUERY 3. Quali sono le persone con stipendio 
--di almeno 60000 euro [2 punti]

Select id, nome, cognome, stipendio
From Persona
Where stipendio >= 60000


--QUERY 4. Qual è il budget totale dei progetti a cui lavora ogni
--professore associato. Per ogni professore associato
--restituire nome, cognome e budget totale dei progetti nei
--quali è coinvolto. [3 punti]




--QUERY 5. Qual è il numero totale di giorni di assenza per 
--maternità di ogni ricercatore. 
--Per ogni ricercatore, restituire nume,cognome 
--e numero di giorni di assenza per maternità [3 punti]

Select distinct p.nome, p.cognome, count(a.giorno)
From Assenza a, Persona p
Where p.id = a.persona
and a.tipo = 'Maternita'
group by p.cognome, p.nome, a.giorno
having count (a.giorno) >= 1


--QUERY 6. Qual è il budget medio dei progetti nel db [2 punti]

Select avg(budget)
From Progetto



--QUERY 7. Qual è il numero totale di ore, per ogni persona, 
--dedicate al progetto con id ‘3’. 
--Per ogni persona che lavora al
--progetto, restituire nome, cognome e numero di ore totali
--dedicate ad attività progettuali relative al progetto [4
--punti]




--QUERY 8. Quali sono i professori ordinari che hanno svolto 
--attività
--nel WP di id ‘3’ del progetto con id ‘4’. 
--Per ogni professore
--ordinario, restituire il numero totale di ore 
--svolte in
--attività progettuali per il WP in questione [4 punti]




--QUERY 9. Quali sono i professori ordinari che lavorano 
--ad almeno un
--progetto e hanno uno stipendio di almeno 60000 [2 punti]

Select distinct p.nome, p.cognome, p.posizione, sum(a.progetto)
From Persona p, AttivitaProgetto a
Where p.id = a.persona
and stipendio >= 60000
and p.posizione ='Professore Ordinario'
group by p.cognome, p.nome, p.posizione
having count (a.progetto) >= 1




--QUERY 10. Qual è la durata media in ore delle attività 
--didattiche
--svolte da ogni persona. Per ogni persona che ha svolto
--attività didattica, restituire nome, cognome e numero
--medio di ore delle sue singole attività didattiche [4 punti]

Select distinct p.nome, p.cognome, sum(a.oreDurata)
From AttivitaNonProgettuale a, Persona p
Where p.id = a.persona
and a.tipo = 'Didattica'
group by p.cognome, p.nome, a.oreDurata
having count (a.oreDurata) >= 1

