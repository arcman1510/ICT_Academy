package com.spring.utente.utility;

import com.spring.utente.Utente;
import com.spring.utente.dto.UtenteDTO;

public class Conversioni {

		public static Utente daUtenteDTOAUtente(UtenteDTO dto) {
			return new Utente(dto.getId(), dto.getNome(), dto.getCognome(), dto.getUsername(), dto.getPassword());
		}
		public static UtenteDTO daUtenteAUtenteDTO(Utente entity) {
			return new UtenteDTO(entity.getId(), entity.getNome(), entity.getCognome(), entity.getUsername(), entity.getPassword());
		}

}
