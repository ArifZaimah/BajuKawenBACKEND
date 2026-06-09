import uuid
from store.firebase import db

# Function to fetch user list from Firestore
def get_user_list():
    users = []
    users_ref = db.collection("users")
    docs = users_ref.stream()

    for doc in docs:
        user_data = doc.to_dict()
        users.append(user_data)

    return users

# Function to create a new user in Firestore
def create_user(name, email, password, create_datetime, update_datetime):
    user_id = str(uuid.uuid4())

    db.collection('users').document(user_id).set({
        'id': user_id,
        'name': name,
        'email': email,
        'password': password,
        'create_datetime': create_datetime,
        'update_datetime': update_datetime
    })

# Function to delete a user from Firestore
def delete_user(user_id):
    try:
        user_ref = db.collection('users').document(user_id)
        # Check if the user exists
        if user_ref.get().exists:
            user_ref.delete()
            return True
        else:
            return False  # User not found
    except Exception as e:
        # print(f"Error deleting user {user_id}: {str(e)}")
        return False
