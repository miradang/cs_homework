/* Miranda Dangerfield 
 PA1
 dangerfieldOrdering.java 
Due Date: ???? */

import java.util.Scanner;
//import java.util.ArrayList;
import java.util.HashMap;


// class for food

public class Food {
  String name;
  double price;
  int id = 0; //needed a way to auto give each object its own id
  HashMap<String, String> subFood = new HashMap<>();

  Food(String name, double price) {
    this.name = name;
    this.price = price;
    this.id = id++;
    subFood.put(this);

  }

  public String displayP(
    String output = "";
    output = name + " is " + price;
    return output;
  )

  public int foodID(
    return this.id;
  )

}


public class ordering {
  public static void main(String[] args) {
      //food info storage
    Food chCurry = new Food(Chicken Curry, 10.69);
    Food spCurry = new Food(Shrimp Curry, 14.25);
    Food naan = new Food(Naan), 3.59);
    Food chai = new Food(Chai, 2.45);
    Food crab = new Food(Crabs, 7.24);
    Food lBir = new Food(Lamb Biriyani, 15.59);
    Food vBir = new Food(Vegtable Biriyani, 11.27);
    Food gMan = new Food(Gobi Manchurian, 10.35);
    Food cMas = new Food(Chana Masala);
    Food khee = new Food(Kheer, 4.99);
    // end food storage. Doing this instead of a dict for fun

    Scanner scnr = new Scanner(System.in);
    int menuOpen = 1;
    
    while (menuOpen == 1) {
      System.out.println(subFood);
      menuOpen = scnr.nextInt();

    }






















     // The Scanner does not directly support reading a single character.
     //  userChar = scnr.next().charAt(0);. next() reads a string from the user input, 
     // then charAt(0) gets the first character within that string.