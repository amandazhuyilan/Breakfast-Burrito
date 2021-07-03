#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct channel {
    std::string name;
    std::vector<int> sub_list;
};

// Definition of PushNotification
class PushNotification {
    public:
        void static notify(int user_id, std::string message) {
            std::cout << "user " << user_id << " received: '" << message << "'" << std::endl;
        }
};

class PubSubPattern {
public:
    std::vector<channel> channel_list_;

	PubSubPattern() {
		// initialize your data structure here.
	}

	/**
	* @param channel:
	* @param user_id:
	* @return: nothing
	*/
	void subscribe(std::string &channel, int user_id) {
		// subscribes new users to existing channels
        // if channel doesn't exist, create new channel with new user
        // if channel exists but user doesn't, add new user into channel
        // if channel exists and user also exists in channel, do nothing
        for (auto channel_list_it = channel_list_.begin(); channel_list_it != channel_list_.end(); channel_list_it++) {
            if (channel_list_it->name == channel) {
                auto user_id_list_it = std::find(channel_list_it->sub_list.begin(), channel_list_it->sub_list.end(), user_id);
                if (user_id_list_it != channel_list_it->sub_list.end()) {
                    // user_id is already subscribing to the channel
                    std::cout << "user " << user_id << " already subscribed to " << channel << std::endl;
                    return;
                } else {
                    channel_list_it->sub_list.push_back(user_id);
                    std::cout << "new user " << user_id << " added into " << channel <<std::endl;
                    return;
                }
            }
        }

        // no existing channel found in channel_list_
        struct channel new_channel;
        std::vector<int> new_user_id_list = {user_id};
        new_channel.name = channel;
        new_channel.sub_list = new_user_id_list;
        channel_list_.push_back(new_channel);
        std::cout << "new channel " << channel << " created with user " << user_id <<std::endl;
	}

	/**
	* @param channel:
	* @param user_id:
	* @return: nothing
	*/
	void unsubscribe(std::string &channel, int user_id) {
        for (auto channel_list_it = channel_list_.begin(); channel_list_it != channel_list_.end(); channel_list_it++) {
            if (channel_list_it->name == channel) {
                auto user_id_list_it = std::find(channel_list_it->sub_list.begin(), channel_list_it->sub_list.end(), user_id);
                if (user_id_list_it != channel_list_it->sub_list.end()) {
                    channel_list_it->sub_list.erase(user_id_list_it);
                    std::cout << "user " << user_id << " has been unsubscribed from " << channel << std::endl;
                    return;
                } else {
                    std::cout << "no user " << user_id << " found in " << channel <<std::endl;
                    return;
                }
            }
        }
        std::cout << "channel " << channel << "does not exist" <<std::endl;
    }

	/**
	* @param channel:
	* @param message:
	* @return: nothing
	*/
	void publish(std::string &channel, std::string &message) {
        for (auto channel_list_it = channel_list_.begin(); channel_list_it != channel_list_.end(); channel_list_it++) {
            PushNotification pn = PushNotification();
            if (channel_list_it->name == channel) {
                for (std::vector<int>::iterator sub_list_it = channel_list_it->sub_list.begin(); sub_list_it != channel_list_it->sub_list.end(); sub_list_it++) {
                    pn.notify(*sub_list_it, message);
                }
                return;
                } else {
                    std::cout << "channel " << channel << " does not exist to publish message" <<std::endl;
                    return;
                }
            }
        }
};

int main() {
    PubSubPattern test_pub_sub = PubSubPattern();
    std::string group_1_str = "group_1";
    std::string group_2_str = "group_2";
    std::string publish_msg_1 = "hello";

    test_pub_sub.subscribe(group_1_str, 1);
    test_pub_sub.subscribe(group_2_str, 1);
    test_pub_sub.subscribe(group_2_str, 2);

    test_pub_sub.unsubscribe(group_2_str, 2);
    test_pub_sub.publish(group_1_str, publish_msg_1);

    return 0;
}