import Player

class Skill:
    def __init__(self, name, description, level_required=1, cost=100, prerequisites=None):
        self.name = name
        self.description = description
        self.level_required = level_required
        self.cost = cost  # Cost in credits to unlock the skill
        self.prerequisites = prerequisites if prerequisites is not None else []

class GunUpgradeTree:
    def __init__(self):
        self.skills = [
            Skill("Basic Damage Boost", "Increases base damage by 10%.", level_required=1, cost=100),
            Skill("Critical Hit Damage", "Increases critical hit damage by 25%.", level_required=2, cost=150),
            Skill("Increased Magazine Size", "Increases magazine size by 5 rounds.", level_required=1, cost=80),
            Skill("Extended Clip", "Further increases magazine size by 10 rounds.", level_required=3, cost=120, prerequisites=[Skill("Increased Magazine Size")]),
            Skill("Faster Rate of Fire", "Increases rate of fire by 15%.", level_required=1, cost=90),
            Skill("Rapid Fire Mode", "Allows for continuous firing for 5 seconds.", level_required=4, cost=200, prerequisites=[Skill("Faster Rate of Fire")]),
        ]

    def display_skills(self):
        for skill in self.skills:
            status = "Available" if skill.cost <= player.credits else "Not Enough Credits"
            print(f"{skill.name}: {skill.description} - Cost: {skill.cost} credits - Status: {status}")

    def earn_credits(self, amount):
        self.credits += amount
        print(f"Earned {amount} credits! Total credits: {self.credits}")

    def unlock_skill(self, skill_name):
        skill = next((s for s in gun_upgrade_tree.skills if s.name == skill_name), None)
        if skill and self.level >= skill.level_required and self.credits >= skill.cost:
            self.unlocked_skills.append(skill)
            self.credits -= skill.cost  # Deduct credits
            print(f"Unlocked skill: {skill.name}. Remaining credits: {self.credits}")
            self.apply_skill_effect(skill)
        else:
            print(f"Cannot unlock skill: {skill_name}. Not enough credits or level.")

    def apply_skill_effect(self, skill):
        if skill.name == "Basic Damage Boost":
            self.damage *= 1.10  # Increase damage by 10%
        elif skill.name == "Critical Hit Damage":
            # Implement logic for critical damage
            pass
        elif skill.name == "Increased Magazine Size":
            self.magazine_size += 5
        elif skill.name == "Extended Clip":
            self.magazine_size += 10
        elif skill.name == "Faster Rate of Fire":
            self.rate_of_fire *= 1.15  # Increase rate of fire by 15%
        elif skill.name == "Rapid Fire Mode":
            # Implement rapid fire mode logic
            pass

class Gun:
    def __init__(self, name, damage, magazine_size, rate_of_fire):
        self.name = name
        self.damage = damage
        self.magazine_size = magazine_size
        self.rate_of_fire = rate_of_fire

    def fire(self):
        # Logic to fire the gun
        print(f"{self.name} fired! Damage: {self.damage}")

class AssaultRifle(Gun):
    def __init__(self):
        super().__init__("Assault Rifle", damage=10, magazine_size=30, rate_of_fire=1)

class GrenadeLauncher(Gun):
    def __init__(self):
        super().__init__("Grenade Launcher", damage=50, magazine_size=5, rate_of_fire=0.5)

class MachineGun(Gun):
    def __init__(self):
        super().__init__("Machine Gun", damage=8, magazine_size=50, rate_of_fire=2)

class Shotgun(Gun):
    def __init__(self):
        super().__init__("Shotgun", damage=25, magazine_size=8, rate_of_fire=0.8)

class GoldenGun(Gun):
    def __init__(self):
        super().__init__("Golden Gun", damage=float('inf'), magazine_size=1, rate_of_fire=1)  # Kills all enemies instantly

# Example Usage
gun_upgrade_tree = GunUpgradeTree()
player = Player()

# Simulate earning credits by defeating enemies
player.earn_credits(150)  # Earn credits
gun_upgrade_tree.display_skills()  # Display available skills

# Try to unlock skills
player.unlock_skill("Basic Damage Boost")
player.unlock_skill("Increased Magazine Size")