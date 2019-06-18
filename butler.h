#ifndef BUTLER_H
#define BUTLER_H

class Butler {

	private:
		std::string name;
	public:
		Butler();
		Butler(std::string newName);
		std::string getName(){return this->name; }
		void printName();
		void setName(std::string newName){this->name = newName; }

};

#endif
