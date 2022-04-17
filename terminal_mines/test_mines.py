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

class Renderer(unittest.TestCase):
    # INTEGRATION TEST
    def test_render_cell_integration_minefield_normal_cell(self):
        from game_logic.renderer import render_cell
        from game_logic import random_minefield
        from game_logic.game_model import GameState, CellState
        from click import style
        fg_mapping = {
            CellState.FLAGGED: "bright_green",
            CellState.WARN1: "bright_cyan",
            CellState.WARN2: "cyan",
            CellState.WARN3: "bright_blue",
            CellState.WARN4: "bright_magenta",
            CellState.WARN5: "magenta",
            CellState.WARN6: "bright_yellow",
            CellState.WARN7: "red",
            CellState.WARN8: "red",
            CellState.EXPLODED: "bright_red"
        }

        minefield = random_minefield(35, 20, 15)
        minefield.x = 1
        minefield.y = 0
        cell = minefield.get_cell(0, 0)
        bg = None
        fg = fg_mapping.get(cell.state, None)

        self.assertEqual(render_cell(minefield, 0, 0), style(cell.state.value, bg=bg, fg=fg))

    def test_render_cell_integration_minefield_inprogress_game_current_cell(self):
        from game_logic.renderer import render_cell
        from game_logic import random_minefield
        from game_logic.game_model import GameState
        from click import style

        minefield = random_minefield(35, 20, 15)
        minefield.x = 0
        minefield.y = 0

        cell = minefield.get_cell(0, 0)

        minefield.state = GameState.IN_PROGRESS
        bg = "bright_green"
        fg = "black"

        self.assertEqual(render_cell(minefield, 0, 0), style(cell.state.value, bg=bg, fg=fg))

    def test_render_cell_integration_minefield_finished_game_flagged_cell(self):
        from game_logic.renderer import render_cell
        from game_logic import random_minefield
        from game_logic.game_model import GameState, CellState
        from click import style
        fg_mapping = {
            CellState.FLAGGED: "bright_green",
            CellState.WARN1: "bright_cyan",
            CellState.WARN2: "cyan",
            CellState.WARN3: "bright_blue",
            CellState.WARN4: "bright_magenta",
            CellState.WARN5: "magenta",
            CellState.WARN6: "bright_yellow",
            CellState.WARN7: "red",
            CellState.WARN8: "red",
            CellState.EXPLODED: "bright_red"
        }

        minefield = random_minefield(35, 20, 15)

        minefield.flag_cell(0, 0)
        cell = minefield.get_cell(0, 0)
        cell.is_mine = False
        minefield.state = GameState.WON
        bg = "red"
        fg = fg_mapping.get(cell.state, None)
        self.assertEqual(render_cell(minefield, 0, 0), style(cell.state.value, bg=bg, fg=fg))
