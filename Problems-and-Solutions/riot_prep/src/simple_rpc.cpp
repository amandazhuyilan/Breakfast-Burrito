#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <vector>

const int32_t TIMEOUT_SEC = 1000;

class Player {
    private:
        std::string name_;
        int32_t health_;
        int32_t attack_power_;

    public:
        Player(std::string n, int32_t h, int32_t a) : name_(n), health_(h), attack_power_(a) {};
        std::string getName() const {
            return name_;
        }

        int32_t getHealth() const {
            return std::max(health_, 0);
        }

        int32_t getAttackPower() const {
            return attack_power_;
        }

        void getAttackedby(const int32_t attack_power) {
            health_ = health_ - attack_power;
        }

        const bool isDead() {
            return (health_ <= 0);
        }
};

void Combat(Player& attacker, Player& defender) {
    defender.getAttackedby(attacker.getAttackPower());
    std::cout << attacker.getName() << " attacks " << defender.getName() << " for " << attacker.getAttackPower() << " damage. " << defender.getName() << " has " << defender.getHealth() << " left." << std::endl;
}

int main() {
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
}
