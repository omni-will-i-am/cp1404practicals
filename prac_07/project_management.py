

from datetime import datetime
from prac_07.project import Project

DATE_FORMAT = "%d/%m/%Y"
DEFAULT_FILE = "projects.txt"

MENU = ("- (L)oad projects  \n"
        "- (S)ave projects  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project  \n"
        "- (U)pdate project\n"
        "- (Q)uit\n>>> ")

def main():
    print("Welcome to Pythonic Project Management")
    # Load default before showing the menu
    try:
        projects = load_projects(DEFAULT_FILE)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    except FileNotFoundError:
        projects = []
        print("No default file found; starting empty.")

    while True:
        choice = input(MENU).strip().lower()
        if choice == "l":
            filename = input("Filename to load: ").strip()
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "s":
            filename = input("Filename to save: ").strip()
            if filename:
                save_projects(filename, projects)
                print(f"Saved {len(projects)} projects to {filename}")
            else:
                print("No filename given.")
        # elif choice == "d":
        #     display_projects(projects)
        # elif choice == "f":
        #     filter_projects_by_date(projects)
        # elif choice == "a":
        #     add_new_project(projects)
        # elif choice == "u":
        #     update_project(projects)
        elif choice == "q":
            if confirm_yes_no(f"Would you like to save to {DEFAULT_FILE}? (Y/N): "):
                save_projects(DEFAULT_FILE, projects)
                print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid menu choice")

def confirm_yes_no(prompt):
    """Prompt until user enters Y or N; return True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter Y or N.")

def parse_date(date_string):
    """Parse the date entered by the user."""
    return datetime.datetime.striptime(date_string.strip(), DATE_FORMAT).date()

def load_projects(filename):
    """Load projects from a file with a header."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, start_string, priority, cost, percent = line.split("\t")
            start_date = parse_date(start_string)
            projects.append(
                Project(name.strip(), start_date, int(priority), float(cost), int(percent))
            )
    return projects

def save_projects(filename, projects):
    """Save projects to a tab-delimited file with header."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t"
                f"{project.start_date.strftime(DATE_FORMAT)}\t"
                f"{project.priority}\t"
                f"{project.cost:.2f}\t"
                f"{project.completion_percentage}\n"
            )
