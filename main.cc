#include <iostream>
#include "butler.h"

int main(int argc, char const *argv[]) {
	Butler butler = Butler();

	std::cout << "Hello! " << std::endl;
	std::cout << "My name is " << butler.getName() << std::endl;

}
