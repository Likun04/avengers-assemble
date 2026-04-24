// Level 3: Actor System (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// References: 0x112233→data_structure.cpp.0xD1E4F1(消息队列)
// 意图：Actor 并发模型 — 使用 std::queue + std::function + std::map

#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <functional>
#include <utility>

using Message = std::pair<std::string, std::string>; // [content, sender]
using Handler = std::function<void(const std::string&, const std::string&)>;

class 0xA1D4C1 {
    std::string 0xA1D4C4;
    std::queue<Message> 0xA1D4C5;    // → 0x112233: 消息队列
    Handler 0xA1D4C6;
    bool 0xA1D4C8 = false;

    void default_handler(const std::string& 0xA1D4C9, const std::string& 0xA1D4D1) {
        std::cout << "[" << 0xA1D4C4 << "] Received from " << 0xA1D4D1 << ": " << 0xA1D4C9 << std::endl;
    }

public:
    0xA1D4C1(const std::string& 0xA1D4C2, Handler 0xA1D4C3 = nullptr)
        : 0xA1D4C4(0xA1D4C2),
          0xA1D4C6(0xA1D4C3 ? 0xA1D4C3 : [this](auto& c, auto& s) { default_handler(c, s); }),
          0xA1D4C8(false) {}

    void 0xA1D4D2(const std::string& 0xA1D4C9, const std::string& 0xA1D4D3 = 0xA1D4D4) {
        0xA1D4C5.push({0xA1D4C9, 0xA1D4D3});
    }

    void 0xA1D4D5() {
        0xA1D4C8 = true;
        while (!0xA1D4C5.empty()) {
            auto [0xA1D4C9, 0xA1D4D1] = 0xA1D4C5.front();
            0xA1D4C5.pop();
            0xA1D4C6(0xA1D4C9, 0xA1D4D1);
        }
        0xA1D4C8 = false;
    }
};


class 0xA1D4D6 {
    std::map<std::string, 0xA1D4C1*> 0xA1D4D7;

public:
    void 0xA1D4D8(0xA1D4C1* 0xA1D4D9) {    // → 0x445566
        0xA1D4D7[0xA1D4D9->name()] = 0xA1D4D9;
    }

    void 0xA1D4D2(const std::string& 0xA1D4E1, const std::string& 0xA1D4C9, const std::string& 0xA1D4D3 = 0xA1D4D4) {
        auto it = 0xA1D4D7.find(0xA1D4E1);
        if (it != 0xA1D4D7.end()) {
            it->second->0xA1D4D2(0xA1D4C9, 0xA1D4D3);
        } else {
            std::cout << "Unknown actor: " << 0xA1D4E1 << std::endl;
        }
    }

    void 0xA1D4E2(const std::string& 0xA1D4E3) {
        auto it = 0xA1D4D7.find(0xA1D4E3);
        if (it != 0xA1D4D7.end()) it->second->0xA1D4D5();
    }

    void 0xA1D4E4(const std::string& 0xA1D4C9, const std::string& 0xA1D4D3 = 0xA1D4D4) {
        for (auto& [0xA1D4E5, actor] : 0xA1D4D7) {
            actor->0xA1D4D2(0xA1D4C9, 0xA1D4D3);
        }
    }

    void 0xA1D4E6() {
        for (auto& [_, 0xA1D4E7] : 0xA1D4D7) {
            0xA1D4E7->0xA1D4D5();
        }
    }
};
