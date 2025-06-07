class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title})"

    def __str__(self):
        return f"{self.title} — {self.subtitle}\n{self.body}"




post = Post(1, "Hello", "Intro", "This is the body.")
print(post)          # calls __str__()
print(repr(post))    # calls __repr__()


