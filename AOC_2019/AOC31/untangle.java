import java.lang.Math;
import java.util.*;
import java.util.Collections; 
public class untangle {
	public static ArrayList<String> subs = new ArrayList<String>(); 
	public static ArrayList<Integer> intersect = new ArrayList<Integer>(); 	
	public static ArrayList<Integer> intcoor = new ArrayList<Integer>(); 	
	public static void MrSubs (String input) {
		//returns Array of strings, subs
		subs.removeAll(subs); 
		
		int counter =0; 	
		for (int i = 0; i< input.length(); i++) {
			if (input.charAt(i) == ',' ) {
				subs.add(input.substring(i-counter,i)); 
				counter = 0;  
			}
			else {
				counter ++; 
			}
		}

	}
	public static void comparer(Wire wire1, Wire wire2) {
		for (int i= 0; i< wire1.getX(); i++) {
			System.out.println(i);
		for (int j= 0; j< wire1.getY(); j++) {	
				if ((wire1.getPos()[i][j] == true && wire2.getPos()[i][j] == true)) {
					intersect.add(Math.abs(i-(wire1.getStartx()))+ Math.abs(j-(wire2.getStarty()))); 
					intcoor.add(i);
					intcoor.add(j);
					//System.out.println(i + " " + j);
				}
				else {
					
				}
		}
		} 
		
	}
	public static int Steps(int smallest_md) { 

	int s = smallest_md; 
	char direction;
	int numSteps =0 ;  
	//^^^^^ '' is no movement, 'L' is left, 'U' is up etc.... 
	//coordinates of intersection
	int ix;
	int iy;
	//current coordinates in loop
	int x;
	int y; 
	
	int i=0;
	//finds coordinates of intersection
	while ( i < intcoor.size() ){
	if (intcoor.get(i) + intcoor.get(i+1) == s) {
		ix = intcoor.get(i); 
		iy = intcoor.get(i+1);
		i = intcoor.size(); 
	}
	else {
		i +=2;
	}
	}
	return numSteps; 
	}	
	//now that coordinates of intersection have been determined, we can work on backtracking to start and counting steps; 
	public static int md () {
		int smallest_md = 0;
		Collections.sort(intersect);
		int c =0; 
		for (int i =0; i<intersect.size(); i++) {
			System.out.println(intersect.get(i));
		}
		while (c<intersect.size()) {
			if (intersect.get(c) != 0){
			smallest_md = intersect.get(c);
			c = intersect.size();
			}
			else {
			c ++; 
			} 	
		} 
		return smallest_md; 
	}
	public static int subcheckX (ArrayList<String> s ) {
		//returns int x	
		int x =0;
		for (int i = 0; i<s.size(); i++) {
			if (s.get(i).charAt(0) == 'L' || s.get(i).charAt(0) == 'R') {
				x += Integer.valueOf(s.get(i).substring(1));
			}
			else {

			}
		}
		return x;
	}
	public static int subcheckY (ArrayList<String> s) {
		//returns int y
		int y = 0; 
		for (int i =0; i<s.size(); i ++) {
			if (s.get(i).charAt(0) == 'U' || s.get(i).charAt(0) == 'D'){
				y += Integer.valueOf(s.get(i).substring(1)); 
			}
			else {

			}
		}
		return y; 
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); 
		String input1 = scan.next() + ",";
		String input2 = scan.next() + ",";
		
		//creates pos for wire1
		MrSubs(input1);
		int x = subcheckX(subs); 
		int y = subcheckY(subs);
		Wire wire1 = new Wire(subs,x,y);
		wire1.builder();
		//creates pos for wire2
		MrSubs(input2); 
		Wire wire2 = new Wire(subs,x,y);
		wire2.builder();
		// uses both pos to find points of intersection, compares their man distances
		comparer(wire1, wire2);
		//int s = lowStep();  
		int m = md(); 
		System.out.println("Manhattan Distance: " + m);
		  
	}
}

