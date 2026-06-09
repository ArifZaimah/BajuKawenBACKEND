from .controllers import user_controller

# Forward requests to controller
get_user_list = user_controller.get_user_list
create_user = user_controller.create_user
delete_user = user_controller.delete_user