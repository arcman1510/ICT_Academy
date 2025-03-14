
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
         * Realizzare una classe Computer con i seguenti attributi
         * - Prezzo
         * - Peso
         * - Dimensioni (larghezza, altezza, profondità)
         * - Produttore
         * - Anno di produzione
         * 
         * Nel main creare degli oggetti di tipo Computer
         * e stampare il loro contenuto
         * 
         * NB: ricordate di utilizzare getter, setter e costruttore
         * generati da eclipse
         * 
         * Bonus: aggiungere un metodo alla classe Computer 
         * che stampi quanti oggetti (di tipo Computer) sono stati creati
         */
		
		
		
		
		Computer com1 = new Computer();
		com1.setAltezza(1.5);
		com1.setAnnoDiProduzione(2023);
		com1.setLarghezza(35);
		com1.setLarghezza(35.0);
		com1.setPeso(4.5);
		com1.setPrezzo(4500.);
		com1.setProduttore("Archer");
		com1.setProfondità(2.5);
		
		Computer com2 = new Computer(9875., 7.2, 60., 5., 40., "IBM", 1990);
		
		Computer com3 = new Computer(9875., 7.2);
		com3.setAltezza(1.5);
		com3.setAnnoDiProduzione(2023);
		com3.setLarghezza(35.0);
		com3.setProduttore("Archer");
		com3.setProfondità(25.0);
		
		System.out.println(com1);
		
		
		Integer.parseInt("1923");
		
		com1.equals(com3);
		
		System.out.println("");
		
/*		int num = 10;
		
		Integer n1 = 10;
		n1.
	*/	
	}

}
