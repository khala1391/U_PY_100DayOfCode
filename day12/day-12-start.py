################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# ////////////////////////////
game_level=3
enemy = ["skeleton","Zombie","Alien"]
if game_level<5:
  new_enemy = enemy[0]

print(new_enemy)


# ////////////////////////////

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# ////////////////////////////
# in practical, not suggested to edit global variable inside local scope
# just read

# below is good practice for modify
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1   # use return
enemies = increase_enemies() # replace new value to global var
print(f"enemies outside function: {enemies}")


# no block scope

a = 2

print(f'before if a: {a}')

if True:
  a = 10

print(f'after if a: {a}')