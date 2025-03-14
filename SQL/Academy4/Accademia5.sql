--Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:


--1. Quali sono il nome, la data di inizio e 
--la data di fine dei WP del progetto di nome ‘Pegasus’ ?

Select w.nome, w.inizio, w.fine
From Progetto p, WP w
Where p.id = w.progetto
and p.nome = 'Pegasus'

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
--una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select distinct ps.nome, ps.cognome, posizione
From Progetto pr, AttivitaProgetto ap, Persona ps
Where pr.nome = ' Pegasus';
and ap.progetto = p.id
and ps.id = ap.persona
order by cognome desc;
--rivedere


--3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
--una attività nel progetto ‘Pegasus’ ?

--screen

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto almeno una assenza per malattia?

select select distinct nome, cognome, posizione
from persona p join assenzaa
on p.id = a.persona
where p.posizione = 'Professore Ordinario'
and a.tipo = 'Malattia';

--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
--fatto più di una assenza per malattia?

--screen

--6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
--un impegno per didattica?

--screen

--7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
--impegno per didattica?

-- screen rivedere

--8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--attività progettuali che attività non progettuali?

--screen 

--9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
--attività progettuali che attività non progettuali? Si richiede anche di proiettare il
--giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
--entrambe le attività.



--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività progettuali?



--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
--assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
--nome del progetto, la causa di assenza e la durata in ore della attività progettuale.



--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?


