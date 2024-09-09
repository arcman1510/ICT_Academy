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