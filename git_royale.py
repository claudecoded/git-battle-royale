import subprocess
import sys
import random
import time

def get_git_contributors():
    """Extracts authors from the git log and calculates their stats based on commit history."""
    try:
        log_cmd = ["git", "log", "--format=%an"]
        result = subprocess.run(log_cmd, capture_output=True, text=True, check=True)
        authors = result.stdout.strip().split('\n')
        
        if not authors or authors == ['']:
            print("[ERROR] No commit history found in this repository.")
            sys.exit(1)
            
        commit_counts = {}
        for author in authors:
            if author:
                commit_counts[author] = commit_counts.get(author, 0) + 1
                
        return commit_counts
    except FileNotFoundError:
        print("[ERROR] Git is not installed or not found in your system PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("[ERROR] This directory is not a valid Git repository. Run 'git init' first.")
        sys.exit(1)

def run_battle_royale():
    print("==================================================")
    print(" ⚔️  WELCOME TO THE GIT BATTLE ROYALE ARENA  ⚔️ ")
    print("==================================================")
    print("Scanning repository history to summon warriors...\n")
    time.sleep(1.5)

    stats = get_git_contributors()
    
    players = []
    for name, commits in stats.items():
        base_hp = 100 + (commits * 2)   
        base_atk = 15 + (commits * 0.5) 
        players.append({
            "name": name,
            "hp": round(base_hp),
            "atk": round(base_atk),
            "commits": commits
        })

    if len(players) < 2:
        print("🤖 Not enough human contributors found. Summoning automated Bot warriors...")
        while len(players) < 4:
            players.append({
                "name": f"Legacy_Code_Bot_{random.randint(100, 999)}",
                "hp": 110,
                "atk": 18,
                "commits": 5
            })

    print(f"🏟️  {len(players)} warriors entered the arena based on commit history!")
    for p in players:
        print(f" -> {p['name']} (HP: {p['hp']} | ATK: {p['atk']} | Commits: {p['commits']})")
    print("\nStarting simulation in 3 seconds... Prepare your branches!\n")
    time.sleep(3)

    round_num = 1
    weapon_actions = [
        "force-pushed over", "resolved a merge conflict against", 
        "deprecated the code of", "cherry-picked the best features from",
        "opened a breaking Pull Request against", "deleted the branch of"
    ]

    while len(players) > 1:
        print(f"--- ROUND {round_num} ---")
        time.sleep(1)
        
        attacker = random.choice(players)
        defender = random.choice(players)
        
        while defender == attacker:
            defender = random.choice(players)
            
        action = random.choice(weapon_actions)
        damage = random.randint(10, attacker["atk"])
        defender["hp"] -= damage
        
        print(f"💥 {attacker['name']} {action} {defender['name']} dealing {damage} DMG!")
        
        if defender["hp"] <= 0:
            print(f"💀 [ELIMINATION] {defender['name']} was purged from the codebase!")
            players.remove(defender)
            
        print(f"   Remaining players: {len(players)}\n")
        round_num += 1

    winner = players[0]
    print("==================================================")
    print(f"🏆 WINNER WINNER MERGE DINNER! 🏆")
    print(f"👑 {winner['name']} dominated the repository and survived the Git Battle Royale!")
    print(f"💪 Final Status -> HP: {max(0, winner['hp'])} | Total Commits: {winner['commits']}")
    print("==================================================")

if __name__ == "__main__":
    run_battle_royale()
