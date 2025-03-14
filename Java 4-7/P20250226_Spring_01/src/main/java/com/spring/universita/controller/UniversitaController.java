package com.spring.universita.controller;

import java.util.List;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.universita.dto.NomeCognomeDTO;
import com.spring.universita.dto.UniversitaDTO;
import com.spring.universita.service.UniversitaService;

@RestController
@RequestMapping(path="/universita")

public class UniversitaController {

	private UniversitaService service = new UniversitaService();
	@GetMapping(path="/registra", consumes = "application/json")
	public boolean registra(@RequestBody  UniversitaDTO dto) {
		// fake
		//System.out.println("ho registrato l'utente: "  + utente);
		//return true;
		
		return service.registra(dto);
	}
	
	@GetMapping(path="/cerca/{id}", produces = "application/json")
	public UniversitaDTO cercaPerId(@PathVariable  int id) {
		// fake
		//return new Utente(id, "mario", "rossi", "mario", "red");
		
		return service.cercaPerId(id);
	}
	
	@GetMapping(path="/mostraTutti", produces = "application/json")
	public List<UniversitaDTO> mostraTutti(){
		return service.mostraTutti();
	}
	
	@GetMapping(path="/modificaPassword/{idUtente}", produces = "application/json")
	public UniversitaDTO modificaMail(@PathVariable int idUtente, String password) {
		return service.updatePassword(idUtente, password);
	}
	
	@GetMapping(path="/cancella/{idUtente}", produces = MediaType.APPLICATION_JSON_VALUE)
	public UniversitaDTO cancellaUtente(@PathVariable int idUtente) {
		return service.cancella(idUtente);
	}

	@GetMapping(path="/nomeCognome/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
	public NomeCognomeDTO getNomeCognome(@PathVariable int id) {
		return service.getNomeCognome(id);
	}
}
