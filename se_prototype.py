from datetime import datetime
from typing import List

# Basic user class
class User:
    def __init__(self, user_id: str, username: str, password: str, email: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.profile = None  # This will be an instance of Profile class
    
    def create_user(self):
        pass  # Implementation for creating a user
    
    def edit_profile(self, profile):
        self.profile = profile
    
    def delete_account(self):
        pass  # Implementation for deleting account
    
    def login(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password
    
    def logout(self):
        pass  # Implementation for logging out

# Profile class for each user
class Profile:
    def __init__(self, gender: str, age: int, bio: str):
        self.gender = gender
        self.age = age
        self.interests = []  # List of Interest objects
        self.bio = bio
        self.location = None  # This will be an instance of Location class
        self.matches = []  # List of Match objects
        self.messages = []  # List of Message objects
        self.eventsRegistered = []  # List of EventRegistration objects
        self.notifications = []  # List of Notification objects

    def add_interest(self, interest):
        self.interests.append(interest)
    
    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)
    
    def send_message(self, message):
        self.messages.append(message)
    
    def create_event_registration(self, event_registration):
        self.eventsRegistered.append(event_registration)
    
    def add_notification(self, notification):
        self.notifications.append(notification)

# Event class for organizing events
class Event:
    def __init__(self, event_id: str, name: str, date: datetime, description: str):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = None  # This will be an instance of Location class
        self.description = description

# Match class to represent matches between users
class Match:
    def __init__(self, matched_user: User, matched_at: datetime):
        self.matched_user = matched_user
        self.matched_at = matched_at
        self.chat_group = None  # This will be an instance of ChatGroup class

# Message class for messaging functionality
class Message:
    def __init__(self, message_id: str, sender: User, receiver: User, content: str, timestamp: datetime):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = timestamp

# Additional classes like EventRegistration, Notification, Location, Interest, and ChatGroup
# would follow a similar structure, with attributes and methods as per the class diagram.

# Example of how these classes might be used
if __name__ == "__main__":
    # Creating two users
    user1 = User("1", "Alice", "password123", "alice@ucl.ac.uk")
    user2 = User("2", "Bob", "password456", "bob@ucl.ac.uk")
    
    # User1 logs in
    assert user1.login("alice@ucl.ac.uk", "password123") == True
    
    # Setting up profiles
    profile1 = Profile("Female", 20, "Hi, I'm Alice!")
    profile2 = Profile("Male", 21, "Hey there, I'm Bob.")
    user1.edit_profile(profile1)
    user2.edit_profile(profile2)
    
    # Further functionality like adding interests, creating matches, etc., would follow.
