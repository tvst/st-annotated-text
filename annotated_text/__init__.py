import streamlit.components.v1

from htbuilder import H, HtmlElement, styles
from htbuilder.units import unit

# Only works in 3.7+: from htbuilder import div, span
div = H.div
span = H.span

# Only works in 3.7+: from htbuilder.units import px, rem, em
px = unit.px
rem = unit.rem
em = unit.em


def annotation(body, label="", background="#ddd", color="#333", **style):
    """Build an HtmlElement span object with the given body and annotation label.

    The end result will look something like this:

        [body | label]

    Parameters
    ----------
    body : string
        The string to put in the "body" part of the annotation.
    label : string
        The string to put in the "label" part of the annotation.
    background : string
        The color to use for the background "chip" containing this annotation.
    color : string
        The color to use for the body and label text.
    **style : dict
        Any CSS you want to use to customize the containing "chip".

    Examples
    --------

    Produce a simple annotation with default colors:

    >>> annotation("apple", "fruit")

    Produce an annotation with custom colors:

    >>> annotation("apple", "fruit", background="#FF0", color="black")

    Produce an annotation with crazy CSS:

    >>> annotation("apple", "fruit", background="#FF0", border="1px dashed red")

    """

    if "font_family" not in style:
        style["font_family"] = "sans-serif"

    return span(
        style=styles(
            background=background,
            border_radius=rem(0.33),
            color=color,
            padding=(rem(0.17), rem(0.67)),
            display="inline-flex",
            justify_content="center",
            align_items="center",
            **style,
        )
    )(
        body,
        span(
            style=styles(
                color=color,
                font_size=em(0.67),
                opacity=0.5,
                padding_left=rem(0.5),
                text_transform="uppercase",
                margin_bottom=px(-2),
            )
        )(label)
    )


def annotated_text(*args, **st_html_kwargs):
    """Writes test with annotations into your Streamlit app.

    Parameters
    ----------
    *args : str, tuple or htbuilder.HtmlElement
        Arguments can be:
        - strings, to draw the string as-is on the screen.
        - tuples of the form (main_text, annotation_text, background, color) where
          background and foreground colors are optional and should be an CSS-valid string such as
          "#aabbcc" or "rgb(10, 20, 30)"
        - HtmlElement objects in case you want to customize the annotations further. In particular,
          you can import the `annotation()` function from this module to easily produce annotations
          whose CSS you can customize via keyword arguments.

    Examples
    --------

    >>> annotated_text(
    ...     "This ",
    ...     ("is", "verb", "#8ef"),
    ...     " some ",
    ...     ("annotated", "adj", "#faa"),
    ...     ("text", "noun", "#afa"),
    ...     " for those of ",
    ...     ("you", "pronoun", "#fea"),
    ...     " who ",
    ...     ("like", "verb", "#8ef"),
    ...     " this sort of ",
    ...     ("thing", "noun", "#afa"),
    ... )

    >>> annotated_text(
    ...     "Hello ",
    ...     annotation("world!", "noun", color="#8ef", border="1px dashed red"),
    ... )

    """
    out = div(style=styles(
        font_family="sans-serif",
        line_height="1.5",
        font_size=px(16),
    ))

    for arg in args:
        if isinstance(arg, str):
            out(arg)

        elif isinstance(arg, HtmlElement):
            out(arg)

        elif isinstance(arg, tuple):
            out(annotation(*arg))

        else:
            raise Exception("Oh noes!")

    streamlit.components.v1.html(str(out), **st_html_kwargs)
