from src.user_dao import add_user
from src.vacation_dao import get_vacations, request_vacation
from src.user_facade import login_user, like_vacation, unlike_vacation
from src.database import get_connection
from datetime import date, timedelta

if __name__ == '__main__':
    # Ensure user is created if not already in the database
    add_user('George', 'Mattar', 'GeorgeMattar@example.com', 'password123', 1)

    user_id = None
    while user_id is None:
        print("Please Enter Email:")
        mail = input().strip()
        print("Please Enter Password:")
        password = input().strip()

        # Retrieve user ID using the login function
        user_id = login_user(mail, password)

        if user_id is None:
            print("Invalid email or password. Please try again.")
        else:
            print(f"Login successful! User ID: {user_id}")

    # Fetch and display vacations for the user to like or dislike
    print("\nHere are the following vacations available:")
    vacations = get_vacations()
    for vacation in vacations:
        print(f"\nVacation ID: {vacation['id']}")
        print(f"Country: {vacation['country']}")
        print(f"Description: {vacation['description']}")
        print(f"Start Date: {vacation['start_date']}")
        print(f"End Date: {vacation['end_date']}")
        print(f"Price: {vacation['price']}")
        print(f"Image: {vacation['image_file']}")

        # Ask the user to like or dislike the vacation
        user_input = input("Do you like this vacation? (y/n): ").strip().lower()

        if user_input == "y":
            like_vacation(user_id, vacation['id'])
            print(f"You liked vacation {vacation['id']}!")
        elif user_input == "n":
            unlike_vacation(user_id, vacation['id'])
            print(f"You unliked vacation {vacation['id']}.")
        else:
            print("Invalid input. Please enter 'y' for like or 'n' for dislike.")

    # Add a new vacation request for the logged-in user
    future_start_date = (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
    future_end_date = (date.today() + timedelta(days=14)).strftime('%Y-%m-%d')

    # Insert a new vacation and retrieve its ID
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO vacations (country_id, description, start_date, end_date, price, image_file)
                VALUES (%s, 'Vacation', %s, %s, %s, %s) RETURNING id
            """, (5, future_start_date, future_end_date, 1500.00, 'beach_resort.jpg'))
            vacation_id = cur.fetchone()[0]  # Retrieve new vacation ID
        conn.commit()

    print(f"Vacation request created successfully with ID: {vacation_id}")

    # Test like and unlike functionality
    like_vacation(user_id, vacation_id)
    print(f"User {user_id} liked vacation {vacation_id}.")

    unlike_vacation(user_id, vacation_id)
    print(f"User {user_id} unliked vacation {vacation_id}.")
