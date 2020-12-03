import java.util.*;
import java.lang.Math;
import java.util.Collections;
public class AOC3 {
		//wire1
		private static ArrayList<Integer> x1vals = new ArrayList<Integer>();
		private static ArrayList<Integer> y1vals = new ArrayList<Integer>();
	
		//wire2 
		private static ArrayList<Integer> x2vals = new ArrayList<Integer>();
		private static ArrayList<Integer> y2vals = new ArrayList<Integer>();
	
		private static ArrayList<Integer> mds = new ArrayList<Integer>();
		private static ArrayList<String> subs = new ArrayList<String>();  
		//mds lists md of all intersections to be used for comparasin in main
		//instead of a 2d, every 2 terms are the x and y coordinate
	

	//accessors
	public static ArrayList<Integer> getlistx1() {
		return x1vals;
	}
	public static ArrayList<Integer> getlisty1() {
		return y1vals;
	}
	public static ArrayList<Integer> getlistx2() {
		return x2vals;
	}
	public static ArrayList<Integer> getlisty2() {
		return y2vals; 
	}
	public static ArrayList<Integer> getlistmds() {
		return mds; 
	}
	public static ArrayList<String> getsubs() {
		return subs;
	}
	
	//builders
	public static void x1builder() {
		getlistx1().add(0); //sets starting point
		for (int j = 0; j<subs.size(); j++) {
			for (int k = 0; k<subs.get(j).length(); k++) {
				if (subs.get(j).charAt(k) == 'L') {
					//use xvals
					String strx= subs.get(j).substring(k+1);
					int prev = getlistx1().get(getlistx1().size() -1);
					for(int m=1; m<=Integer.valueOf(strx); m++){ 
						int numx = prev - m;
						getlistx1().add(numx); 
					}
				}
				else if (subs.get(j).charAt(k) == 'R') {
					//use xvals
					String strx= subs.get(j).substring(k+1);
					int prev = getlistx1().get(getlistx1().size() -1);
					for(int m=1; m<=Integer.valueOf(strx); m++){ 
						int numx = prev + m;
						getlistx1().add(numx); 
					}

				}
				else if (subs.get(j).charAt(k) == 'U' || subs.get(j).charAt(k) == 'D') {
					String str = subs.get(j).substring(k+1); 
					int prev = getlistx1().get(getlistx1().size() -1);
					for (int m =1; m<=Integer.valueOf(str); m++) {
						getlistx1().add(prev);
					}
				}
			} 			 
		}

	}
	public static void y1builder() {
		getlisty1().add(0); //sets starting point
		for (int j = 0; j<subs.size(); j++) {
			for (int k = 0; k<subs.get(j).length(); k++) {
				if (subs.get(j).charAt(k) == 'D') {
					String stry= subs.get(j).substring(k+1);
					int prev = getlisty1().get(getlisty1().size() -1);
					for(int m=1; m<=Integer.valueOf(stry); m++){ 
						int numy = prev - m;
						getlisty1().add(numy); 
					}
				}
				else if (subs.get(j).charAt(k) == 'U') {
					//use xvals
					String stry= subs.get(j).substring(k+1);
					int prev = getlisty1().get(getlisty1().size() -1);
					for(int m=1; m<=Integer.valueOf(stry); m++){ 
						int numy = prev + m;
						getlisty1().add(numy); 
					}

				}
				else if (subs.get(j).charAt(k) == 'L' || subs.get(j).charAt(k) == 'R') {
					String str = subs.get(j).substring(k+1); 
					int prev = getlisty1().get(getlisty1().size() -1);
					for (int m =1; m<=Integer.valueOf(str); m++) {
						getlisty1().add(prev);
					}
				}

			} 			 
		}

	}
	public static void x2builder() {
		getlistx2().add(0); //sets starting point
		for (int j = 0; j<subs.size(); j++) {
			for (int k = 0; k<subs.get(j).length(); k++) {
				if (subs.get(j).charAt(k) == 'L') {
					//use xvals
					String strx= subs.get(j).substring(k+1);
					int prev = getlistx2().get(getlistx2().size() -1);
					for(int m=1; m<=Integer.valueOf(strx); m++){ 
						int numx = prev - m;
						getlistx2().add(numx); 
					}
				}
				else if (subs.get(j).charAt(k) == 'R') {
					//use xvals
					String strx= subs.get(j).substring(k+1);
					int prev = getlistx2().get(getlistx2().size() -1);
					for(int m=1; m<=Integer.valueOf(strx); m++){ 
						int numx = prev + m;
						getlistx2().add(numx); 
					}

				}
				else if (subs.get(j).charAt(k) == 'U' || subs.get(j).charAt(k) == 'D') {
					String str = subs.get(j).substring(k+1); 
					int prev = getlistx2().get(getlistx2().size() -1);
					for (int m =1; m<=Integer.valueOf(str); m++) {
						getlistx2().add(prev);
					}
				}

			} 			 
		}

	}
	public static void y2builder() {
		getlisty2().add(0);
		for (int j = 0; j<subs.size(); j++) {
			for (int k = 0; k<subs.get(j).length(); k++) {
				if (subs.get(j).charAt(k) == 'D') {
					//use xvals
					String stry= subs.get(j).substring(k+1);
					int prev = getlisty2().get(getlisty2().size() -1);
					for(int m=1; m<=Integer.valueOf(stry); m++){ 
						int numy = prev - m;
						getlisty2().add(numy); 
					}
				}
				else if (subs.get(j).charAt(k) == 'U') {
					//use xvals
					String stry= subs.get(j).substring(k+1);
					int prev = getlisty2().get(getlisty2().size() -1);
					for(int m=1; m<=Integer.valueOf(stry); m++){ 
						int numy = prev + m;
						getlisty2().add(numy); 
					}

				}
				else if (subs.get(j).charAt(k) == 'L' || subs.get(j).charAt(k) == 'R') {
					String str = subs.get(j).substring(k+1); 
					int prev = getlisty2().get(getlisty2().size() -1);
					for (int m =1; m<=Integer.valueOf(str); m++) {
						getlisty2().add(prev);
					}
				}


			} 			 
		}
	}
	public static void Mrsubs(String input) {
		getsubs().removeAll(getsubs()); 
		
		int counter =0; 	
		for (int i = 0; i< input.length(); i++) {
			if (input.charAt(i) == ',' ) {
				getsubs().add(input.substring(i-counter,i)); 
				counter = 0;  
			}
			else {
				counter ++; 
			}
		}
	

	}
	//other methods
	public static int md (int x, int y){
		int dis = Math.abs(x) + Math.abs(y);  
		return dis;
	} 
	
	public static void main (String[] args) { 
		
		Scanner scan = new Scanner(System.in); 
		//wire 1
		String input1 = scan.next() + ",";
		//wire 2
		String input2 = scan.next() + ",";
		
		Mrsubs(input1);
		x1builder(); 
		Mrsubs(input1);
		y1builder(); 
		Mrsubs(input2);
		x2builder();
		Mrsubs(input2);
		y2builder();
		//now all you need to do is use the x and y vals arrays to find possible intersections, find their mds and find the lowest md
		ArrayList<Integer> possible = new ArrayList<Integer>();
		ArrayList<Integer> mds = new ArrayList<Integer>(); 
		for (int i =0; i<getlistx1().size(); i++) {
			for (int j=0; j<getlistx2().size(); j++) {
				if (getlistx1().get(i) == getlistx2().get(j) && getlisty1().get(i) == getlisty2().get(j) ) {
						possible.add(getlistx1().get(i));
						possible.add(getlisty1().get(i));
						
						mds.add(md (possible.get(possible.size()-1), possible.get(possible.size()-2) ));						
				}

			}
		}
	//finds smallest mds that is not 0		
		Collections.sort(mds);
		int c =0;
		int smallest_md = 0; 
		while ( c < mds.size() ) {
			if (mds.get(c) != 0) {
				smallest_md= mds.get(c);
				c = mds.size(); 
			} 
			else {
				c ++;
			}
		} 

			
		//test print possibl?
		System.out.println("x1 vals:");
		for( int k=0; k<getlistx1().size(); k++) {
			System.out.print("index:" + k + " ");
			System.out.print("x1: " + getlistx1().get(k));
			System.out.println(" ");
		}
		System.out.println(" ");
		System.out.println("y1 vals:");
		for (int m =0; m<getlisty1().size();m++) {
			System.out.print("index:" + m + " ");
			System.out.print("y1: " + getlisty1().get(m));
			System.out.println(" ");
		}
		System.out.println(" ");
		System.out.println("x2 vals:");
		for (int n = 0; n<getlistx2().size(); n++){
			System.out.print("index:" + n + " ");
			System.out.print("x2: " + getlistx2().get(n));
			System.out.println(" ");

		}
		System.out.println(" ");
		System.out.println("y2 vals:");
		for (int p = 0; p<getlisty2().size(); p++) {
			System.out.print("index:" + p + " ");
			System.out.print("y2: " + getlisty2().get(p));
			System.out.println(" ");

		}
		System.out.println(" "); 
		System.out.println("possible intersections: ");
		for (int q = 0; q<possible.size(); q++) {
			
			System.out.println(possible.get(q));
		} 
		
		System.out.println("The shortest Manhattan Distance is: " + smallest_md);
	}
} 


