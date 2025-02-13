from abc import ABC, abstractmethod

class User(ABC):
    """This class represents the behavior of a general
    user in the application"""

    def __init__(self, id_: int, username: str, email: str):
        self._id = id_
        self._username = username
        self._email = email
        self._grants = {}

    def get_id(self) -> int:
        """This method returns the id of the user.

        Returns:
            An integer with the id of the user.
        """
        return self._id

    @abstractmethod
    def setup_grants(self):
        """This method defines the grants for an specific user."""

    def validate_grants(self, grant: str) -> bool:
        """This method validates if the user has an specific grant.

        In this method a grant is received as parameter in order
        to valide if the user has that grant or not in the application.

        Args:
            grant(str): A grant to be validated

        Returns:
            A boolean with the response of the requested grant.
        """
        return self._grants[grant] if grant in self._grants else False




class Client(User):
    """This class represents the behavior of a general Customer in the application."""

    def __init__(self, id_: int, username: str, email: str):
        super().__init__(id_, username, email)

    def setup_grants(self):
        self._grants = {
            "buy_books": True,
            "add_books": False,
            "delete_books": False,
        }
    
# Clase concreta Admin
class Admin(User):
    """This class represents an administrator. It implements the User interface"""

    def __init__(self, id_: int, username: str, email: str):
        super().__init__(id_, username, email)

    def setup_grants(self):
        self._grants = {
            "buy_books": False,
            "add_books": True,
            "delete_books": True,
        }
