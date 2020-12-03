import java.util.*;
public class Wire {
	private boolean[][] pos; 
	private int posx;
	private int  posy;
	private static int startx;
	private static int starty; 
	private ArrayList<String> subs;
	public Wire (ArrayList<String> s, int x, int y) {
		posx = 25000;
		posy = 25000;
		subs = s; 
		startx = 12500;
		starty = 12500;
		
			
	}
	public boolean[][] getPos() {
		return pos; 
	}
	public static int getStartx() {
		return startx; 
	}
	public static int getStarty() {
		return starty;
	}
	public int getX() {
		return posx; 
	}
	public int getY() {
		return posy;
	}
	public void  builder () {
	/* builder takes an arraylist of strings and uses them to create a 2d boolean array indicating
	the positions of the wire IN ALL FOUR QUADRENTS*/
		pos = new boolean[posx][posy];
		//sets pos equal to false at every point
		for (int a =0; a<posx; a++) {
			for (int b =0; b<posy; b++) {
				pos[a][b] = false;
			}
		}
		int x = startx;
		int y = starty;
		int step = 0; 
		//inscribes the position of the wire into the 2d boolean array pos
		for (int i =0; i<subs.size(); i++) {
			if (subs.get(i).charAt(0) == 'L') {
				int val = -1 * Integer.valueOf(subs.get(i).substring(1));
				for (int j = x; j>= x + val; j--) {
					pos[j][y] = true;
					//System.out.println("pos[" + j +"][" + y +"]= "+  pos[j][y]);  
				}
				x += val;
			}
			else if (subs.get(i).charAt(0) == 'R') {
				int val = Integer.valueOf(subs.get(i).substring(1));
				for (int j = x; j<= x + val; j++) {
					pos[j][y] = true; 
					//System.out.println("pos[" + j +"][" + y +"]= "+  pos[j][y]); 
				}
				x += val;
			}
			else if(subs.get(i).charAt(0) == 'U') {
				int val = Integer.valueOf(subs.get(i).substring(1));
				for (int j = y ; j <= y +val; j ++) {
					pos[x][j] = true;
					//System.out.println("pos[" + x +"][" + j +"]= "+  pos[x][j]); 
				}
				y += val; 
			}
			else if (subs.get(i).charAt(0) == 'D'){ 
				int val = -1 *Integer.valueOf(subs.get(i).substring(1));
				for (int j =y; j >= y + val; j--) {
					pos[x][j] = true;
					//System.out.println("pos[" + x +"][" + j +"]= "+  pos[x][j]); 
				}
				y +=val; 
			} 
		}
		
	}
}
