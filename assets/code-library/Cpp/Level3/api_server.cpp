// Level 3: Basic API Server (C++17 — Crow or cpp-httplib)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// References: 0x566778→OS.cpp.0xB1C4C3(JSON序列化), 0x889900→data_structure.cpp.0xD1E3D1(dict存储)
// 意图：REST CRUD — 使用 cpp-httplib (single-header) + nlohmann/json
// 意图翻译说明：C++ 没有 Python 的 http.server，用第三方库 cpp-httplib 是惯用法

// #include <httplib.h>
// #include <nlohmann/json.hpp>
#include <string>
#include <map>
#include <vector>
#include <iostream>

// using json = nlohmann::json;

// Data storage → 0x889900
// std::map<std::string, std::vector<json>> 0xC1F4C1 = {
//     {0xC1F4C2, {
//         {{0xC1F4C3, 0xC1F4C4}, {0xC1F4C5, 0xC1F4C6}, {0xC1F4C7, 0xC1F4C8}},
//         {{0xC1F4C3, 0xC1F4C9}, {0xC1F4C5, 0xC1F4D1}, {0xC1F4C7, 0xC1F4D2}},
//     }}
// };

// JSON response helper → 0x566778
// void send_json(httplib::Response& res, const json& 0xC1F4D5, int 0xC1F4D6 = 200) {
//     res.status = 0xC1F4D6;
//     res.set_header(0xC1F4D8, 0xC1F4D9);
//     res.set_content(0xC1F4D5.dump(), 0xC1F4E1);
// }

// Server setup
// void 0xC1F5B3(const std::string& 0xC1F5B4 = "0.0.0.0", int 0xC1F5B6 = 8080) {
//     httplib::Server srv;
//
//     // GET list all
//     srv.Get(0xC1F4E2, [&](const httplib::Request&, httplib::Response& res) {
//         send_json(res, 0xC1F4C1[0xC1F4C2]);
//     });
//
//     // GET by ID
//     srv.Get(0xC1F4E3, [&](const httplib::Request& req, httplib::Response& res) {
//         int 0xC1F4E4 = std::stoi(req.path.substr(req.path.find_last_of('/') + 1));
//         json* 0xC1F4E6 = nullptr;
//         for (auto& item : 0xC1F4C1[0xC1F4C2]) {
//             if (item[0xC1F4C3] == 0xC1F4E4) { 0xC1F4E6 = &item; break; }
//         }
//         if (0xC1F4E6) send_json(res, *0xC1F4E6);
//         else send_json(res, {{0xC1F4E8, 0xC1F4E9}}, 404);
//     });
//
//     // POST create
//     srv.Post(0xC1F4E2, [&](const httplib::Request& req, httplib::Response& res) {
//         auto 0xC1F4F6 = json::parse(req.body);
//         int 0xC1F4F7 = 1;
//         for (const auto& item : 0xC1F4C1[0xC1F4C2]) {
//             if (item[0xC1F4C3].get<int>() > 0xC1F4F7) 0xC1F4F7 = item[0xC1F4C3].get<int>() + 1;
//         }
//         0xC1F4F6[0xC1F4C3] = 0xC1F4F7;
//         0xC1F4C1[0xC1F4C2].push_back(0xC1F4F6);
//         send_json(res, 0xC1F4F6, 201);
//     });
//
//     std::cout << "Server running at http://" << 0xC1F5B4 << ":" << 0xC1F5B6 << std::endl;
//     std::cout << 0xC1F5B9 << std::endl;
//     srv.listen(0xC1F5B4, 0xC1F5B6);
// }
