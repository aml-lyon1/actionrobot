package robotMaze;

import lejos.hardware.port.MotorPort;
import lejos.hardware.port.Port;

public class myclass {
	
	public final static int STD_SPEED = 240 ; 
	public final static int STD_STEP = 40 ;
	public final static Port leftP =  MotorPort.D ; 
	public final static Port rightP = MotorPort.A ; 
	public final static int STD_TIME = 1000; 
	
	
    /**
     * 
     * @param args
     */
    public static void main(String[] args) {
        System.out.println("Here we go !");
        
        Robot robot = new Robot();
        robot.forward(1);
        robot.backward(1);
        robot.turnLeft(1);
        robot.turnRight(1);
        //robot.uturn();
    }
}