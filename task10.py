number_of_courses = int(input("Enter number of courses: "))
if number_of_courses <= 0:
    print("Enter at least one course.")
    exit()

courses = {}

for course_number in range(1, number_of_courses + 1):
    print(f"\nCourse {course_number} admission requirements")
    course_name = input("Course name: ")
    courses[course_name] = {
        "aggregate": float(input("Minimum aggregate marks (%): ")),
        "math": float(input("Minimum Mathematics marks (%): ")),
        "science": float(input("Minimum Science marks (%): ")),
    }

number_of_applicants = int(input("\nEnter number of applicants: "))
if number_of_applicants <= 0:
    print("Enter at least one applicant.")
    exit()

applicants = []

for applicant_number in range(1, number_of_applicants + 1):
    print(f"\nApplicant {applicant_number}")
    name = input("Applicant name: ")
    course_choice = input("Course applied for: ")

    if course_choice not in courses:
        print("Course not found. Please enter one of the listed course names.")
        exit()

    english_marks = float(input("English marks (%): "))
    math_marks = float(input("Mathematics marks (%): "))
    science_marks = float(input("Science marks (%): "))
    aggregate = (english_marks + math_marks + science_marks) / 3

    requirements = courses[course_choice]
    eligible = (
        aggregate >= requirements["aggregate"]
        and math_marks >= requirements["math"]
        and science_marks >= requirements["science"]
    )

    applicants.append({
        "name": name,
        "course": course_choice,
        "english": english_marks,
        "math": math_marks,
        "science": science_marks,
        "aggregate": aggregate,
        "eligible": eligible,
    })

print("\n========== ADMISSION RESULTS ==========")

for course_name in courses:
    eligible_applicants = [
        applicant for applicant in applicants
        if applicant["course"] == course_name and applicant["eligible"]
    ]

    # Rank by aggregate, then Mathematics marks, then applicant name.
    eligible_applicants.sort(
        key=lambda applicant: (
            -applicant["aggregate"],
            -applicant["math"],
            applicant["name"].lower(),
        )
    )

    print(f"\nCourse: {course_name}")
    if eligible_applicants:
        for rank, applicant in enumerate(eligible_applicants, start=1):
            print(
                f"{rank}. {applicant['name']} - "
                f"Aggregate: {applicant['aggregate']:.2f}%, "
                f"Math: {applicant['math']:.2f}%, "
                f"Science: {applicant['science']:.2f}%"
            )
    else:
        print("No eligible applicants.")

print("\nApplicants who did not meet their course requirements:")
ineligible_applicants = [
    applicant for applicant in applicants if not applicant["eligible"]
]
if ineligible_applicants:
    for applicant in ineligible_applicants:
        print(f"- {applicant['name']} (applied for {applicant['course']})")
else:
    print("None")

print("\nNote: Aggregate is the average of English, Mathematics, and Science.")
print("Requirements and tie-breaking rules are examples; edit as needed.")
print("=======================================")