# Pulse – Module Extraction AI Agent

## Overview
This project implements an Agentic AI system that extracts structured modules and submodules
from documentation-based help websites. The system converts unstructured documentation content
into a clean, structured JSON format that can be used by product, engineering, or documentation teams.

The solution is designed to prioritize semantic accuracy and logical grouping over noisy extraction.

---

## Problem Statement
Large documentation websites contain thousands of unstructured pages.
Manually identifying product modules and submodules from this content is time-consuming and error-prone.

The goal of this project is to:
- Automatically crawl documentation websites
- Extract meaningful content
- Identify core product modules
- Group related topics as submodules
- Output a structured JSON representation

---

## Agentic AI Approach
This system follows a multi-stage Agentic AI pipeline:

1. **Crawler Agent**
   - Recursively crawls documentation URLs
   - Collects all relevant internal documentation pages

2. **Content Extraction Agent**
   - Removes headers, footers, navigation, and UI noise
   - Extracts only meaningful documentation text

3. **Filtering Agent**
   - Eliminates irrelevant headings such as dates, UI labels, and marketing slogans
   - Applies rule-based reasoning to retain only valid module candidates

4. **Semantic Taxonomy Agent**
   - Maps extracted headings to core product modules
   - Groups related concepts under a single semantic category

5. **Deduplication & Consolidation Agent**
   - Merges repeated concepts
   - Ensures clean and consistent output

This precision-first approach avoids unreliable or ambiguous submodules.

---

## Input
- One or more documentation URLs  
  Example: https://wordpress.org/documentation/

  ---

## Output
Structured JSON output with the following format:

{
"module": "Module Name",
"Description": "Detailed description of the module",
"Submodules": {
  "Submodule Name": "Detailed description of the submodule"
}
}

Final output file:

output/wordpress_docs.json

Example Output
[
  {
    "module": "Getting Started",
    "Description": "This module handles functionality related to getting started.",
    "Submodules": {}
  },
  {
    "module": "Publishing",
    "Description": "This module handles functionality related to publishing.",
    "Submodules": {}
  }
]

Tech Stack

Python

BeautifulSoup

Requests

Trafilatura

Rule-based Agentic AI logic

Assumptions

Documentation pages are primarily static HTML

English-language documentation

Submodules are included only when semantic confidence is high

Limitations

JavaScript-heavy websites may require browser-based crawling

Very sparse documentation may result in fewer submodules

How to Run
python src/main.py

Demo Video

Loom Demo: https://www.loom.com/share/d06fc4184a0947869b01f1bd420e3c78

