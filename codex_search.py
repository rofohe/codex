#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def search_codex(query, base_url="http://localhost:8080"):
    """Search CODEX and return ranked results."""
    r = requests.get(f"{base_url}/api/search", params={"q": query})
    r.raise_for_status()
    results = r.json()

    for i, s in enumerate(results, 1):
        print(f"\n#{i} [{s['source']}] {s['name']}  ★{'★'*s['importance']}")
        print(f"   {s['description']}")
        print(f"   {s['code'][:120]}{'...' if len(s['code']) > 120 else ''}")

    return results

# Usage in your IDE:
#search_codex("rolling average")
#search_codex("group by")
#search_codex("deploy steps")

