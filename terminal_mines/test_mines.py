import unittest
from unittest.mock import MagicMock, patch


from mines import DIFFICULTY_PRESETS, DifficultyParamType
from mines import main as main_function
# import click

class MinesTestCase(unittest.TestCase):
    def test_difficulty_param_type(self):
        difficulty_param_type_obj = DifficultyParamType()
        DIFFICULTY_PRESETS = {
            "balanced": (35, 20, 15),
            "challenging": (70, 25, 20),
            "easy": (10, 8, 8),
            "intermediate": (40, 16, 16),
            "expert": (99, 16, 30)
        }
        self.assertEqual(difficulty_param_type_obj.convert("balanced", None, None), DIFFICULTY_PRESETS["balanced"])
        self.assertEqual(difficulty_param_type_obj.convert("challenging", None, None),  DIFFICULTY_PRESETS["challenging"])
        self.assertEqual(difficulty_param_type_obj.convert("easy", None, None),DIFFICULTY_PRESETS["easy"])
        self.assertEqual(difficulty_param_type_obj.convert("intermediate", None, None), DIFFICULTY_PRESETS["intermediate"])
        self.assertEqual(difficulty_param_type_obj.convert("expert", None, None), DIFFICULTY_PRESETS["expert"])

    def test_difficulty_param_type_custom_difficulty(self):
        difficulty_param_type_obj = DifficultyParamType()
        self.assertEqual(difficulty_param_type_obj.convert("50, 10,10", None, None), (50, 10, 10))

    def test_difficulty_param_type_invalid_difficulty_name(self):
        difficulty_param_type_obj = DifficultyParamType()
        from click import BadParameter
        self.assertRaises(BadParameter, difficulty_param_type_obj.convert, "invalid", None, None)

    def test_difficulty_param_type_invalid_difficulty_name_2(self):
        difficulty_param_type_obj = DifficultyParamType()
        from click import BadParameter
        self.assertRaises(BadParameter, difficulty_param_type_obj.convert, "10,10", None, None)

    def test_difficulty_param_type_invalid_difficulty_name_3(self):
        difficulty_param_type_obj = DifficultyParamType()
        from click import BadParameter
        self.assertRaises(BadParameter, difficulty_param_type_obj.convert, "-1, 10,10", None, None)

    def test_difficulty_param_type_invalid_difficulty_name_4(self):
        difficulty_param_type_obj = DifficultyParamType()
        from click import BadParameter
        self.assertRaises(BadParameter, difficulty_param_type_obj.convert, "5, 55,10", None, None)

    def test_difficulty_param_type_invalid_difficulty_name_5(self):
        difficulty_param_type_obj = DifficultyParamType()
        from click import BadParameter
        self.assertRaises(BadParameter, difficulty_param_type_obj.convert, "101, 10,10", None, None)

