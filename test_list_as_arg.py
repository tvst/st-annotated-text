import streamlit as st

from annotated_text import *

annot_text = ["This ", ("is", "verb", "#8ef"), " some ", 
            ("annotated", "adj", "#faa"), ("text", "noun", "#afa"), 
            " for those of ", ("you", "pronoun", "#fea"), " who ", 
            ("like", "verb", "#8ef"), " this sort of ", 
            ("thing", "noun", "#afa"), ]


annotated_text(annot_text)