from htbuilder import H, styles
import html

span = H.span

import annotated_text.parameters as p

default_style_args = dict(display="inline-flex",
                flex_direction="row",
                align_items="center",
                border_radius=p.BORDER_RADIUS,
                padding=p.PADDING,
                overflow="hidden",
                line_height=1,)


def map_strategy(body, newline_mode, background, color_style, style, label_element):
    '''Maps options to newline handling versions'''
    mapping={'old' : wrap_with_default_flex,
             'flex': newlines_to_br,
             'multiline': multiline
    }

    return mapping[newline_mode](body, background, color_style, style, label_element)

def style_and_span(out, background, color_style, style, label_element):
    '''Universal output span formater'''
    merged_styles = {**default_style_args, 
                     'background-color':background , 
                     **color_style, 
                     **style}
    return (
        span(
            style=styles(**merged_styles),
        )(
        out,
        label_element,
        )
    )

def wrap_with_default_flex(body, background, color_style, style, label_element):
    '''Default behavior without newlines processing'''
    out = html.escape(body)
    return style_and_span(out, background, color_style, style, label_element)
        
def newlines_to_br(body, background, color_style, style, label_element):
    '''Preprocess newlines to HTML complatible form with replace'''
    body_new=H.raw(html.escape(body).replace("\n", "<br>"))
    return style_and_span(body_new, background, color_style, style, label_element)  
    
def multiline(body, background, color_style, style, label_element):
    '''Split to separate lines by \n with inline display'''
    parts = body.split("\n")
    style_new = {**default_style_args, 'display': "inline", **style}
    spans = [style_and_span(part, background, color_style, style_new, '') for part in parts[:-1]]
    spans.append(style_and_span(parts[-1], background, color_style, style_new, label_element))
    
    content = H.raw("<br>".join([str(s) for s in spans]))
    
    return span()(content, '')