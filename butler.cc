#include <iostream>
#include <ctime>	// For time()
#include <cstdlib> 	// For srand() and rand()
#include "butler.h"

Butler::Butler(){
	this->name = "Wadsworth";
}

Butler::Butler(std::string newName){
	this->name = newName;
}

void Butler::printName(){
	std::cout << this->getName() << std::endl;
}


