# Question 1: Gym Database Management with Python and SQL

# Task 1: Add a Member

from connect_mysql import connect_database
conn = connect_database()

def add_member(name, age):
    # SQL query to add a new member
    if conn is not None:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO Members(name, age) VALUES (%s, %s)"
            cursor.execute(query, (name, age))
            conn.commit()
            print("New member added successfully.")
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            # conn.close()

add_member("Bat Man", 33)
add_member("Wonder Woman", 26)            
add_member("Super Man", 30)
add_member("Spider Man", 22)

# Task 2: Add a Workout Session

def add_workout_session(date, duration_minutes, calories_burned, member_id):
    # SQL query to add a new workout session
    if conn is not None:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO WorkoutSessions(date, duration_minutes, calories_burned, member_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (date, duration_minutes, calories_burned, member_id))
            print("Workout session added successfully.")
            # Error handling
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            # conn.close()

add_workout_session("2024-10-07", 30, 1500, 2)
add_workout_session("2024-11-06", 30, 1800, 2)
add_workout_session("2024-11-02", 30, 1700, 5)


# Task 3: Updating Member Information

def update_member_age(new_age, member_id):
    # SQL query to update age
    if conn is not None:
        cursor = conn.cursor()
        try:
            query_select = "SELECT * FROM Members WHERE id = %s"
            cursor.execute(query_select, (member_id,))
            if cursor.fetchone():
                query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query, (new_age, member_id))
                conn.commit()
                print("The age of member updated successfully.")
            else:
                print("This member ID does not exist. Please try again.")
        # Error handling
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            # conn.close()

update_member_age(26, 2)


# Task 4: Delete a Workout Session

def delete_workout_session(session_id):
    if conn is not None:
        cursor = conn.cursor()
        try:
            # SQL query to delete a session
            cursor = conn.cursor()
            check_query = "SELECT id FROM WorkoutSessions WHERE id = %s"
            cursor.execute(check_query, (session_id,))
            session = cursor.fetchone()
            # Error handling for non-existent session ID
            if session:
                delete_query = "DELETE FROM WorkoutSessions WHERE id = %s"
                cursor.execute(delete_query, (session_id,))

                conn.commit()
                print("Workout session deleted successfully.")
            else:
                print("The session ID does not exist. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_workout_session(8)
