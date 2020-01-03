from requirements.action import Action
from requirements.avoidance import Avoidance
from requirements.continuous_action import ContinuousAction
from requirements.landing import Landing


def generate_requirements(reqs):

    requirements = []

    for r in reqs:
        i = r["id"]
        c = r["class"]

        if c == "ACTION":

            a = r["area"]
            requirements.append(Action(i, a))

        elif c == "CONT_ACTION":

            a1 = r["area_1"]
            a2 = r["area_2"]
            requirements.append(ContinuousAction(i, a1, a2))

        elif c == "LANDING":

            a = r["area"]
            requirements.append(Landing(i, a))

        elif c == "AVOIDANCE":

            a = r["area"]
            requirements.append(Avoidance(i, a))

    return requirements
