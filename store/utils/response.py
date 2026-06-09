from django.http import JsonResponse


def success_response(message, data=None):

    response_data = {"status": True, "message": message}

    if data is not None:
        response_data["data"] = data

    return JsonResponse(response_data)


def error_response(message, status_code=500):
    return JsonResponse({"status": False, "message": message}, status=status_code)
