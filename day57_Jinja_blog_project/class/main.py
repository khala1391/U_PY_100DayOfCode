# main.py

from post import Post

# Create an example Post object
post = Post(
    id=1,
    title="Welcome to My Blog",
    subtitle="Getting started",
    body="This is the very first post on my blog. Stay tuned for more!"
)

# Show what happens when you print
print("Using print():")
print(post)  # Calls __str__()

print("\nUsing repr():")
print(repr(post))  # Calls __repr__()

print("\nInspecting object directly in interactive shell or Jupyter:")
post  # Would display the result of __repr__()
