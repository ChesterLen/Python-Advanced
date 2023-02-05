def students_credits(*args):
    total_points_earned = 0
    total_credits = 0

    courses = {}
    result = []

    for data in args:
        course, credits, points, diyan_points = data.split("-")[0], int(data.split("-")[1]), int(data.split("-")[2]), int(data.split("-")[3])
        if course not in courses.keys():
            courses[course] = 0
        total_points_earned += diyan_points
        percent_points = diyan_points / points * 100
        credits_earned = percent_points / 100 * credits
        courses[course] = float(f"{credits_earned:.1f}")
        total_credits += credits_earned
    
    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")
    sorted_result = sorted(courses.items(), key=lambda x: -x[1])

    for course, points in sorted_result:
        result.append(f"{course} - {points}")
    
    return "\n".join(result)