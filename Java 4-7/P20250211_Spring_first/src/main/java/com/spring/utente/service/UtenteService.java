package com.spring.utente.service;

import java.util.List;
import com.spring.utente.Utente;
import com.spring.utente.dao.DAOUtenteMappa;
import com.spring.utente.dto.NomeCognomeDTO;
import com.spring.utente.dto.UtenteDTO;
import com.spring.utente.utility.Conversioni; 

public class UtenteService {

    private DAOUtenteMappa dao = new DAOUtenteMappa();

    public boolean registra(UtenteDTO dto) {
        Utente entity = Conversioni.daUtenteDTOAUtente(dto);
        return dao.insert(entity);
    }

    public UtenteDTO cercaPerID(int id) {
        Utente utente = dao.selectById(id);
        if (utente != null) {
            return Conversioni.daUtenteAUtenteDTO(utente);
        }
        return null;
    }

    public boolean delete(int id) {
        return dao.delete(id); // chiama il DAO per eliminare l'utente
    }

    public List<Utente> selectAll() {
        return dao.selectAll(); // restituisce la lista di utenti
    }

    public NomeCognomeDTO getNomeCognome(int id) {
        Utente utente = dao.selectById(id);
        if (utente != null) {
            return new NomeCognomeDTO(utente.getNome(), utente.getCognome()); // CORRETTO NomeCognomeDTO
        }
        return null;
    }
}