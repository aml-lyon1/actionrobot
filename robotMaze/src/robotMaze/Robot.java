package robotMaze;

public class Robot {
	
	int step ; 
	int speed ; 
	
	/**
	 * Instantiate a robot with standard speed and step as defined in main class.
	 */
	public Robot() {	
		this.step = myclass.STD_STEP ; 
		this.speed = myclass.STD_SPEED ; 
	}
	
	/**
	 * Instantiate a robot with speed and step as specified by the developer.
	 * @param step
	 * @param speed
	 */
	public Robot(int step, int speed) {
		this.step = step; 
		this.speed = speed; 
	}

	/**
	 * To get the step of the robot. 
	 * 
	 * @return step 
	 */
	public int getStep() {
		return step;
	}

	/**
	 * To set the step of the robot. 
	 * 
	 * @param step
	 */
	public void setStep(int step) {
		this.step = step;
	}

	/**
	 * To get the speed of the robot.
	 * 
	 * @return speed
	 */
	public int getSpeed() {
		return speed;
	}

	/**
	 * To get the speed of the robot. 
	 * 
	 * @param speed
	 */
	public void setSpeed(int speed) {
		this.speed = speed;
	}
	
	/** 
	 * Make the robot move forward 
	 * 
	 * @param nbCase
	 */
	public void forward(int nbCase) {
		for(int i=0; i<nbCase; i++) {
			//TODO move i*step 
		}
	}
	
	/** 
	 * Make the robot move backward 
	 * 
	 * @param nbCase
	 */
	public void backward(int nbCase) {
		for(int i=0; i<nbCase; i++) {
			//TODO move i*step
		}
	}
	
	/**
	 * Make the robot turn right, without moving forward 
	 * 
	 */
	public void turnRight() {
		//TODO  
	}

	/** 
	 * Make the robot turn left, without moving forward
	 */
	public void turnLeft() {
		//TODO 
	}
	
	/**
	 * The robot makes a Uturn, without moving forward 
	 */
	public void uturn() {
		//TODO  
	}
	
}
