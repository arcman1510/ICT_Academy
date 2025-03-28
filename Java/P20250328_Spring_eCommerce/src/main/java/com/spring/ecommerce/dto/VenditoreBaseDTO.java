package com.spring.ecommerce.dto;

public class VenditoreBaseDTO {
    private Long id;
    private String nome;
    private String cognome;
    private String username;
    private String via;
    private String citta;

    public VenditoreBaseDTO() {}

    public VenditoreBaseDTO(Long id, String nome, String cognome, String username, String via, String citta) {
        this.id = id;
        this.nome = nome;
        this.cognome = cognome;
        this.username = username;
        this.via = via;
        this.citta = citta;
    }

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getVia() {
		return via;
	}

	public void setVia(String via) {
		this.via = via;
	}

	public String getCitta() {
		return citta;
	}

	public void setCitta(String citta) {
		this.citta = citta;
	}


}