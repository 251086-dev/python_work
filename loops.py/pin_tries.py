# pin_tries.py
# Give the user three tries to enter the correct PIN.
MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0
while tries < MAX_TRIES:
    pin = input("PIN: ")
    tries += 1
    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")
    if tries == MAX_TRIES:
        print("Card blocked.")