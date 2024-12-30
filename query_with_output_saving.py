import re
import openai
import pandas as pd

from constants import *


# Set the OpenAI API key (imported from constants file)
openai.api_key = API_KEY


# Function to generate a lesson plan from LLM, for a given (topic, culture, prompting strategy).
def generate_lesson(topic, culture, strategy):
    # You can change the overall prompt here which will be send to LLM API.
    prompt = f"""Generate a complete 2nd-grade math lesson on '{topic}' with a culturally relevant context for {culture} culture, 
                    including Introduction, Math Breakdown, and Conclusion. 
                    Include a multiple choice question for each section. 
                    Make the class appropriate for 2nd grade.
                """

    # For each prompting strategy, we might also append additional instructions to LLM after the overall prompt. 
    
    # For 0-shot, we send the prompt as it is
    if strategy == "0-shot":
        full_prompt = prompt
        
    # For few-shot with example, we attach the culture_knowledge_base + example course plans for the LLM to follow. 
    # You can edit the examples / instructions for how the LLM should follow the example below.
    elif strategy == "few-shot with example":
        full_prompt = f"""{culture_knowledge_base}
        Using the example lessons below, {prompt}\n
        example 1: {example_lesson_1}. 
        example 2: {example_lesson_2}. 
        example 3: {example_lesson_3}. 
        example 4: {example_lesson_4}. 
        These lessons focus on problem-solving with multiple-choice answers to engage students while connecting math concepts to cultural and historical themes."""

    # For few-shot with culture knowledge prompting strategy, give it the general definition of cultural knowledge (i.e. culture_knowledge_base)
    # Plus individual cutural knowledge for eac culture
    elif strategy == "few-shot with culture knowledge":
        cultural_knowledge = {
            "Chinese": "With knowledge of Chinese culture, like Lunar New Year, dragons, and traditional foods like dumplings...",
            "African American": "With knowledge of African American culture, including music, history, and community traditions..."
        }
        full_prompt = f"{culture_knowledge_base}{cultural_knowledge[culture]} {prompt}"

    # Actually send the promot to chatgpt and get response back
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=1000
    )
    
    return response['choices'][0]['message']['content'].strip()

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


# Function to save all lessons to a single text file
def save_all_lessons_to_file(index, lesson, culture, strategy, filename="all_lessons.csv"):
    with open(filename, "a") as f:
        f.write(f"Lesson {index} - Culture: {culture}, Strategy: {strategy}\n")
        f.write(lesson)
        f.write("\n" + "="*50 + "\n")  # Separate lessons with a line of "=" for clarity


# Function to save the scores (i.e. counting of appearance of cultural elements) to a CSV file
def save_scores_to_csv(scores, filename="lesson_scores.csv"):
    df = pd.DataFrame(scores)
    df.to_csv(filename, index=False)


# Main workflow
def main():
    lessons = []
    scores = []
    # File to save all lessons
    lesson_filename = "all_lessons.txt"
    
    # Clear the file before writing new lessons (optional)
    open(lesson_filename, 'w').close()
    
    # Generate lessons and score them
    index = 1
    for culture in cultures:
        for topic in math_topics:
            for strategy in prompting_strategies:
                # Generate the full lesson for given (culture, topic, strategy)
                full_lesson = generate_lesson(topic, culture, strategy)
                
                # Save the lesson to the single file with index
                save_all_lessons_to_file(index, full_lesson, culture, strategy, lesson_filename)
                
                # Score the lesson
                score_dict, total_score = score_lesson(full_lesson, culture)
                
                # Collect score data (i.e. counting of cultural elements)
                score_row = {
                    "Lesson_Index": index,
                    "Culture": culture,
                    "Strategy": strategy,
                    **score_dict,
                    "Total_Score": total_score
                }
                scores.append(score_row)
                
                # Increment lesson index
                index += 1
    
    # Save all scores to a CSV file
    save_scores_to_csv(scores)


# Run the main fnuction
if __name__ == "__main__":
    main()
