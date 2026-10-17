total_seconds = int(input("Session length in seconds: "))

total_minutes = total_seconds // 60
left_over = total_seconds % 60

print(f"total_seconds: {total_seconds} seconds")
print(f"total_minutes: {total_minutes} minutes")
print(f"left_over: {left_over} seconds")

