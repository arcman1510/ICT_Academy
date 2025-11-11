package com.spring.utente.entity;
import java.util.ArrayList;
import java.util.List;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring.utente.Utente;
import com.spring.utente.dto.NomeCognomeDTO;
import com.spring.utente.dto.UtenteDTO;
import com.spring.utente.service.UtenteService;


@RestController
@RequestMapping(path="/utenti")
public class UtenteController {
	
	
	private UtenteService service = new UtenteService();
	
	@GetMapping(path="/registra", consumes="application/json")
	public boolean registra(@RequestBody UtenteDTO dto) {
		//Fake method for testing purposes
		return service.registra(dto);
	}
	
	@GetMapping(path="/cerca/{id}", produces="application/json")
	public UtenteDTO cercaPerId(@PathVariable int id) {
		//Fake method for testing purposes
		return service.cercaPerID(id);
	}
	
	@GetMapping(path="/mostraTutti", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<Utente> mostraTutti() {
        return service.selectAll();
    }
	
    @GetMapping(path = "/elimina/{id}")
    public boolean elimina(@PathVariable int id) {
        return service.delete(id);
    }
    
    @GetMapping(path="/nomeCognome/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public NomeCognomeDTO getNomeCognome(@PathVariable int id) {
    	return service.getNomeCognome(id);
    }
	
	
}
