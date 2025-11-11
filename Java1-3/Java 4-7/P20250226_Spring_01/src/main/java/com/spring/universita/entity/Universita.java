package com.spring.universita.entity;

public class Universita {

	
	private int matricola, anno_nascita, anno_immatricolazione, p_id;
	private String nome, cognome, indirizzo, password, p_nome, p_cognome, p_materia;
	
	
	
	public Universita() {
	}

	public Universita(int matricola, int anno_nascita, int anno_immatricolazione, int p_id, String nome, String cognome,
			String indirizzo, String password, String p_nome, String p_cognome, String p_materia) {
		super();
		this.matricola = matricola;
		this.anno_nascita = anno_nascita;
		this.anno_immatricolazione = anno_immatricolazione;
		this.p_id = p_id;
		this.nome = nome;
		this.cognome = cognome;
		this.indirizzo = indirizzo;
		this.password = password;
		this.p_nome = p_nome;
		this.p_cognome = p_cognome;
		this.p_materia = p_materia;
	}

	public int getMatricola() {
		return matricola;
	}

	public void setMatricola(int matricola) {
		this.matricola = matricola;
	}

	public int getAnno_nascita() {
		return anno_nascita;
	}

	public void setAnno_nascita(int anno_nascita) {
		this.anno_nascita = anno_nascita;
	}

	public int getAnno_immatricolazione() {
		return anno_immatricolazione;
	}

	public void setAnno_immatricolazione(int anno_immatricolazione) {
		this.anno_immatricolazione = anno_immatricolazione;
	}

	public int getP_id() {
		return p_id;
	}

	public void setP_id(int p_id) {
		this.p_id = p_id;
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

	public String getIndirizzo() {
		return indirizzo;
	}

	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getP_nome() {
		return p_nome;
	}

	public void setP_nome(String p_nome) {
		this.p_nome = p_nome;
	}

	public String getP_cognome() {
		return p_cognome;
	}

	public void setP_cognome(String p_cognome) {
		this.p_cognome = p_cognome;
	}

	public String getP_materia() {
		return p_materia;
	}

	public void setP_materia(String p_materia) {
		this.p_materia = p_materia;
	}
	
	
	
	
}
