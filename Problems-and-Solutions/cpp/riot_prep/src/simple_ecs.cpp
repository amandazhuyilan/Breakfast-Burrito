#include <iostream>
#include <memory>
#include <mutex>
#include <optional>
#include <thread>

struct Position {float x, y;};
struct Velocity {float dx, dy;};
using Entity = uint32_t;

class PositionComponentStorage {
    public:
        void Add(const Position& p, Entity& e) {
        // adds a new position component in the position_map_
            std::lock_guard<std::mutex> lock(position_mutex_);
            position_map_[e] = p;
        };
    
        bool Update(const Position& new_p, Entity& e) {
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

        std::optional<Position> Get(Entity& e) {
            // get the position of the requested Entity
            std::lock_guard<std::mutex> lock(position_mutex_);
            return position_map_[e];
        }
    private:
        std::mutex position_mutex_;
        std::unordered_map<Entity, Position> position_map_;
        
};

class VelocityComponentStorage {
    private:
        std::mutex velocity_mutex_;
        std::unordered_map<Entity, Velocity> velocity_map_;
    
        public:
        void Add(Velocity v, const Entity e) {
            std::lock_guard<std::mutex> lock(velocity_mutex_);
            velocity_map_[e] = v;
        };

        std::optional<Velocity> Get(Entity e) {
            std::lock_guard<std::mutex> lock(velocity_mutex_);
            auto it = velocity_map_.find(e);
            if (it != velocity_map_.end()) {
                return it->second;
            } else {
                return std::nullopt;
            }
        }

};

void MovementSystem(PositionComponentStorage& position_store, VelocityComponentStorage& velocity_store, const std::vector<Entity>& e) {
    // iterate through all entities in the vector
    // update the positions
    for (Entity ent : e) {
        auto current_pos = position_store.Get(ent);
        auto current_vel = velocity_store.Get(ent);

        if (current_pos && current_vel) {
            Position new_pos = *current_pos;
            new_pos.x += current_vel->dx;
            new_pos.y += current_vel->dy;
            position_store.Update(new_pos, ent);
        }
    }
};


// int main() {
//     PositionComponentStorage pos_storage;
//     VelocityComponentStorage vel_storage;

//     std::vector<Entity> entity_list = {1, 2, 3};
//     Position p_start = {0.0, 0.0};
//     Velocity v_start = {1.0, 0.0};


//     for (Entity e : entity_list) {
//         pos_storage.Add(p_start, e);
//         vel_storage.Add(v_start, e);

//         std::thread t1(MovementSystem, std::ref(pos_storage), std::ref(vel_storage), std::vector<Entity>{1});
//         std::thread t2(MovementSystem, std::ref(pos_storage), std::ref(vel_storage), std::vector<Entity>{2, 3});

//         t1.join();
//         t2.join();

//         for (Entity ent : e) {
//             auto pos = pos_storage.Get(e);
//             std::cout << "Entity " << e << " final position is: (" << pos->x << " , " << pos->y << std::endl;
//         }

//     }
// }