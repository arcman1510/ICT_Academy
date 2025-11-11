package com.spring.ecommerce.entity;

import jakarta.persistence.*;

@Entity
public class Prodotto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descrizione;
    private int quantita;
    private double prezzo;
    private int sconto;
    private String categoria;

    @ManyToOne
    @JoinColumn(name = "venditore_id")
    private Venditore venditore;

    public Prodotto() {}

    public Prodotto(Long id, String descrizione, int quantita, double prezzo, int sconto, String categoria, Venditore venditore) {
        this.id = id;
        this.descrizione = descrizione;
        this.quantita = quantita;
        this.prezzo = prezzo;
        this.sconto = sconto;
        this.categoria = categoria;
        this.venditore = venditore;
    }

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}

	public int getQuantita() {
		return quantita;
	}

	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}

	public double getPrezzo() {
		return prezzo;
	}

	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}

	public int getSconto() {
		return sconto;
	}

	public void setSconto(int sconto) {
		this.sconto = sconto;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	public Venditore getVenditore() {
		return venditore;
	}

	public void setVenditore(Venditore venditore) {
		this.venditore = venditore;
	}
}