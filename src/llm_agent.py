import re

def is_valid_module(module_name: str) -> bool:
    blacklist_keywords = [
        "search", "submit", "see all", "sponsored",
        "december", "november", "january",
        "people of", "month in", "release",
        "faq", "date", "copyright"
    ]

    name = module_name.lower()

    if any(bad in name for bad in blacklist_keywords):
        return False

    if len(module_name.split()) > 10:
        return False

    if re.match(r"^\d", module_name):
        return False

    return True

CORE_MODULES = {
    "Getting Started": [
        "get started", "first steps", "where to start",
        "introduction", "learn about"
    ],
    "Publishing": [
        "publish", "post", "page", "blog", "content"
    ],
    "Appearance": [
        "theme", "appearance", "layout", "design",
        "header", "menu", "widget"
    ],
    "Plugins": [
        "plugin", "extend", "addon"
    ],
    "Media": [
        "image", "gallery", "media", "video", "file"
    ],
    "Security": [
        "security", "https", "password", "login"
    ],
    "Maintenance": [
        "maintenance", "update", "auto-update"
    ],
    "Community": [
        "community", "contributor", "five for the future"
    ],
    "Development": [
        "developer", "block", "editor", "pattern", "api"
    ]
}


def map_to_core_module(module_name: str):
    """
    Maps noisy headings to core product modules.
    Returns None if not relevant.
    """
    name = module_name.lower()

    for core_module, keywords in CORE_MODULES.items():
        if any(keyword in name for keyword in keywords):
            return core_module

    return None

def generate_description(name: str) -> str:
    return f"This module handles functionality related to {name.lower()}."
