
import random
import constants

def make_random_choice_of_roles() -> str:
    roles = [constants.NAME_NAUGHTS, constants.NAME_CROSSES]
    user_role, program_role = random.sample(roles, 2)
    return user_role, program_role


def swich_player_for_next_step(current_player: str) -> str:
    return constants.USERS_STEP if current_player==constants.PROGRAMS_STEP else constants.PROGRAMS_STEP


def swich_roles_for_next_step(current_role: str) -> str:
    return constants.NAME_CROSSES if current_role==constants.NAME_NAUGHTS else constants.NAME_NAUGHTS


def decide_who_makes_next_step(user_role: str) -> str:
    return constants.USERS_STEP if user_role==constants.NAME_CROSSES else constants.PROGRAMS_STEP