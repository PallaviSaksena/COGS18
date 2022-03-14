"""Test for my functions.

I wrote tests for all of my functions, but the last three functions call on other functions and are harder to test.
Just the first few functions can be used to check for the project requirements.
"""

import functions as f
from functions import character_list

import mock
import builtins


def test_pick_character():
    assert type(f.pick_character(character_list)) == str
    assert len(f.pick_character(character_list)) > 0
    assert f.pick_character(character_list) in character_list


def test_scramble_names():
    
    test_string = 'BLACK WIDOW'
    
    assert type(f.scramble_names(test_string)) == str
    assert len(f.scramble_names(test_string)) == len(test_string)
    
    
def test_change_case():
    
    assert f.change_case('iron man') == 'IRON MAN'
    assert f.change_case('Quit') == 'QUIT'
    assert f.change_case('GIVE UP') == 'GIVE UP'
    
    
def test_compare_response():
    assert f.compare_response('IRON MAN', 'IRON MAN') == 'Correct!'
    assert f.compare_response('IRON MAN', 'HULK') == 'Incorrect. The answer is IRON MAN'
    assert f.compare_response('IRON MAN', 'QUIT') == 'Goodbye!'
    assert f.compare_response('IRON MAN', 'GIVE UP') == 'The answer is IRON MAN'
    assert f.compare_response('IRON MAN', 1308) == 'Incorrect. The answer is IRON MAN'
    
    
def test_add_score():
    
    assert callable(f.add_score)
    assert type(f.add_score('IRON MAN', 'IRON MAN')) == int
    assert f.add_score('IRON MAN', 'IRON MAN') > 0
    # score should be > 0 if character_name matches response
        # score = 1 the first time you run it, score = 2 the second time, etc.
    

def test_play_game():
    assert callable(f.play_game)
    
    with mock.patch.object(builtins, 'input', lambda _: 'IRON MAN'):
        assert type(f.play_game(character_list)) == tuple
        assert len(f.play_game(character_list)) == 3
    

def test_run_chat():
    assert callable(f.run_chat)