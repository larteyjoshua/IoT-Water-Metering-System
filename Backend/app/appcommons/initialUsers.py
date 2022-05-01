from app.utils.config import settings
class User:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    SUPER_ADMIN = {
        "fullName": "SUPERADMIN",
        "email": settings.FIRST_SUPER_ADMIN_EMAIL,
        "password": settings.FIRST_SUPER_ADMIN_PASSWORD,
        "phoneNumber": settings.PHONENUMBER
    }
    