
import random
from functions.constants import USERS_STEP, PROGRAMS_STEP, NAME_CROSSES, NAME_NAUGHTS

def make_random_choice_of_roles() -> tuple[str, str]:
    roles = [NAME_NAUGHTS, NAME_CROSSES]
    user_role, program_role = random.sample(roles, 2)
    return user_role, program_role


def swich_player_for_next_step(
        current_player: str
        ) -> str:
    return USERS_STEP if current_player == PROGRAMS_STEP else PROGRAMS_STEP


def swich_roles_for_next_step(
        current_role: str
        ) -> str:
    return NAME_CROSSES if current_role == NAME_NAUGHTS else NAME_NAUGHTS


def decide_who_makes_next_step(user_role: str) -> str:
    return USERS_STEP if user_role == NAME_CROSSES else PROGRAMS_STEP