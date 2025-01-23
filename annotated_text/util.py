import html

from htbuilder import H, HtmlElement, styles
from htbuilder.units import unit

from .handler import map_strategy

# This works in 3.7+:
# from htbuilder import span
#
# ...so we use the 3.7 version of the code above here:
try:
    span = H.span
except AttributeError:
    from htbuilder import span

import annotated_text.parameters as p

def annotation(body, label="", background=None, color=None, newline_mode="old", **style):
    """Build an HtmlElement span object with the given body and annotation label.

    The end result will look something like this:

        [body | label]

    Parameters
    ----------
    body : string
        The string to put in the "body" part of the annotation.
    label : string
        The string to put in the "label" part of the annotation.
    background : string or None
        The color to use for the background "chip" containing this annotation.
        If None, will use a random color based on the label.
    color : string or None
        The color to use for the body and label text.
        If None, will use the document's default text color.
    newline_mode : string
        The string that selects display of newlines.
          - 'old' (default) - ignores first consequential \n, background break on second is possible
          - 'flex' - Writes all newlines. Background fixed for both label and content. Each annotation is grouped in a box having the same label on the side (display inline-flex preserved)
          - 'multiline' - Writes all newlines with proper background for content. Lines are preserved (inline-blocks instead of inline-flex).
    style : dict
        Any CSS you want to apply to the containing "chip". This is useful for things like


    Examples
    --------

    Produce a simple annotation with default colors:

    >>> annotation("apple", "fruit")

    Produce an annotation with custom colors:

    >>> annotation("apple", "fruit", background="#FF0", color="black")

    Produce an annotation with crazy CSS:

    >>> annotation("apple", "fruit", background="#FF0", border="1px dashed red")

    Produce an annotation preserving newlines 
    
    >>> annotation("This is a \n \n test.", "test", newline_mode="multiline")
    
    """

    color_style = {}

    if color:
        color_style['color'] = color

    if background:
        background_color = background
    else:
        label_sum = sum(ord(c) for c in label)
        background_color = p.PALETTE[label_sum % len(p.PALETTE)]
        background_opacity = p.OPACITIES[label_sum % len(p.OPACITIES)]
        background = background_color + background_opacity

    label_element = ""

    if label:
        separator = ""

        if p.SHOW_LABEL_SEPARATOR:
            separator = span(
                style=styles(
                    border_left=f"1px solid",
                    opacity=0.1,
                    margin_left=p.LABEL_SPACING,
                    align_self="stretch",
                )
            ),

        label_element = (
            separator,
            span(
                style=styles(
                    margin_left=p.LABEL_SPACING,
                    font_size=p.LABEL_FONT_SIZE,
                    opacity=p.LABEL_OPACITY,
                )
            )(
                html.escape(label),
            )
        )

    return map_strategy(body, newline_mode, background, color_style, style, label_element)

def get_annotated_html(*args, newline_mode="old"):
    """Writes text with annotations into an HTML string.

    Parameters
    ----------
    *args : see annotated_text()

    Returns
    -------
    str
        An HTML string.
    """

    return str(get_annotated_element(*args, newline_mode=newline_mode))


def get_annotated_element(*args, newline_mode="old"):
    """Writes text with annotations into an HTBuilder HtmlElement object.

    Parameters
    ----------
    *args : see annotated_text()

    Returns
    -------
    HtmlElement
        An HTBuilder HtmlElement object.
    """

    out = span()

    for arg in args:
        if isinstance(arg, str):
            out(html.escape(arg))

        elif isinstance(arg, HtmlElement):
            out(arg)

        elif isinstance(arg, tuple):
            out(annotation(*arg, newline_mode=newline_mode))

        elif isinstance(arg, list):
            out(get_annotated_element(*arg, newline_mode=newline_mode))

        else:
            raise Exception("Oh noes!")

    return out
