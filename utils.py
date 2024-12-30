import re
import pandas as pd

from constants import *


# Function to score the lesson based on cultural appropriateness
# ***Note: this output of this function should be sanity checked manually, as LLM might not generate 100% reliable counting
def score_lesson(lesson, culture):
    prompt = f"""
    The following is a math course plan for 2nd graders. Please check if the plan mentions any of the following cultural categories: {cultural_elements}.
    Then, determine if the cultural elements are appropriate for the target culture: {culture}. Return the count of mentioning of cultural elements, where negative numbers means inappropriate or
    mistaken mentioning of cultural elements for the target culture. Return the response in the form of a list of integers (only return the list of integers in response, no explanations), corresponding to the count for each cultural category in order
    
    Course Plan: {lesson}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    
    # Capture the score output from the model's response
    scores = response['choices'][0]['message']['content'].strip().split('\n')[0][1:-1].split(",")
    scores = [int(s) for s in scores]
    score_element = zip(cultural_elements, scores)
    score_dict = {elem: s for (elem, s) in score_element}  # Initialize scores for all cultural elements
    total_score = sum(score_dict.values())
    return score_dict, total_score


# Function to save the scores (i.e. counting of appearance of cultural elements) to a CSV file
def save_scores_to_csv(scores, filename="lesson_scores.csv"):
    df = pd.DataFrame(scores)
    df.to_csv(filename, index=False)
