from math import ceil


planned_participants = int(input("Enter planned number of participants: "))
if planned_participants <= 0:
    print("The planned number of participants must be greater than zero.")
    exit()

venue_cost = float(input("Venue cost: Rs. "))
equipment_cost = float(input("Equipment cost: Rs. "))
transport_cost = float(input("Total transport cost: Rs. "))
catering_per_person = float(input("Catering cost per participant: Rs. "))
certificate_per_person = float(input("Certificate cost per participant: Rs. "))
sponsorship = float(input("Sponsorship amount: Rs. "))
registration_fee = float(input("Registration fee per participant: Rs. "))

fixed_cost = venue_cost + equipment_cost + transport_cost
variable_cost_per_person = catering_per_person + certificate_per_person
variable_cost = planned_participants * variable_cost_per_person
total_cost = fixed_cost + variable_cost

participant_contributions = planned_participants * registration_fee
total_funds = participant_contributions + sponsorship
shortfall = max(0, total_cost - total_funds)
surplus = max(0, total_funds - total_cost)
net_contribution_per_registration = registration_fee - variable_cost_per_person

print("\n====== CAMPUS EVENT BUDGET ======")
print(f"Venue cost:                 Rs. {venue_cost:,.2f}")
print(f"Equipment cost:              Rs. {equipment_cost:,.2f}")
print(f"Transport cost:              Rs. {transport_cost:,.2f}")
print(f"Catering cost:               Rs. {variable_cost:,.2f}")
print(f"Certificate cost:            Rs. {planned_participants * certificate_per_person:,.2f}")
print(f"Total event cost:            Rs. {total_cost:,.2f}")
print("---------------------------------")
print(f"Registration contributions:  Rs. {participant_contributions:,.2f}")
print(f"Sponsorship:                 Rs. {sponsorship:,.2f}")
print(f"Funding shortfall:           Rs. {shortfall:,.2f}")
print(f"Funding surplus:             Rs. {surplus:,.2f}")
print(f"Net contribution per registration: Rs. {net_contribution_per_registration:,.2f}")

if sponsorship >= fixed_cost:
    minimum_registrations = 0
    print("Registrations needed to cover fixed costs: 0")
    print("Sponsorship alone covers the fixed event costs.")
elif net_contribution_per_registration > 0:
    minimum_registrations = ceil(
        (fixed_cost - sponsorship) / net_contribution_per_registration
    )
    print(f"Minimum registrations to break even: {minimum_registrations}")
else:
    minimum_registrations = None
    print("Break-even is not possible with the current registration fee.")
    print("The fee must exceed per-participant catering and certificate costs,")
    print("or the sponsorship must cover all fixed event costs.")

if minimum_registrations is not None and minimum_registrations > planned_participants:
    print("Warning: Planned participants are below the break-even count.")

print("=================================")
print("Note: All amounts are example inputs; enter costs in the same currency.")