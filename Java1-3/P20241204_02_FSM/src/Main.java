import java.util.Scanner;

public class Main {

	public static void main (String[] args) {
		Scanner rd = new Scanner(System.in);
		while (true) {
			System.out.println("A che piano devo: []0,1,2,3");
			int piano = rd.nextInt();
			Macchina(piano);
		}
	}

	static int [][]fsm= {{0, 1, 2, 3},
						 {-1, 0, 1, 2},
						 {-2, -1, 0, 1},
						 {-3, -2, -1, 0}
		// TODO Auto-generated method stub
		
	};
	
	private static void Macchina(int piano) {
		// TODO Auto-generated method stub
		
	}
}
