import re
import openai
import pandas as pd

# Set the OpenAI API key
# paste your API key here
API_KEY = "" 
openai.api_key = API_KEY

# Define the 2nd-grade math topics here
math_topics = [
    "Count to 100 by ones and by tens",
    "Count forward beginning from a given number within the known sequence",
    "Write numbers from 0 to 20 and represent objects with numerals",
    "Understand that each successive number name refers to a larger quantity",
    "Compare two numbers between 1 and 10 presented as written numerals"
]

# Define the cultural elements used in counting here
cultural_elements = ["name", "place", "food", "clothing", "slang", "time", "religion"]

# Define the cultures for which you want to generate classes here
cultures = ["Chinese", "African American", "Hispanic", "Caribbean", "Hindu"]

# Define the different prompting strategies you want to use here
prompting_strategies = ["0-shot", "few-shot with example", "few-shot with culture knowledge"]

# Example lesson to use in few-shot with example prompting strategy. 
# These will be given to the LLM as examples to follow for generating outputs
example_lesson_1 = """
Culture-Based Math Lesson 
Target Grade Level: 2nd Grade
Topic: Numbers and Operations/Base Ten
National Standard Unit Number: CCSS.MATH.CONTENT
Step 1 Introduction: 
“Today, our class took a field trip to the Baltimore National Zoo! We saw so many cool animals and had a great time but your classmates, and I can't remember how many animals, we saw in each exhibit. Can you help us remember? 
Zyharra saw 1 red parrot at the zoo, and Caesar saw 5 blue parrots.
How many parrots did they see in total?”
Multiple Choice Answers: 
Together, Zyharra and Caesar saw 6 parrots
Zyharra and Caesar saw 3 parrots
Zyharra and Caesar saw 4 parrots
Zyharra and Caesar saw 9 parrots
  Step 2: Math Breakdown
Johan has never seen any giraffes in Baltimore so he really wants to remember how many animals he saw at the zoo, he first saw 5 tall giraffes at the zoo.
Then he saw 2 small baby giraffes.
How many total giraffes did she see at the zoo?
Multiple Choice Answers: 

Johan saw 7 giraffes in total.
Johan saw 10 giraffes
Johan saw 3 giraffes
Johan saw 12 giraffes

Step 3: Conclusion
Gabrielle  and Carlos have seen monkeys in El Salvador but have also seen monkeys at the Baltimore City Zoo, Gabrielle saw 11 monkeys swinging in the zoo, then 2 of them stopped swinging to eat bananas. How many monkeys are still swinging?
There are still 9 monkeys swinging
There are still 7 monkeys swinging
There are still 4 monkeys swinging
There are still 3 monkeys swinging

"""

example_lesson_2 = """
Culture-Based Math Lesson
Target Grade Level: 2nd Grade
Topic: Numbers and Operations/Base Ten
National Standard Unit Number: CCSS.MATH.CONTENT.2.NBT.B.5
Step 1: Introduction
“Today, we’re learning about patterns through the world of African American music! Did you know that rhythm is a big part of music styles like jazz and hip-hop? Let’s explore some number patterns using rhythms, just like musicians do.
Here’s a pattern: 2, 4, 6, __, __. Can you help complete this pattern?"
Multiple Choice Answers:
A) 8, 10
B) 6, 7
C) 10, 12
D) 4, 8
Step 2: Math Breakdown
"Rhythm patterns can be found in songs we hear every day. Let’s look at another example. Imagine a musician is tapping out a beat that goes 1, 2, 1, 2, __, __. What numbers should come next to continue the pattern?"
Multiple Choice Answers:
A) 1, 2
B) 2, 3
C) 3, 4
D) 1, 1
Step 3: Conclusion
"Great job with the rhythm patterns! Let’s try one last example. A jazz drummer is tapping out a beat: 3, 6, 9, __, __. How does this pattern continue?"
Multiple Choice Answers:
A) 9, 12
B) 12, 15
C) 10, 11
D) 15, 18

"""

example_lesson_3 = """
Culture-Based Math Lesson
Target Grade Level: 2nd Grade
Topic: Fractions and Measurement
National Standard Unit Number: CCSS.MATH.CONTENT.2.G.A.3
Step 1: Introduction
“Today, we’re learning about fractions using a popular African American Soul Food dessert—sweet potato pie! Fractions help us measure the ingredients for our pie.
If we have 1/2 cup of sugar, and we want to add another 1/2 cup, how much sugar do we have in total?”
Multiple Choice Answers:
A) 1 cup
B) 1/2 cup
C) 2 cups
D) 1/4 cup
Step 2: Math Breakdown
"If the recipe needs 1/4 teaspoon of nutmeg and we add another 1/4 teaspoon, what is the total amount of nutmeg?"
Multiple Choice Answers:
A) 1/2 teaspoon
B) 1/4 teaspoon
C) 3/4 teaspoon
D) 1 teaspoon
Step 3: Conclusion
"Now, if a recipe calls for 1/3 cup of milk, but we only have 2/3 cup, do we have enough for one pie or two pies?"
Multiple Choice Answers:
A) One pie
B) Two pies
C) Half a pie
D) None

"""

example_lesson_4 = """
Culture-Based Math Lesson
Target Grade Level: 2nd Grade
Topic: Measurement and Distance
National Standard Unit Number: CCSS.MATH.CONTENT.2.MD.A.1
Step 1: Introduction
“Today, we’re going to learn about distance by talking about a significant event in African American history called the Great Migration. Where many families traveled from the South to the North.
If one family traveled 300 miles from Georgia to Tennessee and then 200 more miles to Chicago, how far did they travel in total?”
Multiple Choice Answers:
A) 500 miles
B) 600 miles
C) 700 miles
D) 400 miles
Step 2: Math Breakdown
"Another family traveled 150 miles from Mississippi to Alabama and then 350 miles to Detroit. How many miles did they travel in total?"
Multiple Choice Answers:
A) 450 miles
B) 500 miles
C) 300 miles
D) 400 miles
Step 3: Conclusion
"If a family has already traveled 600 miles of their 1,000-mile journey, how many more miles do they need to travel?"
Multiple Choice Answers:
A) 400 miles
B) 300 miles
C) 500 miles
D) 200 miles

"""

# Define cultural knowledge base here
# This will be given to the LLM for few-shot with culture knowledge prompting strategy.
# For example, you can replace this with RAG
culture_knowledge_base = """
Culture is a set of learned expectations which allow us to intepret and value behavior. 
Culture teaches us how to act, what's ok and what's not ok, what to value, what not to value, and what to share with others.
In general, cultural identities include: status (social, economic, position), affliations (family, work, organizations),
demographic (age/generation, gender, geographic location), ethnographic (religion, ethnicity, country of origin, country of residence). 
"""

# Function to generate a lesson plan, for a given (topic, culture, prompting strategy).
def generate_lesson(topic, culture, strategy):
    # You can change the overall prompt here which will be send to LLM API.
    prompt = f"""Generate a complete 2nd-grade math lesson on '{topic}' with a culturally relevant context for {culture} culture, 
                    including Introduction, Math Breakdown, and Conclusion. 
                    Include a multiple choice question for each section. 
                    Make the class appropriate for 2nd grade.
                """

    if strategy == "0-shot":
        full_prompt = prompt
    elif strategy == "few-shot with example":
        full_prompt = f"""{culture_knowledge_base}
        Using the example lessons below, {prompt}\n
        example 1: {example_lesson_1}. 
        example 2: {example_lesson_2}. 
        example 3: {example_lesson_3}. 
        example 4: {example_lesson_4}. 
        These lessons focus on problem-solving with multiple-choice answers to engage students while connecting math concepts to cultural and historical themes."""
    elif strategy == "few-shot with culture knowledge":
        cultural_knowledge = {
            "Chinese": "With knowledge of Chinese culture, like Lunar New Year, dragons, and traditional foods like dumplings...",
            "African American": "With knowledge of African American culture, including music, history, and community traditions..."
        }
        full_prompt = f"{culture_knowledge_base}{cultural_knowledge[culture]} {prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=1000
    )
    
    return response['choices'][0]['message']['content'].strip()

# Function to score the lesson based on cultural appropriateness
def score_lesson(lesson, culture):
    prompt = f"""
    The following is a math course plan for 2nd graders. Please check if the plan mentions any of the following cultural categories: name, place, food, clothing, slang, time, religion.
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

# Function to save all lessons to a single text file with index
def save_all_lessons_to_file(run_index, index, lesson, culture, strategy, filename="all_lessons.csv"):
    # filename = f"all_lessons_{run_index}.csv"
    with open(filename, "a") as f:
        f.write(f"Lesson {index} - Culture: {culture}, Strategy: {strategy}\n")
        f.write(lesson)
        f.write("\n" + "="*50 + "\n")  # Separate lessons with a line of "=" for clarity


# Function to save the scores to a CSV file
def save_scores_to_csv(run_index, scores, filename="lesson_scores.csv"):
    filename = f"lesson_scores_{run_index}.csv"
    df = pd.DataFrame(scores)
    df.to_csv(filename, index=False)

# Main workflow
def main(run_index):
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
                # Generate the full lesson in one go
                full_lesson = generate_lesson(topic, culture, strategy)
                
                # Save the lesson to the single file with index
                save_all_lessons_to_file(run_index, index, full_lesson, culture, strategy, lesson_filename)
                
                # Score the lesson
                score_dict, total_score = score_lesson(full_lesson, culture)
                
                # Collect score data
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
    save_scores_to_csv(run_index, scores)


# Run the main fnuction
# Currently, the function is only run 1 time, so you will only get 1 output txt file
# you can run the entire script multiple times by changing the "i" in range(i) if you want to look at outputs across runs.
if __name__ == "__main__":
    for i in range(1):
        main(i)
