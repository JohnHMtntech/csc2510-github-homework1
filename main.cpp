#include<stdio.h> // look im so quirky i don't use cout
#include<string>
#include<ctime>
#include<cstdlib>

int fightClub();
char const* funcVandergriff();


int main() { 
  printf("Welcome to your pull request homework!\n");

  
  int winner = fightClub();

  printf("STUDENT NUMBER %d IS THE WINNER OF FIGHT CLUB\n", winner);
 
  // thank you c++11 for not taking a string
  // and taking a disgusting char const*
  char const* coolestAnimal = funcVandergriff();
  printf("%s are the coolest animal. \n\n",  coolestAnimal);

  return 0;
} 

int fightClub() {
  srand(time(0));

  // i think there's like 20 of us in the class
  return rand() % 20; 
}

char const* funcVandergriff() { 
  return "horse";
}
