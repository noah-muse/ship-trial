"""Small text utilities used for the Claude Ship trial."""


def slugify(text: str) -> str:
    """Lowercase the text and join words with hyphens."""
    words = []
    current = []
    for ch in text.lower():
        if ch.isalnum():
            current.append(ch)
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    return "-".join(words)


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def truncate(text: str, limit: int) -> str:
    """Truncate text to at most `limit` characters, adding an ellipsis."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if len(text) <= limit:
        return text
    if limit <= 3:
        return text[:limit]
    return text[: limit - 3] + "..."
