"""Basic tests for HoloIndex standalone package."""

import pytest
from pathlib import Path


def test_import():
    """Test that holoindex can be imported."""
    from holoindex import HoloIndex
    assert HoloIndex is not None


def test_version():
    """Test version is defined."""
    import holoindex
    assert hasattr(holoindex, "__version__")
    assert holoindex.__version__ == "0.1.0"


@pytest.mark.skip(reason="Requires ChromaDB setup")
def test_basic_indexing(tmp_path):
    """Test basic indexing functionality."""
    from holoindex import HoloIndex

    vector_path = tmp_path / "vectors"
    holo = HoloIndex(vector_path=str(vector_path))

    # Create a test file
    test_file = tmp_path / "test.py"
    test_file.write_text("def hello(): return 'world'")

    # Index it
    holo.index_documents(roots=[str(tmp_path)])

    # Search
    results = holo.search("hello function")
    assert len(results) > 0
