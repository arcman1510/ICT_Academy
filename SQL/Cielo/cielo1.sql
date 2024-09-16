
--Definire in SQL le seguenti interrogazioni, 
--in cui si chiedono tutti risultati distinti:


--1. Quali sono i voli (codice e nome della compagnia)
-- la cui durata supera le 3 ore?

Select codice, comp
From Volo
Where durataMinuti >300



--2. Quali sono le compagnie che hanno voli che superano le 3 ore?

Select distinct comp
From Volo
Where durataMinuti >300


--3. Quali sono i voli (codice e nome della compagnia) 
--che partono dall’aeroporto con codice ‘CIA’ ?

Select codice, comp
From ArrPart
Where partenza = 'CIA'

-- 4. Quali sono le compagnie che hanno voli che 
--arrivano all’aeroporto con codice ‘FCO’ ?

Select distinct comp
From ArrPart
Where arrivo = 'FCO'

--5. Quali sono i voli (codice e nome della compagnia) 
-- che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

Select codice, comp
From ArrPart 
Where partenza = 'FCO'
and arrivo = 'JFK'

--6. Quali sono le compagnie che hanno voli che 
--partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

Select distinct comp
From ArrPart 
Where partenza = 'FCO'
and arrivo = 'JFK'

--7. Quali sono i nomi delle compagnie che hanno voli diretti 
--dalla città di ‘Roma’ alla città di ‘New York’ ?

Select distinct v.comp
From Volo v join ArrPart ap
	on v.codice = ap.codice
Where ap.partenza = 'FCO' 
or ap.partenza = 'CIA'
and ap.arrivo = 'JFK'

--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) 
--nei quali partono voli della compagnia di nome ‘MagicFly’ ?

Select a.codice, a.nome, la.citta
From Aeroporto a, LuogoAeroporto la, ArrPart ap
Where a.codice = la.aeroporto
And a.codice = ap.partenza
And ap.comp = 'MagicFly'

--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
--atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
--del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select *
from arrpart ap join aeroporto a 
on ap.partenza = a.codice


--10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
--voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
--qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
--codici dei voli, e aeroporti di partenza, scalo e arrivo.

Select v1.comp, v1.codice, v2.codice, v1.partenza, v1.arrivo, v2.arrivo
From ArrPart v1, ArrPart v2, LuogoAeroporto lp, LuogoAeroporto la
Where v1.arrivo = v2.partenza
and v1.comp = v2.comp
and v1.partenza = lp.Aeroporto
and v2.partenza= la.Aeroporto
and lp.citta = 'Roma'
and la.citta = 'New York'

--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, 
--atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione


select distinct comp
from arrpart ap, compagnia c 
where comp = c.nome
and ap.partenza = 'FCO'
and ap.arrivo = 'JFK'
and annofondaz is not null