package robotMaze;

import lejos.nxt.Button;

public class myclass {
	
	public final static int STD_SPEED = 240 ; 
	public final static int STD_STEP = 40 ; 
	
    /**
     * 
     * @param args
     */
    public static void main(String[] args) {
        System.out.println("Here we go !");
        Button.waitForAnyPress();
        
        Robot robot = new Robot();
        robot.forward(3);
        robot.turnRight();
        robot.forward(1);
        robot.turnLeft();
        robot.forward(1);
        robot.uturn();
        robot.forward(3);
        
        System.out.println("Okay, I'm done ! ");
        Button.waitForAnyPress();
    }
}