import names
import random


def make_random_choice_of_roles() -> str:
    roles = [names.NAME_NAUGHTS, names.NAME_CROSSES]
    user_role, program_role = random.sample(roles, 2)
    return user_role, program_role


def swich_player_for_next_step(current_player: str) ->str:
    return names.USERS_STEP if current_player==names.PROGRAMS_STEP else names.PROGRAMS_STEP


def decide_who_makes_next_step(user_role: str) -> str:
    return names.USERS_STEP if user_role==names.NAME_CROSSES else names.PROGRAMS_STEP