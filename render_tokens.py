import re

def tokenize(text):
    """Split text into tokens (words, numbers, punctuation)."""
    return re.findall(r"\w+|[^\w\s]", text)

def render_tokens(tokens):
    """Print each token with its index."""
    print(f"{'Index':<8} {'Token'}")
    print("-" * 20)
    for i, token in enumerate(tokens):
        print(f"{i:<8} {token!r}")

if __name__ == "__main__":
    sample = "Hello, world! This is a simple token renderer with 3 tokens... and more."
    tokens = tokenize(sample)
    print(f"Input: {sample!r}\n")
    render_tokens(tokens)
    print(f"\nTotal tokens: {len(tokens)}")
