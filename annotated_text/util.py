import html

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

    """

    return (
        span(
            style=styles(
                background=background,
                border_radius=rem(0.33),
                padding=(rem(0.125), rem(0.5)),
                overflow="hidden",
                **style,
            ))(

            span(style=styles(color=color))(
                html.escape(body),
            ),

            span(
                style=styles(
                    padding_left=rem(0.5),
                    text_transform="uppercase",
                ))(
                span(
                    style=styles(
                        font_size=em(0.67),
                        opacity=0.5,
                        color=color,
                    ))(
                    html.escape(label),
                ),
            ),
        )
    )


def get_annotated_html(*args):
    """Writes text with annotations into an HTML string.

    Parameters
    ----------
    *args : see annotated_text()

    Returns
    -------
    str
        An HTML string.
    """


    out = div()

    for arg in args:
        if isinstance(arg, str):
            out(html.escape(arg))

        elif isinstance(arg, HtmlElement):
            out(arg)

        elif isinstance(arg, tuple):
            out(annotation(*arg))

        else:
            raise Exception("Oh noes!")

    return str(out)
