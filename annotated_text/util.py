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

# Colors from the Streamlit palette.
# These are red-70, orange-70, ..., violet-70, gray-70.
PALETTE = [
    "#ff4b4b",
    "#ffa421",
    "#ffe312",
    "#21c354",
    "#00d4b1",
    "#00c0f2",
    "#1c83e1",
    "#803df5",
    "#808495",
]

OPACITIES = [
    "33", "66",
]

def annotation(body, label="", background=None, color=None, **style):
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

    color_style = {}

    if color:
        color_style['color'] = color

    if not background:
        label_sum = sum(ord(c) for c in label)
        background_color = PALETTE[label_sum % len(PALETTE)]
        background_opacity = OPACITIES[label_sum % len(OPACITIES)]
        background = background_color + background_opacity

    anno = [span(
                style=styles(
                    background=background,
                    border_radius=rem(0.33),
                    padding=(rem(0.125), rem(0.5)),
                    overflow="hidden",
                    **color_style,
                    **style,
                    )
            )(html.escape(body))]

    if label != "":
        anno.append(span(
                style=styles(
                    padding_left=rem(0.5),
                    text_transform="uppercase",
                ))(
                span(
                    style=styles(
                        font_size=em(0.67),
                        opacity=0.5,
                    ))(
                    html.escape(label),
                ),
            ))

    return tuple(anno)


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
