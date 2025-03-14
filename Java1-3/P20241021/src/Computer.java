public class Computer {
    private double prezzo;
	private double peso;
    private double larghezza, altezza, profondità;
    private String produttore;
    private int annoDiProduzione;
    
    privatw static int contatore = 0;
   
    //Classi Wrapper che nascondono i tipi primitivi di java
    // int => Integer
    //double => Double
    /
    
    public Computer() {
    	contatore++;
    
    }
    
    public Computer(Double prezzo, Double peso) {
    	this.prezzo = prezzo;
    	this.peso = peso;
    	contatore++;
    }
    
    static public int GetContatore() {
    	
    	return contatore;
    }
    
    
    public double getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso = peso;
	}
	public double getLarghezza() {
		return larghezza;
	}
	public void setLarghezza(double larghezza) {
		this.larghezza = larghezza;
	}
	public double getAltezza() {
		return altezza;
	}
	public void setAltezza(double altezza) {
		this.altezza = altezza;
	}
	public double getProfondità() {
		return profondità;
	}
	public void setProfondità(double profondità) {
		this.profondità = profondità;
	}
	public String getProduttore() {
		return produttore;
	}
	public void setProduttore(String produttore) {
		this.produttore = produttore;
	}
	public int getAnnoDiProduzione() {
		return annoDiProduzione;
	}
	public void setAnnoDiProduzione(int annoDiProduzione) {
		this.annoDiProduzione = annoDiProduzione;
	}
	public Computer(double prezzo, double peso, double larghezza, double altezza, double profondità, String produttore, 
			int annoDiProduzione) {
		super();
		this.prezzo = prezzo;
		this.peso = peso;
		this.larghezza = larghezza;
		this.altezza = altezza;
		this.profondità = profondità;
		this.produttore = produttore;
		this.annoDiProduzione = annoDiProduzione;
		contatore++;

	}

}

	