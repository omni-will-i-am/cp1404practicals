"""
CP1404/CP5632 Practical 07
This program will load and save a data file and use a list of Project objects in a variety of different functions.
"""

import datetime
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

    while True: # Stop doing this
        choice = input(MENU).strip().lower()
        # while choice != "q":
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
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
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
    return datetime.datetime.strptime(date_string.strip(), DATE_FORMAT).date()

def load_projects(filename):
    """Load projects from a file with a header."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                continue
            name, start_string, priority, cost, percent = parts[:5]
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
def display_projects(projects):
    """Display incomplete then completed projects, each sorted by priority (uses __lt__)."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    incomplete.sort()  # priority ascending via Project.__lt__
    complete.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Prompt for a cutoff date and print projects starting on/after it, sorted by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    cutoff = parse_date(date_string)
    filtered = [project for project in projects if project.start_date >= cutoff]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project)

def add_new_project(projects):
    """Prompt for new project fields and append a Project to the list."""
    print("Let's add a new project")
    name = input("Project name: ").strip()
    start_string = input("Start date (dd/mm/yyyy): ").strip()
    start_date = parse_date(start_string)
    priority = int(input("Priority: ").strip())
    cost = float(input("Cost estimate: $").replace(",", "").strip())
    percent = int(input("Percent complete: ").strip())
    projects.append(Project(name, start_date, priority, cost, percent))

def update_project(projects):
    """Choose a project, then optionally update completion % and/or priority (blank keeps existing)."""
    if not projects:
        print("No projects to update.")
        return
    # Show an unsorted indexed list
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    while True:
        try:
            index = int(input("Project choice: ").strip())
            project = projects[index]
            break
        except (ValueError, IndexError):
            print("Invalid selection; enter a valid number.")

    print(project)
    new_percentage = input("New Percentage: ").strip()
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ").strip()
    if new_priority != "":
        project.priority = int(new_priority)

if __name__ == "__main__":
    main()