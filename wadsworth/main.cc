#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include "butler.h"

int main(int argc, char const *argv[]) {
	static bool KILLSWITCH = false;
	std::string input = "";

	Butler butler = Butler();

	std::cout << "Hello and welcome to your virtual butler!" << std::endl;
	std::cout << "What would you like to name your butler?";
	std::cin >> input;

	// Standard butler template
	if(input == "Wadsworth"){
		butler.setName("Wadsworth");
		std::cout << "Good choice! Wadsworth is our standard (and frankly most basic) Butler" << std::endl;
	}

	// Butler template for the fancier folk
	else if(input == "Allister"){
		butler.setName("Allister");
		std::cout << "Aha! I can see one seeks the finer things in life" << std::endl;
	}

	// Coolest butler template
	else if(input == "Brad"){
		butler.setName("Brad");
		std::cout << "Sup dude, name's Brad"<< std::endl;
	}

	// Any other name will default to wadsworth
	else {
		butler.setName("Wadsworth");
		std::cout << "What a unique name!";
	}

	while(! KILLSWITCH){
		input = "";
		std::cout << "For a list of commands, enter \'c\'. Else, enter \'q\' to quit" << std::endl;
		std::cout << ">> ";
		std::cin >> input;

		if(input == "c" || input == "C"){
			std::cout << "Generic Commands (Static Regardless of Butler Type):" << std::endl;
			std::cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << std::endl;

			std::cout << "weather -> opens weather app using default browser" << std::endl;
			std::cout << "clear -> clears terminal window";
		}

		if(input == "q" || input == "Q"){
			std::cout << "Goodbye!" << std::endl;
			KILLSWITCH = true;
			break;
		}

		if(input == "clear"){
			system("scripts/clearscreen.sh");
		}
	}

	if( ! KILLSWITCH){
		std::cout << "Hello! " << std::endl;
		std::cout << "My name is " << butler.getName() << std::endl;
	}


}
