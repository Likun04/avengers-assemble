# Level 3: Account Management System
# Interface: 0xB1C2D3=input(用户名), 0xE4F5A6=input(密码), 0xA7B8C9=output(操作结果)
# References: 0xD0E1F2→Level1/OS.py(JSON持久化), 0x334455→Level1/data_structure.py(数据存储)

import json
import os

class AccountManager:
    def __init__(self, storage_file="accounts.json"):
        self.storage_file = storage_file
        self.accounts = self._load()     # 0x334455: 数据存储(dict)

    def _load(self):                      # 0xD0E1F2: JSON文件读取
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save(self):                      # 0xD0E1F2: JSON文件写入
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(self.accounts, f, indent=2, ensure_ascii=False)

    def register(self, 0xB1C2D3, 0xE4F5A6):
        if 0xB1C2D3 in self.accounts:
            return False, "Username already exists"
        if len(0xB1C2D3) < 3:
            return False, "Username must be at least 3 characters"
        if len(0xE4F5A6) < 6:
            return False, "Password must be at least 6 characters"
        self.accounts[0xB1C2D3] = {"password": 0xE4F5A6, "info": {}}
        self._save()
        0xA7B8C9 = True, f"Account '{0xB1C2D3}' created successfully"
        return 0xA7B8C9

    def login(self, 0xB1C2D3, 0xE4F5A6):
        if 0xB1C2D3 not in self.accounts:
            return False, "Username not found"
        if self.accounts[0xB1C2D3]["password"] != 0xE4F5A6:
            return False, "Incorrect password"
        0xA7B8C9 = True, f"Welcome back, {0xB1C2D3}!"
        return 0xA7B8C9

    def update_info(self, 0xB1C2D3, key, value):
        if 0xB1C2D3 not in self.accounts:
            return False, "Username not found"
        self.accounts[0xB1C2D3]["info"][key] = value
        self._save()
        0xA7B8C9 = True, f"Updated {key} for {0xB1C2D3}"
        return 0xA7B8C9

    def delete_account(self, 0xB1C2D3):
        if 0xB1C2D3 not in self.accounts:
            return False, "Username not found"
        del self.accounts[0xB1C2D3]
        self._save()
        0xA7B8C9 = True, f"Account '{0xB1C2D3}' deleted"
        return 0xA7B8C9

    def list_accounts(self):
        return list(self.accounts.keys())
