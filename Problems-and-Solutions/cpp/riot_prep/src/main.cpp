#include <iostream>
#include "shape_factory.cpp"
#include "simple_rpc.cpp"
#include "simple_ecs.cpp"

void test_shape_factory() {
    std::cout << "==================== Start ShapeFactory ====================" << std::endl;
    auto rect = ShapeFactory::createRectangle(1.0, 2.0);
    std::cout << "Created Rectangle with area: " << rect->area() << std::endl;
    
    auto circle = ShapeFactory::createCircle(1.5);
    std::cout << "Created circle with area: " << circle->area() << std::endl;
    std::cout << "==================== End ShapeFactory ====================" << std::endl;
}

int test_simple_rpc() {
    std::cout << "==================== Start SimpleRPC ====================" << std::endl;
    Player player_1 = Player("Alice", 100, 15);
    Player player_2 = Player("Bob", 105, 18);
    
    for (int32_t i = 0; i < TIMEOUT_SEC; i++) {
        if (player_1.isDead()) {
            std::cout << player_2.getName() << " wins!" << std::endl;
            return 0;
        }
        else if (player_2.isDead()) {
            std::cout << player_1.getName() << " wins!" << std::endl;
            return 0;
        }
        Combat(player_1, player_2);
        Combat(player_2, player_1);

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "==================== End SimpleRPC ====================" << std::endl;
}

void test_simple_ecs() {
    std::cout << "==================== Start TinyTanks ====================" << std::endl;
    PositionComponentStorage pos_storage;
    VelocityComponentStorage vel_storage;

    std::vector<Entity> entity_list = {1, 2, 3};
    Position p_start = {0.0, 0.0};
    Velocity v_start = {1.0, 0.0};


    for (Entity e : entity_list) {
        pos_storage.Add(p_start, e);
        vel_storage.Add(v_start, e);

        std::thread t1(MovementSystem, std::ref(pos_storage), std::ref(vel_storage), std::vector<Entity>{1});
        std::thread t2(MovementSystem, std::ref(pos_storage), std::ref(vel_storage), std::vector<Entity>{2, 3});

        t1.join();
        t2.join();
    }

    for (Entity e : entity_list) {
        auto pos = pos_storage.Get(e);
        std::cout << "Entity " << e << " final position is: (" << pos->x << " , " << pos->y << ")" << std::endl;
    }

    std::cout << "==================== End TinyTanks ====================" << std::endl;

}

int main() {
    std::cout << "Starting...." << std::endl;
    test_shape_factory();
    test_simple_rpc();
    test_simple_ecs();
    return 0;
}
