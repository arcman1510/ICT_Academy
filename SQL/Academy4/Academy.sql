--Definire in SQL le seguenti interrogazioni:
--1. Quali sono i cognomi distinti di tutti gli strutturati?

select distinct id, cognome
from Persona
order by cognome asc

--2. Quali sono i Ricercatori (con nome e cognome)?

select id, cognome, nome
from Persona
where posizione = 'Ricercatore'
order by cognome asc

--3. Quali sono i Professori Associati 
--il cui cognome comincia con la lettera ‘V’ ?

select id, cognome, nome
from Persona
where posizione = 'Professore Associato'
and cognome like 'V%'
order by cognome asc

--4. Quali sono i Professori (sia Associati che Ordinari) 
--il cui cognome comincia con la lettera ‘V’ ?

select id, cognome
from Persona
where posizione like 'Professore%' and cognome like 'V%'


--5. Quali sono i Progetti già terminati alla data odierna?

select id, nome
from Progetto
where fine < CURRENT_DATE



-- 6. Quali sono i nomi di tutti i Progetti ordinati 
-- in ordine crescente di data di inizio?

select id, nome, inizio
from Progetto
where fine < CURRENT_DATE
order by inizio asc

--7. Quali sono i nomi dei WP ordinati 
--in ordine crescente (per nome)?



--8. Quali sono (distinte) le cause di assenza
--di tutti gli strutturati?



--9. Quali sono (distinte) le tipologie 
--di attività di progetto di tutti gli strutturati?



--10. Quali sono i giorni distinti nei quali 
--del personale ha effettuato attività 
--non progettuali di tipo ‘Didattica’ ? 
--Dare il risultato in ordine crescente


