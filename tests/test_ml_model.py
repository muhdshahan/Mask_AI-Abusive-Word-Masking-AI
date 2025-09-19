""" unit tests for mask_abusive_words, is_toxic """

from src.train import is_toxic, mask_abusive_words
import pytest

@pytest.fixture
def text1():
    """ Fixed text for reusing using fixture """
    return "Hello friend, have a nice day!"

def test_toxicity_false(text1):
    """ Testing if text is clean """
    assert is_toxic(text1, 0.5) is False

def test_mask_abusive_false(text1):
    """ Testing clean text = original text """
    masked = mask_abusive_words(text1, 0.5)
    assert masked == text1

@pytest.fixture
def text2():
    """ Fixed text for reusing using fixture """
    return "You are an idiot"

def test_toxicity_true(text2):
    """ Testing if text is toxic """
    assert is_toxic(text2, 0.5) is True

def test_mask_abusive(text2):
    """ Testing cleaned text != original text """
    masked = mask_abusive_words(text2, 0.5)
    assert "idiot" not in masked
    assert "*" in masked
    assert "are" in masked
