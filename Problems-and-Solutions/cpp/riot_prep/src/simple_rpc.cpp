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
