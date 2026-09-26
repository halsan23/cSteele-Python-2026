# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements",
]


initial_game_state = dict.fromkeys(game_properties, 0)

for key, value in initial_game_state.items():
    print(f"{key}: {value}")


print()
print()
print("- - End of Line - -")
