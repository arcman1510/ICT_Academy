--1. Quali sono gli aeroporti (restituire codice e nome) della
--città di Roma [2 punti]

Select a.codice, a.nome
From LuogoAeroporto l
JOIN Aeroporto a
On a.codice = l.aeroporto
where l.citta = 'Roma'

Select a.codice, a.nome
From LuogoAeroporto l
JOIN Aeroporto a
On a.codice = l.aeroporto
where l.nazione = 'France'

--2. Quali sono le compagnie (restituire nome e anno di
--fondazione) che hanno voli di durata di almeno 3 ore [3
--punti]

Select C.nome, C.annofondaz
From Compagnia C, Volo V
where C.nome = V.comp
and V.durataMinuti >= 180;

SELECT DISTINCT C.nome, C.annoFondaz
FROM Compagnia C
JOIN Volo V ON C.nome = V.comp
WHERE V.durataMinuti >= 180;


--3. Qual è la durata più lunga di un volo di ogni compagnia
--(restituire nome della compagnia e durata di tale volo) [3
--punti]

SELECT C.nome, max(V.durataMinuti)
FROM Volo V
JOIN Compagnia C ON V.comp = C.nome
GROUP BY C.nome

SELECT C.nome, min(V.durataMinuti)
FROM Volo V
JOIN Compagnia C ON V.comp = C.nome
GROUP BY C.nome



--4. Quali sono le compagnie che hanno voli che atterrano in
--un qualche aeroporto di New York [3 punti]

SELECT DISTINCT C.nome
FROM Compagnia C, ArrPart A
JOIN Volo V ON V.comp = C.nome
AND LuogoAeroporto L ON L.aeroporto = A.arrivo
WHERE A.arrivo = 'JFK' 

SELECT DISTINCT C.nome
FROM Compagnia C
JOIN Volo V ON C.nome = V.comp
JOIN ArrPart A ON V.codice = A.codice AND V.comp = A.comp
JOIN LuogoAeroporto L ON A.arrivo = L.aeroporto
WHERE L.citta = 'New York';


SELECT C.nome, V.codice, A.codice, A.arrivo
FROM Compagnia C
JOIN Volo ON C.nome = V.comp
JOIN ArrPart ON V.codice = A.codice AND v.comp = A.comp




--5. Quali sono i piani di volo con un cambio che collegano
--Roma a New York in al più 6 ore (escludendo il tempo del
--cambio) [4 punti]



--6. Quanti sono, per ogni compagnia, i piani di volo con un
--cambio (con entrambi i voli di quella compagnia) che
--collegano Roma a New York in al più 6 ore [4 punti]




--7. Quali sono i piani di volo con un cambio in Germania che
--collegano Roma a New York in al più 6 ore di volo
--(escludendo il tempo di cambio in Germania). Ordinare i
--voli per durata di volo complessiva (escludendo il tempo di
--cambio) crescente [4 punti]



--8. Qual è l’anno nel quale è stata fondata la prima
--compagnia aerea presente nel db [2 punti]



--9. Quante sono le compagnie aeree di cui non si conosce
--l’anno di fondazione [2 punti]


--10. Quante sono le compagnie aeree fondate ogni anno. Per
--ogni anno nel quale è stata fondata almeno una
--compagnia, restituire l’anno e il numero di compagnie
--fondate in quell’anno [3 punti]
--Si scriva il codice SQL in un file chiamato


