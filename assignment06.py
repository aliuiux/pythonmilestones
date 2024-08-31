def manage_student_database():
    students = []
    student_id = 1

    while True:
        # Get the student's name or stop the input process
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        if name.lower() == 'stop':
            break

        # Check for duplicate names
        if any(student[1] == name for student in students):
            print("This name is already in the list.")
        else:
            # Add the student to the list
            students.append((student_id, name))
            student_id += 1

    # Display the complete list of students (tuples)
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Calculate and display the total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate and display the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")

    # Find the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda x: len(x[1]))
        shortest_name_student = min(students, key=lambda x: len(x[1]))
        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Call the function to run the program
manage_student_database()
