import json
from src.utils.llm_utils import chat
from src.utils.food_utils import get_nutrition_facts_by_name

USER_PROFILE = {
    "dietary_restrictions": ["vegan"],
    "fitness_goal": "muscle gain",
    "preferred_foods": ["banana", "quinoa"]
}

REPLY_PROMPT = (
    "You are a helpful answering assistant.\n"
    "Your task is to provide concise and polite answers. Consider the user's dietary restrictions and fitness goals while responding.\n"
    "Answer in plain text (concise, maximum 3 sentences) and not in Markdown format."
)

def handle_function_call(inquiry):
    if inquiry.lower().startswith("what are the nutritions of this food"):
        food_name = inquiry.split("food")[-1].strip()
        if food_name:
            return get_nutrition_facts_by_name(food_name)
        else:
            return {"error": "Please provide a valid food name."}
    elif inquiry.lower().startswith("what should i eat for"):
        goal = inquiry.split("for")[-1].strip()
        if goal in USER_PROFILE.get("fitness_goal", "").lower():
            return {"suggestion": f"Based on your goal of {goal}, consider eating more {', '.join(USER_PROFILE['preferred_foods'])}."}
        else:
            return {"error": "Goal not recognized. Please clarify your fitness goal."}
    return None

def reply(context):
    inquiry = context["inquiry"]
    history = context["history"]
    stream = context["stream"]

    function_call_result = handle_function_call(inquiry)
    if function_call_result:
        return json.dumps(function_call_result)

    messages = [{"role": "system", "content": REPLY_PROMPT}]
    relevant_history = history[-4:]
    for msg in relevant_history:
        messages.append({"role": "user", "content": msg["inquiry"]})
        messages.append({"role": "assistant", "content": msg["answer"]})
    messages.append({"role": "user", "content": inquiry})

    answer = chat(messages, stream)
    return answer

