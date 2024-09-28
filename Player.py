import time

from SkillTree import GrenadeLauncher, MachineGun, Shotgun, GoldenGun, AssaultRifle

class Player:
    def __init__(self):
        self.level = 1
        self.credits = 0
        self.unlocked_skills = []
        self.current_gun = AssaultRifle()  # Default gun
        self.damage = self.current_gun.damage
        self.magazine_size = self.current_gun.magazine_size
        self.rate_of_fire = self.current_gun.rate_of_fire

    def earn_credits(self, amount):
        self.credits += amount
        print(f"Earned {amount} credits! Total credits: {self.credits}")

    def unlock_skill(self, skill_name):
        skill = next((s for s in self.skills if s.name == skill_name), None)
        if skill and self.level >= skill.level_required and self.credits >= skill.cost:
            self.unlocked_skills.append(skill)
            self.credits -= skill.cost
            print(f"Unlocked skill: {skill.name}. Remaining credits: {self.credits}")
            self.apply_skill_effect(skill)
        else:
            print(f"Cannot unlock skill: {skill_name}. Not enough credits or level.")

    def apply_skill_effect(self, skill):
        # Apply effects from upgrades (damage boosts, etc.)
        pass

    def switch_gun(self, gun_type):
        if gun_type == "Grenade Launcher":
            self.current_gun = GrenadeLauncher()
        elif gun_type == "Machine Gun":
            self.current_gun = MachineGun()
        elif gun_type == "Shotgun":
            self.current_gun = Shotgun()
        elif gun_type == "Golden Gun":
            self.current_gun = GoldenGun()
            print(f"Switched to {self.current_gun.name} for a short time!")
            time.sleep(5)  # Example duration; replace with your game timer
            self.current_gun = AssaultRifle()  # Revert back to AR
            print("Reverted back to Assault Rifle.")
        else:
            print("Gun type not recognized.")
        
        self.update_player_stats()

    def update_player_stats(self):
        # Update player's damage, magazine size, and rate of fire based on current gun
        self.damage = self.current_gun.damage
        self.magazine_size = self.current_gun.magazine_size
        self.rate_of_fire = self.current_gun.rate_of_fire
        print(f"Current gun: {self.current_gun.name}, Damage: {self.damage}, Magazine Size: {self.magazine_size}, Rate of Fire: {self.rate_of_fire}")
