package com.spring.ecommerce.entity;

import jakarta.persistence.*;
import java.util.*;

@Entity
public class Venditore {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private String cognome;
    private String username;
    private String password;
    private String via;
    private String citta;

    @OneToMany(mappedBy = "venditore", cascade = CascadeType.ALL)
    private List<Prodotto> prodotti = new ArrayList<>();

    public Venditore() {}

    public Venditore(Long id, String nome, String cognome, String username, String password, String via, String citta, List<Prodotto> prodotti) {
        this.id = id;
        this.nome = nome;
        this.cognome = cognome;
        this.username = username;
        this.password = password;
        this.via = via;
        this.citta = citta;
        this.prodotti = prodotti;
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

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
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

	public List<Prodotto> getProdotti() {
		return prodotti;
	}

	public void setProdotti(List<Prodotto> prodotti) {
		this.prodotti = prodotti;
	}
}