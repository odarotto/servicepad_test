import pytest
import random
from answers import answer_1, answer_2, answer_3

class TestLogic:
    def test_question_1_fizz(self):
        expected_result = ['fizz']
        input_example = [3]
        result = answer_1(input_example)
        assert result[0] == expected_result[0]

    def test_question_1_buzz(self):
        expected_result = ['buzz']
        input_example = [5]
        result = answer_1(input_example)
        assert result[0] == expected_result[0]

    def test_question_1_both(self):
        expected_result = ['fizz buzz']
        input_example = [15]
        result = answer_1(input_example)
        assert result[0] == expected_result[0]

    def test_question_1_full(self):
        results = answer_1()
        for i, result in enumerate(results):
            if i+1 % 3 == 0 and i+1 % 5 == 0:
                assert result == 'fizz buzz'
            if i+1 % 3 == 0:
                assert result == 'fizz'
            if i+1 % 3 == 0:
                assert result == 'buzz'

    def test_question_2_0(self):
        expeted_result = 0
        result = answer_2(0)
        assert expeted_result == result

    def test_question_2_n(self):
        expeted_result = 610
        result = answer_2(15)
        assert expeted_result == result

    def test_question_3_hola_mundo(self):
        expected_result = {
            'hola': 1,
            'mundo': 1
        }
        input_example = 'hola mundo'
        result = answer_3(input_example)
        assert expected_result == result

    def test_question_3_big_text(self):
        text = '''Mango banana apple pear
            Banana grapes strawberry
            Apple pear mango banana
            Kiwi apple mango strawberry'''
        expected_result = {
            'mango': 3,
            'banana': 3,
            'apple': 3,
            'pear': 2,
            'grapes': 1,
            'strawberry': 2,
            'kiwi': 1
        }
        result = answer_3(text)
        assert expected_result == result
