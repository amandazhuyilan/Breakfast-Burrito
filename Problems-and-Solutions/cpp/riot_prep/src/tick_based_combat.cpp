#include <chrono>
#include <iostream>
#include <vector>

static const int TICK_RATE_MS = 50;
static const float ATTACK_RANGE = 2.0;

using Entity = uint32_t;

struct PlayerInput {
    // represents player commands (movement/attack).
    Entity id_;
    float dx_;
    float dy_;
    bool attack_;
};

class PlayerState {
    public:
        // stores player position, health, and unique ID.
        Entity id_;
        float x_;
        float y_;
        float health_;

        void applyInput(const PlayerInput input) {
            x_ += input.dx_;
            y_ += input.dy_;
        };

        void print() {
            std::cout << "Player " << id_ << " poistion: " << x_ << " , " << y_ << " , health: " << health_ << " ." << std::endl; 
        };
    };

class GameServer {
    // receives inputs from GameClient
    // runs simulation on fixed ticks
    // broadcasts updated PlayerStates to GameClient
    // The GameServer should process all received inputs each tick.
    private:
        std::unordered_map<Entity, PlayerState> player_states_;
        std::queue<PlayerInput> player_input_queue_;

    public:
        void addNewPlayer(const Entity e) {
            player_states_[e] = PlayerState{e, 0, 0, false};
        };

        void receivePlayerInput(const PlayerInput& input) {
            player_input_queue_.push(input);
        };

        void tick() {
            while (!player_input_queue_.empty()) {
                PlayerInput front_input = player_input_queue_.front();
                player_input_queue_.pop();

                if (player_states_.find(front_input.id_) != player_states_.end()) {
                    player_states_[front_input.id_].applyInput(front_input);
                }
            }

            broadcastState();
            }
        };

        void broadcastState() {
            for (auto &[id, state] : player_states_) {
                state.print();
            }
        };

        void run() {
            for (int i; i < 10; i++) {
                tick();
                std::this_thread::sleep_for(std::chono::miliseconds(100));
            }
        };

        const std::unordered_map<Entity, PlayerState>& getStates() const {
            return player_states;
        };

};

class GameClient {
    private:
        Entity id_;
    public:
        GameClient(const Entity e) : id_ (e) {};
        PlayerInput createInput(Entity e) {
            return PlayerInput{e, 0.0, 0.0, false};
        };
        void receiveState() {};
    // sends PlayerInputs from GameServer
    // receives PlayerStates from GameServer, 
    // bonus: performs client-side interpolation between server snapshots.
};

int main() {
    GameServer server;
    server.addNewPlayer(1);
    server.addNewPlayer(2);

    GameClient client1(1);
    GameClient client2(2);

    // Simulate client input and server ticks
    for (int tick = 0; tick < 10; ++tick) {
        server.receiveInput(client1.createInput(0.5f, 0.1f, false));
        server.receiveInput(client2.createInput(-0.3f, 0.2f, false));

        server.tick();

        // Clients receive state snapshot
        auto allStates = server.getStates();
        client1.receiveState(allStates.at(1));
        client2.receiveState(allStates.at(2));

        // // Simulate interpolation
        // client1.displayInterpolated(0.5f);
        // client2.displayInterpolated(0.5f);

        std::this_thread::sleep_for(std::chrono::milliseconds(50));
    }

    return 0;
}
