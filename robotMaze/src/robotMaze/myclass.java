package robotMaze;

import lejos.hardware.port.MotorPort;
import lejos.hardware.port.Port;

public class myclass {
	
	public final static int STD_SPEED = 240 ; 
	public final static int STD_STEP = 40 ; // TODO penser à changer en cm de case
	public final static Port leftP =  MotorPort.D ; 
	public final static Port rightP = MotorPort.A ; 
	public final static int STD_TIME = 1000; 
	
	
    /**
     * 
     * @param args
     */
    public static void main(String[] args) {
        System.out.println("Here we go !");
        //Button.waitForAnyPress();
        /*
        Robot robot = new Robot();
        robot.forward(3);
        robot.turnRight();
        robot.forward(1);
        robot.turnLeft();
        robot.forward(1);
        robot.uturn();
        robot.forward(3);
        */
        System.out.println("Okay, I'm done ! ");
        //Button.waitForAnyPress();
    }
}