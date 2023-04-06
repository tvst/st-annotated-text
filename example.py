import streamlit as st
from annotated_text import annotated_text



"""
# Annotated Text

This app shows off the [Annotated Text component](https://github.com/tvst/st-annotated-text) for
Streamlit.

If you want to try this at home, you'll first need to install it:

```python
pip install st-annotated-text
```


## Basic example

Annotations are just tuples:
"""

with st.echo():
    from annotated_text import annotated_text

    annotated_text(
        "This ",
        ("is", "Verb"),
        " some ",
        ("annotated", "Adj"),
        ("text", "Noun"),
        " for those of ",
        ("you", "Pronoun"),
        " who ",
        ("like", "Verb"),
        " this sort of ",
        ("thing", "Noun"),
        ". ",
        "And here's a ",
        ("word", ""),
        " with a fancy background but no label.",
    )

""

"""
## Nested arguments

You can also pass lists (and lists within lists!) as an argument:
"""


with st.echo():
    my_list = [
        "Hello ",
        [
            "my ",
            ("dear", "Adj"),
            " ",
        ],
        ("world", "Noun"),
        ".",
    ]

    annotated_text(my_list)


""
""

"""
## Customization
"""

"""
### Custom colors

If the annotation tuple has more than 2 items, the 3rd will be used as the background color and the 4th as the foreground color:
"""

with st.echo():
    annotated_text(
        "This ",
        ("is", "Verb", "#8ef"),
        " some ",
        ("annotated", "Adj", "#faa"),
        ("text", "Noun", "#afa"),
        " for those of ",
        ("you", "Pronoun", "#fea"),
        " who ",
        ("like", "Verb", "#8ef"),
        " this sort of ",
        ("thing", "Noun", "#afa"),
        ". "
        "And here's a ",
        ("word", "", "#faf"),
        " with a fancy background but no label.",
    )

""
""

"""
### Custom styles

You can customize a bunch of different styles by overriding the variables
set in the `annotated_text.parameters` module. For example:

```python
from annotated_text import annotated_text, parameters

parameters.SHOW_LABEL_SEPARATOR = False
parameters.BORDER_RADIUS = 0
parameters.PADDING = "0 0.25rem"
```

For more configurable parameters, see the
[parameters.py source file](https://github.com/tvst/st-annotated-text/blob/master/annotated_text/parameters.py).
"""

""
""

"""
### Even more customization

If you want to go beyond the customizations above, you can bring your own CSS!
  
```python
from annotated_text import annotated_text, annotation

annotated_text(
  "Hello ",
  annotation("world!", "noun", font_family="Comic Sans MS", border="2px dashed red"),
)
```
