from store.services import user_service
from store.utils.response import success_response, error_response
import json
from datetime import datetime, timezone
from django.views.decorators.csrf import csrf_exempt


def get_user_list(request):
    try:
        users = user_service.get_user_list()
        print("Fetched users:", users)
        return success_response("Successfully fetched users", users)

    except Exception as e:
        print("Error fetching users:", str(e))
        return error_response(f"Failed to fetch users: {str(e)}")

@csrf_exempt 
def create_user(request):
    if request.method != "POST":
        return error_response("Only POST method is allowed.", 405)

    try:
        # Parse JSON body
        body_unicode = request.body.decode("utf-8")
        body_data = json.loads(body_unicode)

        # Validate input
        name = body_data.get("name")
        email = body_data.get("email")
        password = body_data.get("password")

        if not name or not email or not password:
            return error_response("Name, Email, and Password are required.", 400)

        now = datetime.now(timezone.utc).isoformat()

        user_service.create_user(name, email, password, now, now)

        return success_response("User created successfully.")

    except Exception as e:
        print("Error creating user:", str(e))
        return error_response(f"Failed to create user: {str(e)}")

@csrf_exempt
def delete_user(request):
    if request.method != "DELETE":
        return error_response("Only DELETE method is allowed.", 405)

    try:
        data = request.body

        # Step 1: Decode the byte string
        body_string = data.decode("utf-8")

        # Step 2: Parse the JSON to a Python dictionary
        body_data = json.loads(body_string)

        # Step 3: Extract 'user_id' from the dictionary
        user_id = body_data.get("user_id")

        print("user id: ", user_id)
       
        if user_service.delete_user(user_id):
            return success_response("User deleted successfully.")
        else:
            return error_response("User not found.", 404)
    except Exception as e:
        print("Error deleting user:", str(e))
        return error_response(f"Failed to delete user: {str(e)}")
