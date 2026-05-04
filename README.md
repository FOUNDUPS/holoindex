# HoloIndex

Semantic code retrieval and project memory substrate for the FoundUps ecosystem.

## Installation

```bash
pip install holoindex
```

## Quick Start

```python
from holoindex import HoloIndex

# Initialize with vector storage path
holo = HoloIndex(vector_path="./vectors")

# Index your codebase
holo.index_documents(roots=["./src"])

# Search
results = holo.search("authentication middleware", limit=5)
for r in results:
    print(f"{r['path']}: {r['similarity']:.2f}")
```

## Features

- **Semantic Search**: Find code by meaning, not just keywords
- **ChromaDB Backend**: Persistent vector storage
- **Sentence Transformers**: State-of-the-art embeddings
- **Hybrid Scoring**: Combines semantic + keyword relevance

## Configuration

```python
# Use custom embedding model
holo = HoloIndex(
    vector_path="./vectors",
    model_name="all-MiniLM-L6-v2",
)

# Configure similarity threshold
results = holo.search("query", min_similarity=0.5)
```

## License

MIT - See LICENSE for details.

## Links

- [FoundUps](https://foundups.com)
- [Documentation](https://github.com/FOUNDUPS/holoindex)
