

public class Main {

	public static void main(String[] args) {
		
		
		/*
		 *  for i in range(0, 10):
		 *  	print(i)
		 * 
		 * 
		*/
		
		
		/* per il for: tre elementi separati da ;
		 * primo: dichiarazione e inizializzazione
		 * 			della variabile di ciclo
		 * second: condizione di permanenza nel ciclo
		 * terzo: incremento della variabile di ciclo
		 * 			da fare alla fine del ciclo
		 */
		
		
		
		for (int i=0; i<10; i++) {
			System.out.println(i);
		}
		
		System.out.println();
		
//		for (;;) {
//			System.out.println("Ciao");
//		}
	
		System.out.println();
		
		int i1=20;
		for (; i1<25; i1 += 10) {
			System.out.println(i1);
		}
		
		System.out.println();
		
		for (int i=0; i<10; i++) {
			System.out.println(i);
		}
		
		System.out.println();
		
//		for (int i=0; i<1;) {
//			System.out.println(i);
//		}
		System.out.println();
		
		for (int i= 0; i<=10; i++) {
			double n = Math.random();
			System.out.println(n);
		}

		System.out.println();
		
		for (int i= 0; i<=10; i++) {
			double n = Math.random();
			System.out.print(n);
			System.out.print(" ");
		}
		
		System.out.println();
		
		for (int i= 0; i<=10; i++) {
			double n = Math.random();
			System.out.println((i<9)?" ":"" + (i+1) + ") " + n);
		}
		/*
		 *  Operatore ternario
		 *  <espressione logica> ? <valore if true>:<valore if false>
		 */
		
		
		System.out.println();
		
		for (int i= 0; i<=10; i++) {
			double n = Math.random();
			System.out.printf("%2n)\t%4.3g\n", i+1, n);
		
	}
		/*
		 * System.out.printf è un metodo che vuole come parametri
		 * 1) una stringa di formato
		 * 2) un elenco di variabili i cui valori
		 * 		saranno inseriti nella stringa risultante
		 * 		in corrispondenza dei caratteri %<dgcs..> dove
		 * 		d: intero
		 * 		c: char
		 * 		g: float
		 * 		s: string
		 * 		...
		 * 		Inoltre nella stringa di formato
		 *		\n => vai a capo a nuova riga
		 *		\r => vai a capo sulla riga corrente
		 *		\t => inserisci un tab
		 *		Tutto quello che non è %<...> oppure\.
		 *		viene riportato in stampa così com'è
		 * 
		 */
		
		
	}
}
