import os
import openai
from app import config

openai.api_key = config.OPENAI_API_KEY


def generate_blog(prompt):
    sections = generate_blog_sections(prompt)
    secs = [i for i in sections.split('\n') if i != '']

    res = ''
    for s in secs:
        res += "<h3>" + s.upper() + "</h3>"
        res += "<p>" + blog_section_expander(s) + "</p>" + "\n\n"

    return res


def generate_blog_sections(prompt):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Give an outline of the blog sections of a blog about: {}".format(
            prompt),
        temperature=0.8,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']


def blog_section_expander(prompt):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Expand the blog section about {} into a detailed explanation".format(
            prompt),
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']
