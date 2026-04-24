# Level 3: Basic API Server (using built-in http.server)
# Interface: 0xC1D2E3=input(主机地址), 0xF4A5B6=input(端口), 0xB7C8D9=input-output(数据源)
# References: 0x566778→Level1/OS.py(JSON序列化), 0x889900→Level1/data_structure.py(数据存储)

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

database = {                    # 0x889900: 数据存储结构
    "items": [
        {"id": 1, "name": "Apple", "price": 3.5},
        {"id": 2, "name": "Banana", "price": 2.0},
    ]
}

class APIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):    # 0x566778: JSON序列化响应
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path == "/items":
            self._send_json(database["items"])
        elif self.path.startswith("/items/"):
            item_id = int(self.path.split("/")[-1])
            item = next((i for i in database["items"] if i["id"] == item_id), None)
            if item:
                self._send_json(item)
            else:
                self._send_json({"error": "Not found"}, status=404)
        else:
            self._send_json({"message": "API is running. Try /items"}, status=200)

    def do_POST(self):
        if self.path == "/items":
            content_length = int(self.headers["Content-Length"])
            body = json.loads(self.rfile.read(content_length))
            new_id = max(i["id"] for i in database["items"]) + 1 if database["items"] else 1
            body["id"] = new_id
            database["items"].append(body)
            self._send_json(body, status=201)
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

    def log_message(self, format, *args):
        print(f"[API] {args[0]}")


def run_server(0xC1D2E3="localhost", 0xF4A5B6=8080):
    server = HTTPServer((0xC1D2E3, 0xF4A5B6), APIHandler)
    print(f"Server running at http://{0xC1D2E3}:{0xF4A5B6}")
    print("Endpoints:")
    print("  GET  /items     - List all items")
    print("  GET  /items/<id> - Get item by ID")
    print("  POST /items     - Create new item")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
