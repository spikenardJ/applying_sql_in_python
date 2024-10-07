# Question 2: Advanced Data Analysis in Gym Management System

# Task 1: SQL BETWEEN Usage

from connect_mysql import connect_database
conn = connect_database()

def get_members_in_age_range(cursor, start_age, end_age):
    # SQL query using BETWEEN
    query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))
    print(f"Members with ages between {start_age} and {end_age}:")
    # Execute and fetch results
    for members in cursor.fetchall():
        print(members)

def main():
    if conn is not None:
        try:
            cursor = conn.cursor()
            start_age = input("Using only numbers, enter the starting age of members that you are looking for: ")
            end_age = input("Using only numbers, enter the ending age of members that you are looking for: ")
            get_members_in_age_range(cursor, start_age, end_age)
        except ValueError:
            print("Please use valid numbers for ages.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()