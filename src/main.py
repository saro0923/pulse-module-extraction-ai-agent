from crawler import crawl_docs
from content_extractor import extract_content
from module_builder import build_modules
from llm_agent import (
    generate_description,
    is_valid_module,
    map_to_core_module
)
import json
import os

START_URL = "https://wordpress.org/documentation/"

pages = crawl_docs(START_URL)

# Dict for semantic grouping + deduplication
final_output = {}

for url in pages:
    text = extract_content(url)
    if not text:
        continue

    modules = build_modules(text)

    for module, subs in modules.items():

        # 1️⃣ Noise filtering agent
        if not is_valid_module(module):
            continue

        # 2️⃣ Semantic mapping agent
        core_module = map_to_core_module(module)
        if not core_module:
            continue

        key = core_module.lower()

        # 3️⃣ Create core module once
        if key not in final_output:
            final_output[key] = {
                "module": core_module,
                "Description": generate_description(core_module),
                "Submodules": {}
            }

        # 4️⃣ Merge submodules under core module
        for sub in subs:
            final_output[key]["Submodules"][sub] = generate_description(sub)

# Save output
os.makedirs("output", exist_ok=True)
with open("output/wordpress_docs.json", "w", encoding="utf-8") as f:
    json.dump(list(final_output.values()), f, indent=2)

print("✅ Extraction completed. Output saved in output/wordpress_docs.json")
