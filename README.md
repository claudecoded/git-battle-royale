# ⚔️ Git Battle Royale

Turn your local Git repository commit history into a text-based, action-packed automated Battle Royale game! 

This script scans your repository, detects all contributors, scales their health (HP) and attack power (ATK) based on their real-world commit frequency, and drops them into a virtual terminal arena where only one branch survivor remains.

## 🚀 How it Works

* **HP & ATK Scaling:** Developers with more commits enter the arena with a slight tactical health and damage advantage.
* **Smart Detection:** Automatically falls back to AI/Legacy Bots if your repository has fewer than 2 active contributors.
* **Zero Dependencies:** Built entirely using native Python libraries (`subprocess`, `sys`, `random`, `time`). No `pip install` required.

## 🛠️ Usage Instructions

1. Download or clone this repository.
2. Copy the `git_royale.py` script and drop it into the root directory of **any active Git repository** on your computer.
3. Open your terminal inside that repository folder and execute:

```bash
python git_royale.py
```

## 🎮 Preview Match Example

```text
==================================================
 ⚔️  WELCOME TO THE GIT BATTLE ROYALE ARENA  ⚔️ 
==================================================
Scanning repository history to summon warriors...

🏟️  3 warriors entered the arena based on commit history!
 -> Alice (HP: 150 | ATK: 28 | Commits: 25)
 -> Bob (HP: 112 | ATK: 18 | Commits: 6)
 -> Charlie (HP: 104 | ATK: 16 | Commits: 2)

--- ROUND 1 ---
💥 Alice force-pushed over Bob dealing 24 DMG!
   Remaining players: 3

--- ROUND 2 ---
💥 Charlie opened a breaking Pull Request against Bob dealing 15 DMG!
💀 [ELIMINATION] Bob was purged from the codebase!
```

## 📄 License

This project is licensed under the MIT License. Feel free to fork, modify, and add custom combat lines!
