import streamlit as st
from annotated_text import annotated_text, annotation


"""
# Annotated text example

Below is some annotated text:
"""

with st.echo():
    annotated_text(
        "This ",
        ("is", "verb"),
        " some ",
        ("annotated", "adj"),
        ("text", "noun"),
        " for those of ",
        ("you", "pronoun"),
        " who ",
        ("like", "verb"),
        " this sort of ",
        ("thing", "noun"),
        "."
    )

# Weird, right now there's negative margin at the bottom of all st.markdown.
# Adding this to make up for it, but we should fix it in Streamlit itself.
""

"""
Bam!
"""

"""
And you can also customize colors:
"""

with st.echo():
    annotated_text(
        "This ",
        ("is", "verb", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
        "."
    )
