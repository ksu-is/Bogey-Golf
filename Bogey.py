python
# Golf course library
golf_courses = {
    "Cobblestone": [4, 3, 5, 4, 4, 3, 5, 4, 4],  # Par for each hole
    "Governors": [5, 4, 3, 4, 5, 3, 4, 4, 4],
    "Marietta City Club": [4, 3, 4, 5, 4, 3, 5, 4, 4]
}

def list_courses():
    print("\nAvailable Golf Courses:")
    for i, course in enumerate(golf_courses.keys(), start=1):
        print(f"{i}. {course}")

def get_course_selection():
    while True:
        try:
            choice = int(input("\nEnter the name of the course you'd like to play: "))
            if 1 <= choice <= len(golf_courses):
                return list(golf_courses.keys())[choice - 1]
            else:
                print("Invalid choice. Please select a valid course number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_scores(par_values):
    scores = []
    print("\nEnter your scores for each hole:")
    for i, par in enumerate(par_values, start=1):
        while True:
            try:
                score = int(input(f"Hole {i} (Par {par}): "))
                if score > 0:
                    scores.append(score)
                    break
                else:
                    print("Score must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores

def display_scorecard(course_name, par_values, scores):
    print("\n--- Scorecard ---")
    print(f"Course: {course_name}")
    print("Hole:    ", ' '.join(f"{i+1:2}" for i in range(len(par_values))))
    print("Par:     ", ' '.join(f"{par:2}" for par in par_values))
    print("Score:   ", ' '.join(f"{score:2}" for score in scores))
    
    total_par = sum(par_values)
    total_score = sum(scores)
    print(f"\nTotal Par: {total_par}")
    print(f"Total Score: {total_score}")
    print(f"Result: {'Over' if total_score > total_par else 'Under' if total_score < total_par else 'Even'} Par by {abs(total_score - total_par)} strokes")

def main():
    print("Welcome to the Golf Score Tracker!")
    list_courses()
    course_name = get_course_selection()
    par_values = golf_courses[course_name]
    
    scores = input_scores(par_values)
    display_scorecard(course_name, par_values, scores)