#include <iostream>
#include <memory>
#include <mutex>
#include <optional>

struct Position {float x, y;};
struct Velocity {float dx, dy;};
using Entity = uint32_t;

class PositionComponentStorage {
    public:
        void Add(const Position& p, Entity e) {
        // adds a new position component in the position_map_
            std::lock_guard<std::mutex> lock(position_mutex_);
            position_map_[e] = p;
        };
    
        bool Update(const Position& new_p, Entity e) {
            // updates the position of the entity in the position_map_
            // return True if successful
            std::lock_guard<std::mutex> lock(position_mutex_);                
            auto found_position = position_map_.find(e);
            if (found_position != position_map_.end()) {
                found_position->second = new_p;
                return true;
            } else {
                return false;
            }
        };

        std::optional<Position> Get(Entity e) {
            // get the position of the requested Entity
            std::lock_guard<std::mutex> lock(position_mutex_);
            return position_map_[e];
        }
    private:
        std::mutex position_mutex_;
        std::unordered_map<Entity, Position> position_map_;
        
};

class VelocityComponentStorage {
    public:
        void Add(const Entity e, Velocity v) {
            std::lock_guard<std::mutex> lock(velocity_mutex_);
            velocity_map_[e] = v;
        };

        std::optional<Velocity> Get(Entity e) {
            std::lock_guard<std::mutex> lock(velocity_mutex);
            auto it = velocity_map_.find(e);
            if (it != velocity_map_.end()) {
                return it->second;
            } else {
                return std::nullopt;
            }
        }
    
        private:
            std::mutex velocity_mutex_;
            std::unordered_map<Entity, Velocity> velocity_map_;

};

void MovementSystem(PositionComponentStorage&, VelocityComponentStorage&, const std::vector<Entity>&) {
    // iterate through all entities in the vector
    // update the positions and the velocity
};


int main() {

}