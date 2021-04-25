/*
Create a simplified version of a simulation world - the goal is to implement a thread-safe way to keep track of the status of the objects in the world. Bonus - think about testing ahead of time!

1. Create 2 instances of a new Actor object that contains these following fields:
name (in std::string)
 * location (x, y - longitudinal and latitudinal position)

 2. Implement a “SetLongitudinalVelocity()” method that allows the actor object to travel on the x-axis, updating the actor’s coordinates accordingly.
  * Add unit test for this method 

3. Implement a mechanism to constantly check on the positions of these 2 actors - exit out of the main() loop and throw a customized error if the actor objects collide (x, y coordinate values become the same) * How would you test it?
*/

#include <iostream>
#include <string>

struct Point{
  int x;
  int y;
};

class Actor {
  private:
   std::string name_;
   Point location_;

  public:
   Actor(std::string new_name, Point new_location) : name_(new_name), location_(new_location) {}
   
   std::string getName() const {
     return name_;
   }

   Point getLocation() const {
     return location_;
   }
   
};

int main() {
  Point p1 = {};
  p1.x = 0; 
  p1.y = 0;

  Actor actor1("Tyler", p1);
  std::cout << "Created new actor: " << actor1.getName() << std::endl;
}
