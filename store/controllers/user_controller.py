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
