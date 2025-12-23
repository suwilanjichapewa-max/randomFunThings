package lab_quiz;

	class Vehicle {
	private String licensePlate ="ABC 6969 "; 
	protected double rentalCostperDay = 60;
	
	void calculateRentalCost(int days) {
		
		System.out.println("Rental cost for " + licensePlate + ":" + rentalCostperDay * days);	
		
	}

	class Car extends Vehicle{
	boolean isElectric;
	
	}



class Truck extends Vehicle{
	protected double loadCapacity;
	String licensePlate ="ABC 6999"; 
	
	void calculateRentalCost() {
		System.out.println("Surcharge for " + ":" + super.licensePlate  + rentalCostperDay * loadCapacity);
	}
	
}

}