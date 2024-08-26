# Wrong

class UserManager:
    def authenticate_user(self, username, password):
        pass

    def update_user_profile(self, user_id, new_profile_data):
        pass

    def send_email_notification(self, user_email, message):
        pass


# Correct

class UserAuthenticator:
    def authenticate_user(self, username, password):
        pass


class UserProfileManager:
    def update_user_profile(self, user_id, new_profile_data):
        pass


class EmailNotifier:
    def send_email_notification(self, user_email, message):
        pass
