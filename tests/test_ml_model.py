# unit tests for mask_abusive_words, is_toxic

import pytest
from src.train import is_toxic, mask_abusive_words

@pytest.fixture
def text1():
    return "Hello friend, have a nice day!"

def test_toxicity_false(text1):
    assert is_toxic(text1, 0.5) is False

def test_mask_abusive_true(text1):
    masked = mask_abusive_words(text1, 0.5)
    assert masked == text1

@pytest.fixture
def text2():
    return "You are an idiot"

def test_toxicity_true(text2):
    assert is_toxic(text2, 0.5) is True

def test_mask_abusive(text2):
    masked = mask_abusive_words(text2, 0.5) 
    assert "idiot" not in masked
    assert "*" in masked
    assert "are" in masked


