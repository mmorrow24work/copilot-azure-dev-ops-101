def greeting(name: str = "Azure DevOps learner") -> str:
    """Return a deterministic greeting."""
    clean = name.strip() or "Azure DevOps learner"
    return f"Hello, {clean}!"
