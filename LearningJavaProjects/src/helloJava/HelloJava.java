package helloJava;

import java.util.Scanner;

public class HelloJava {
	
	public static void main(String [] args){
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		System.out.println("Hallo User, welcome to Billy's computer program");
		System.out.println("So what's your name, Dear User -- Enter Below");
		String yourName = input.nextLine();
	    System.out.println("Hallo, " + yourName);
	    
//	    Executing string formats.. for development.
	    System.out.printf("Hallo, %s", yourName);
	}

}
