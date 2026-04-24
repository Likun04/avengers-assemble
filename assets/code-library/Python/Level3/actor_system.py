# Level 3: Actor System
# Interface: 0xA1B2C3=input(Actor名称), 0xD4E5F6=input(消息内容), 0xF7A8B9=input(消息处理函数)
# References: 0x112233→Level1/data_structure.py(消息队列), 0x445566→Level1/function.py(处理器注册)

from collections import deque

class Actor:
    def __init__(self, 0xA1B2C3, handler=None):
        self.name = 0xA1B2C3
        self.mailbox = deque()     # 0x112233: 消息队列
        self.handler = handler or self.default_handler
        self.running = False

    def default_handler(self, 0xD4E5F6, sender):
        print(f"[{self.name}] Received from {sender}: {0xD4E5F6}")

    def send(self, 0xD4E5F6, sender="system"):
        self.mailbox.append((0xD4E5F6, sender))

    def process_all(self):
        self.running = True
        while self.mailbox:
            0xD4E5F6, sender = self.mailbox.popleft()
            self.handler(0xD4E5F6, sender)
        self.running = False


class ActorSystem:
    def __init__(self):
        self.actors = {}

    def register(self, actor):     # 0x445566: 处理器注册
        self.actors[actor.name] = actor
        print(f"Registered actor: {actor.name}")

    def send(self, target_name, 0xD4E5F6, sender="system"):
        if target_name in self.actors:
            self.actors[target_name].send(0xD4E5F6, sender)
        else:
            print(f"Unknown actor: {target_name}")

    def process_all(self, actor_name):
        if actor_name in self.actors:
            self.actors[actor_name].process_all()

    def broadcast(self, 0xD4E5F6, sender="system"):
        for name in self.actors:
            self.actors[name].send(0xD4E5F6, sender)

    def process_all_actors(self):
        for name, actor in self.actors.items():
            actor.process_all()
