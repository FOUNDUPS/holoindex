"""
HoloIndex - Semantic code retrieval for FoundUps.

Usage:
    from holoindex import HoloIndex

    holo = HoloIndex(vector_path="./vectors")
    holo.index_documents(roots=["./src"])
    results = holo.search("query", limit=5)
"""

from holoindex.core import HoloIndex

__version__ = "0.1.0"
__all__ = ["HoloIndex"]
