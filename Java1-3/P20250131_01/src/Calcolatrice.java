public class Calcolatrice {
	
		public static void main(String[] args) {
		
			Calcolatrice c = new Calcolatrice();
			
		
			System.out.println("La somma è " + c.somma(3, 2));
		}
		
		public int somma(int a, int b) {
		
			return a + b;
		}
		
	    public int sottrai(int a, int b) {
	        return a - b;
	    }
	    
	    public int moltiplica(int a, int b) {
	        return a * b;
	    }
	    
	    public double dividi(int a, int b) {
	        if (b == 0) {
	            throw new ArithmeticException("Impossibile dividere per zero");
	        }
	        return (double) a / b;
	    }

}
