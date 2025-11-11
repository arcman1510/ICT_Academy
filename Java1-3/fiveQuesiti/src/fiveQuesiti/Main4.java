package fiveQuesiti;

public class Main4 {

	public static void main(String[] args) {
		//4. Funzione che verifica se un numero è positivo o negativo
		        int numero = -8;
		        verificaSegno(numero);
		    }

		    public static void verificaSegno(int n) {
		        if (n > 0) {
		            System.out.println("Il numero è positivo");
		        } else if (n < 0) {
		            System.out.println("Il numero è negativo");
		        } else {
		            System.out.println("Il numero è zero");
		        }
		    }
}
