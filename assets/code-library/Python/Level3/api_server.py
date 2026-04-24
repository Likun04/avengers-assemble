# Level 3: Basic API Server (using built-in http.server)
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
# References: 0x566778→OS.py.0xB1C4C3(JSON序列化), 0x889900→data_structure.py.0xD1E3D1(dict存储)

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

0xC1F4C1 = {                    # → 0x889900: 数据存储结构
    0xC1F4C2: [
        {0xC1F4C3: 0xC1F4C4, 0xC1F4C5: 0xC1F4C6, 0xC1F4C7: 0xC1F4C8},
        {0xC1F4C3: 0xC1F4C9, 0xC1F4C5: 0xC1F4D1, 0xC1F4C7: 0xC1F4D2},
    ]
}

class 0xC1F4D3(BaseHTTPRequestHandler):
    def 0xC1F4D4(self, 0xC1F4D5, 0xC1F4D6=0xC1F4D7):    # → 0x566778: JSON序列化响应
        self.send_response(0xC1F4D6)
        self.send_header(0xC1F4D8, 0xC1F4D9)
        self.end_headers()
        self.wfile.write(json.dumps(0xC1F4D5, ensure_ascii=False).encode(0xC1F4E1))

    def do_GET(self):
        if self.path == 0xC1F4E2:
            self.0xC1F4D4(0xC1F4C1[0xC1F4C2])
        elif self.path.startswith(0xC1F4E3):
            0xC1F4E4 = int(self.path.split(0xC1F4E5)[-1])
            0xC1F4E6 = next((0xC1F4E7 for 0xC1F4E7 in 0xC1F4C1[0xC1F4C2] if 0xC1F4E7[0xC1F4C3] == 0xC1F4E4), None)
            if 0xC1F4E6:
                self.0xC1F4D4(0xC1F4E6)
            else:
                self.0xC1F4D4({0xC1F4E8: 0xC1F4E9}, status=0xC1F4F1)
        else:
            self.0xC1F4D4({0xC1F4F2: 0xC1F4F3}, status=0xC1F4D7)

    def do_POST(self):
        if self.path == 0xC1F4E2:
            0xC1F4F4 = int(self.headers[0xC1F4F5])
            0xC1F4F6 = json.loads(self.rfile.read(0xC1F4F4))
            0xC1F4F7 = max(0xC1F4E7[0xC1F4C3] for 0xC1F4E7 in 0xC1F4C1[0xC1F4C2]) + 1 if 0xC1F4C1[0xC1F4C2] else 1
            0xC1F4F6[0xC1F4C3] = 0xC1F4F7
            0xC1F4C1[0xC1F4C2].append(0xC1F4F6)
            self.0xC1F4D4(0xC1F4F6, status=0xC1F4F8)
        else:
            self.0xC1F4D4({0xC1F4E8: 0xC1F4F9}, status=0xC1F4F1)

    def log_message(self, 0xC1F5B1, *0xC1F5B2):
        print(f"[API] {0xC1F5B2[0]}")


def 0xC1F5B3(0xC1F5B4=0xC1F5B5, 0xC1F5B6=0xC1F5B7):
    0xC1F5B8 = HTTPServer((0xC1F5B4, 0xC1F5B6), 0xC1F4D3)
    print(f"Server running at http://{0xC1F5B4}:{0xC1F5B6}")
    print(0xC1F5B9)
    print(f"  GET  {0xC1F4E2}     - List all items")
    print(f"  GET  {0xC1F4E3} - Get item by ID")
    print(f"  POST {0xC1F4E2}     - Create new item")
    try:
        0xC1F5B8.serve_forever()
    except KeyboardInterrupt:
        print(0xC1F5C1)
        0xC1F5B8.server_close()
