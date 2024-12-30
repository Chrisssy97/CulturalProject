# CulturalProject

Below are instructions to using the file.

To run the script to generate lesson plans
1. Open a command line terminal
2. cd into this CulturalProject directory
3. Install necessary packages: pip3 install -r requirements.txt
4. run script: python3 query_with_output_saving.py

To score lessons generated:
python3 score_lesson.py

Background

We evaluate the following LLMs: 
(a) GPT4 queried via API between Oct 1 and <end date> 2024.

We generate a maximum of 1000 tokens for each individual lesson plan generation.

Prompting:
For a given culture and topic, we ask GPT to generate a complete 2nd-grade math lesson on the topic with a culturally relevant context for the given culture, including three sections: introduction, math breakdown, and conclusion. A multiple choice question is included for each section. 


We use three individual prompting strategies to query GPT: (a) 0-shot, where we ask GPT to generate the lesson plan according to the above base prompt without additional information. (b) few-shot with examples, where we make 4 example course plans that are approved by human experts, and given them to GPT as examples to follow while generating lesson plans. (c) few-shot with culture knowledge, where we give base cultural knowledge for each individual culture (more documentation on the given cultural knowledge here) in the prompting.

For each combination of (prompting strategy, culture, topic), we generate 1 lesson for GPT. We then aggregate all output lesson plans and analyze the result.

