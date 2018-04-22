package firstproject;
import java.util.Scanner;

import javax.*;
import javax.activation.*;
import javax.annotation.processing.*;
import javax.imageio.*;

public class Starter {
    //Scanner class is used to facilitate input values...
	static Scanner scan = new Scanner(System.in);
	public static void main(String [] args){	
         welcome_message();
         System.out.println("");
	}
	
	public static void welcome_message(){
		System.out.println("****************************************************************************");
		System.out.println("****************************************************************************");
		System.out.println("******  WELCOME TO YOUR FINAL PROGRAMME                             ********");
		System.out.println("****************************************************************************");
		System.out.println("****************************************************************************");
		System.out.println("Enter your First Name: ");
		String firstname = scan.nextLine();
	}
	
	public static void show_starting_menu(){
		
	}
	
	public static double calculate_tax(){
		return 0;	
	}
	
	public static void enter_customer_address(){
		
	}
	
	public static void show_balance_chckbook(){
		
	}
	
	public static void calculate_sales_tax(){
		
	}
	
	public static void conversion_utility(){
		
	}
	
}

