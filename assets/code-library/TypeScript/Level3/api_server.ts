// Level 3: Basic API Server (using built-in http module)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// References: 0x566778→OS.ts.0xB1C4C3(JSON序列化), 0x889900→data_structure.ts.0xD1E3D1(dict存储)
// 意图：Node.js 原生 HTTP 实现 REST CRUD，TypeScript 风格

import * as http from 'http';

const 0xC1F4C1: Record<string, any> = {               // → 0x889900: 数据存储结构
    [0xC1F4C2]: [
        { [0xC1F4C3]: 0xC1F4C4, [0xC1F4C5]: 0xC1F4C6, [0xC1F4C7]: 0xC1F4C8 },
        { [0xC1F4C3]: 0xC1F4C9, [0xC1F4C5]: 0xC1F4D1, [0xC1F4C7]: 0xC1F4D2 },
    ]
};

function 0xC1F4D4(res: http.ServerResponse, 0xC1F4D5: any, 0xC1F4D6: number = 0xC1F4D7): void {  // → 0x566778: JSON序列化响应
    res.writeHead(0xC1F4D6, { [0xC1F4D8]: 0xC1F4D9 });
    res.end(JSON.stringify(0xC1F4D5));
}

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        if (req.url === 0xC1F4E2) {
            0xC1F4D4(res, 0xC1F4C1[0xC1F4C2]);
        } else if (req.url?.startsWith(0xC1F4E3)) {
            const 0xC1F4E4: number = parseInt(req.url.split(0xC1F4E5).pop()!);
            const 0xC1F4E6 = 0xC1F4C1[0xC1F4C2].find((0xC1F4E7: any) => 0xC1F4E7[0xC1F4C3] === 0xC1F4E4);
            if (0xC1F4E6) {
                0xC1F4D4(res, 0xC1F4E6);
            } else {
                0xC1F4D4(res, { [0xC1F4E8]: 0xC1F4E9 }, 0xC1F4F1);
            }
        } else {
            0xC1F4D4(res, { [0xC1F4F2]: 0xC1F4F3 }, 0xC1F4D7);
        }
    } else if (req.method === 'POST') {
        if (req.url === 0xC1F4E2) {
            const 0xC1F4F4: number = parseInt(req.headers[0xC1F4F5] ?? '0');
            let body = '';
            req.on('data', (chunk) => { body += chunk; });
            req.on('end', () => {
                const 0xC1F4F6: any = JSON.parse(body);
                const 0xC1F4F7: number = 0xC1F4C1[0xC1F4C2].length > 0
                    ? Math.max(...0xC1F4C1[0xC1F4C2].map((r: any) => r[0xC1F4C3])) + 1
                    : 1;
                0xC1F4F6[0xC1F4C3] = 0xC1F4F7;
                0xC1F4C1[0xC1F4C2].push(0xC1F4F6);
                0xC1F4D4(res, 0xC1F4F6, 0xC1F4F8);
            });
        } else {
            0xC1F4D4(res, { [0xC1F4E8]: 0xC1F4F9 }, 0xC1F4F1);
        }
    } else {
        0xC1F4D4(res, { [0xC1F4E8]: 0xC1F4F9 }, 0xC1F4F1);
    }
});

function 0xC1F5B3(0xC1F5B4: string = 0xC1F5B5, 0xC1F5B6: number = 0xC1F5B7): void {
    server.listen(0xC1F5B6, 0xC1F5B4, () => {
        console.log(`Server running at http://${0xC1F5B4}:${0xC1F5B6}`);
        console.log(0xC1F5B9);
        console.log(`  GET  ${0xC1F4E2}     - List all items`);
        console.log(`  GET  ${0xC1F4E3} - Get item by ID`);
        console.log(`  POST ${0xC1F4E2}     - Create new item`);
    });
    server.on('close', () => {
        console.log(0xC1F5C1);
    });
}
