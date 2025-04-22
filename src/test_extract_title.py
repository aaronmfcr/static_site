import pytest
from markdown_blocks import extract_title  

def test_extract_title_with_h1():
    assert extract_title("# Hello") == "Hello"

def test_extract_title_with_whitespace():
    assert extract_title("#   Hello   ") == "Hello"

def test_extract_title_not_first_line():
    assert extract_title("Some text\n# Title") == "Title"

def test_extract_title_raises_error():
    with pytest.raises(Exception):
        extract_title("No title here")
