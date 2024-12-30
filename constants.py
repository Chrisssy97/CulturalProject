# paste your API key here
API_KEY = "" 

# Chatgpt model version
MODEL = "gpt-4"

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

# Define cultural knowledge base here: i.e. the meaning of cultural knowledge
# This will be given to the LLM for few-shot with cultural knowledge base prompting strategies.
# For example, you can replace this with RAG
culture_knowledge_base = """
Culture is a set of learned expectations which allow us to intepret and value behavior. 
Culture teaches us how to act, what's ok and what's not ok, what to value, what not to value, and what to share with others.
In general, cultural identities include: status (social, economic, position), affliations (family, work, organizations),
demographic (age/generation, gender, geographic location), ethnographic (religion, ethnicity, country of origin, country of residence). 
"""

# Define cultural knowledge for individual culture here
cultural_knowledge = {
    "Chinese": ["Dumplings are a traditional food during Lunar New Year."],
    "African American": ["Jazz and hip-hop are central to African American culture."],
    "Hispanic": [
        "Tacos and tamales are traditional Mexican dishes, often enjoyed during celebrations like Día de los Muertos.",
        "Flan is a popular dessert in many Hispanic countries, symbolizing the shared cultural love for sweet treats.",
        "Mariachi music is an iconic symbol of Mexican culture, often performed during festivals and family gatherings.",
        "Salsa dancing originated in the Caribbean but is widely celebrated in Hispanic culture as a joyful, communal activity.",
        "Día de los Muertos (Day of the Dead) is a Mexican holiday that celebrates loved ones who have passed away, with vibrant altars and offerings.",
        "The Mayan pyramids, such as Chichén Itzá, reflect the rich history of ancient civilizations in Mexico."
    ],
    "Caribbean": [
        "Reggae music, popularized by artists like Bob Marley, is a hallmark of Caribbean culture, particularly in Jamaica.",
        "Carnival is celebrated across the Caribbean with colorful parades, calypso music, and traditional costumes.",
        "Ackee and saltfish is Jamaica's national dish, showcasing the unique flavors of Caribbean cuisine.",
        "The steel drum, or steelpan, is an instrument invented in Trinidad and Tobago and is central to many Caribbean music styles.",
        "The Caribbean Sea is home to rich biodiversity, including coral reefs and tropical fish, making it a vital part of local culture."
    ],
    "Hindu": [
        "Diwali, the festival of lights, is one of the most important Hindu celebrations, symbolizing the victory of light over darkness.",
        "The Bhagavad Gita is a sacred Hindu scripture that offers spiritual guidance and philosophy.",
        "Yoga, a spiritual and physical practice, has its origins in Hindu traditions and emphasizes balance and mindfulness.",
        "Traditional Indian cuisine, such as samosas and curries, is often prepared during Hindu festivals and celebrations.",
        "The Ganges River is considered sacred in Hinduism and is a central part of many religious rituals and traditions."
    ]
}
