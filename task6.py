from math import floor


classes_held = int(input("Enter total classes held so far: "))
classes_attended = int(input("Enter classes attended so far: "))
eligibility_threshold = float(input("Enter eligibility threshold (%): "))

if classes_held <= 0:
    print("Total classes held must be greater than zero.")
    exit()

if classes_attended < 0 or classes_attended > classes_held:
    print("Classes attended must be between 0 and total classes held.")
    exit()

if eligibility_threshold < 0 or eligibility_threshold > 100:
    print("Eligibility threshold must be between 0 and 100.")
    exit()

current_percentage = classes_attended / classes_held * 100

print(f"\nCurrent attendance: {current_percentage:.2f}%")
print(f"Eligibility threshold: {eligibility_threshold:.2f}%")

if current_percentage >= eligibility_threshold:
    print("You already meet the eligibility threshold.")
else:
    print("You do not currently meet the eligibility threshold.")

print("\nEnter the expected attendance rate for each future scenario.")
scenario_rates = []

for scenario_number in range(1, 4):
    rate = float(input(f"Scenario {scenario_number} rate (%): "))
    if rate < 0 or rate > 100:
        print("Attendance rate must be between 0 and 100%.")
        exit()
    scenario_rates.append(rate)

print("\n====== FUTURE ATTENDANCE SCENARIOS ======")

for scenario_number, future_rate in enumerate(scenario_rates, start=1):
    print(f"\nScenario {scenario_number}: {future_rate:.2f}% future attendance")

    if current_percentage >= eligibility_threshold:
        print("Classes needed: 0 (already eligible)")
    elif future_rate <= eligibility_threshold:
        print("The threshold cannot be reached at this future attendance rate.")
    else:
        future_classes = 0
        while True:
            future_classes += 1
            future_attended = floor(future_classes * future_rate / 100)
            total_classes = classes_held + future_classes
            total_attended = classes_attended + future_attended
            attendance_percentage = total_attended / total_classes * 100

            if attendance_percentage >= eligibility_threshold:
                break

        print(f"Minimum future classes needed: {future_classes}")
        print(f"Attendance after that: {attendance_percentage:.2f}%")

print("\nNote: Future attended classes are rounded down for each scenario.")
print("=========================================")