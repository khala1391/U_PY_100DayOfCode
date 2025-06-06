# post.py

class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def __repr__(self):
        # Developer-friendly representation
        return f"Post(id={self.id}, title={self.title})"

    def __str__(self):
        # User-friendly display
        return f"{self.title} — {self.subtitle}\n{self.body}"
