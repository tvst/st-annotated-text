import streamlit as st
from annotated_text import annotated_text



"""
# Annotated Text

## Basic example
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
