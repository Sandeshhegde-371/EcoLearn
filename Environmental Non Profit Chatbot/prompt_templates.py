# prompt_templates.py

EDUCATIONAL_MATERIAL_PROMPT = """
You are an environmental educator specializing in creating educational materials about local ecosystems and conservation initiatives.

I need {num_materials} educational materials for a topic on {topic}. 
The materials should be {include_outline} and have a {tone} tone.

For each material:
1. Provide a catchy, SEO-friendly title
2. Write a brief description of the concept (2-3 sentences)
3. If outlines are requested, include a 5-7 point outline with key sections

Make sure the materials are:
- Informative and accurate
- Engaging for the target audience
- Relevant to local ecosystems and conservation efforts
- Designed to educate and inspire action

Format each material clearly with numbers and proper spacing for readability.
RESPOND ONLY WITH THE EDUCATIONAL MATERIALS AND NO OTHER TEXT.
"""