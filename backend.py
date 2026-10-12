from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class BMI(TypedDict):
    weight: float
    height: float
    bmi: float
    category: str


def bmi(state: BMI) -> BMI:
    weight_kg = state["weight"]
    height_m = state["height"]

    bmi_value = weight_kg / (height_m ** 2)
    state["bmi"] = round(bmi_value, 2)

    return state


def category(state: BMI) -> BMI:
    bmi_value = state["bmi"]

    if bmi_value < 18.5:
        state["category"] = "Underweight"
    elif bmi_value < 25:
        state["category"] = "Normal weight"
    elif bmi_value < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"

    return state


graph = StateGraph(BMI)

graph.add_node("bmi", bmi)
graph.add_node("category", category)

graph.add_edge(START, "bmi")
graph.add_edge("bmi", "category")
graph.add_edge("category", END)

workflow = graph.compile()


def calculate_bmi(weight: float, height: float) -> dict:
    result = workflow.invoke({
        "weight": weight,
        "height": height,
        "bmi": 0.0,
        "category": ""
    })

    return result
