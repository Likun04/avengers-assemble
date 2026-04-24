// Level 3: Actor System
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// References: 0x112233→data_structure.ts.0xD1E4F1(消息队列)
// 意图：Actor 并发模型 — 消息队列、Actor注册、广播，TypeScript 类实现

type Message = [any, string]; // [content, sender]
type Handler = (content: any, sender: string) => void;

class 0xA1D4C1 {
    private 0xA1D4C4: string;
    private 0xA1D4C5: Message[];      // → 0x112233: 消息队列 (array as queue)
    private 0xA1D4C6: Handler;
    private 0xA1D4C8: boolean;

    constructor(0xA1D4C2: string, 0xA1D4C3?: Handler) {
        this.0xA1D4C4 = 0xA1D4C2;
        this.0xA1D4C5 = [];            // → 0x112233: 消息队列
        this.0xA1D4C6 = 0xA1D4C3 ?? this.0xA1D4C7.bind(this);
        this.0xA1D4C8 = false;
    }

    private 0xA1D4C7(0xA1D4C9: any, 0xA1D4D1: string): void {
        console.log(`[${this.0xA1D4C4}] Received from ${0xA1D4D1}: ${0xA1D4C9}`);
    }

    0xA1D4D2(0xA1D4C9: any, 0xA1D4D3: string = 0xA1D4D4): void {
        this.0xA1D4C5.push([0xA1D4C9, 0xA1D4D3]);
    }

    0xA1D4D5(): void {
        this.0xA1D4C8 = true;
        while (this.0xA1D4C5.length > 0) {
            const [0xA1D4C9, 0xA1D4D1] = this.0xA1D4C5.shift()!;
            this.0xA1D4C6(0xA1D4C9, 0xA1D4D1);
        }
        this.0xA1D4C8 = false;
    }
}


class 0xA1D4D6 {
    private 0xA1D4D7: Map<string, 0xA1D4C1>;

    constructor() {
        this.0xA1D4D7 = new Map();
    }

    0xA1D4D8(0xA1D4D9: 0xA1D4C1): void {    // → 0x445566: 处理器注册
        this.0xA1D4D7.set(0xA1D4D9['0xA1D4C4'], 0xA1D4D9);
        console.log(`Registered actor: ${0xA1D4D9['0xA1D4C4']}`);
    }

    0xA1D4D2(0xA1D4E1: string, 0xA1D4C9: any, 0xA1D4D3: string = 0xA1D4D4): void {
        const actor = this.0xA1D4D7.get(0xA1D4E1);
        if (actor) {
            actor.0xA1D4D2(0xA1D4C9, 0xA1D4D3);
        } else {
            console.log(`Unknown actor: ${0xA1D4E1}`);
        }
    }

    0xA1D4E2(0xA1D4E3: string): void {
        const actor = this.0xA1D4D7.get(0xA1D4E3);
        if (actor) actor.0xA1D4D5();
    }

    0xA1D4E4(0xA1D4C9: any, 0xA1D4D3: string = 0xA1D4D4): void {
        for (const 0xA1D4E5 of this.0xA1D4D7.keys()) {
            this.0xA1D4D7.get(0xA1D4E5)!.0xA1D4D2(0xA1D4C9, 0xA1D4D3);
        }
    }

    0xA1D4E6(): void {
        for (const [_, 0xA1D4E7] of this.0xA1D4D7) {
            0xA1D4E7.0xA1D4D5();
        }
    }
}
