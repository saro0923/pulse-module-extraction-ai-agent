def build_modules(text):
    lines = text.split("\n")
    modules = {}
    current_module = None

    for line in lines:
        line = line.strip()

        # Detect module (short heading-like lines)
        if 3 <= len(line.split()) <= 8 and line[0].isupper():
            current_module = line
            modules[current_module] = []

        # Detect submodules (bullet points or short action lines)
        elif current_module and (line.startswith("-") or line.startswith("•")):
            modules[current_module].append(line.lstrip("-• ").strip())

    return modules
