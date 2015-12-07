import java.util.Scanner;


public class PrimeNumbers {
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int num = s.nextInt();
		while (num != -1) {
			System.out.println("Recursive: " + isPrimeRecur(num));
			System.out.println("Iterative: " + isPrimeIter(num));
			System.out.print("\nEnter a number: ");
			num = s.nextInt();
		}
	}
	
	public static boolean isPrimeRecur(int n) {
		return null;
	}
	
	public static boolean isPrimeIter(int n) {
		return null;
	}

}
