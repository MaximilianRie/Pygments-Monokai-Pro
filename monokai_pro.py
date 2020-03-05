# -*- coding: utf-8 -*-
"""
    My take on miming the Monokai Pro theme: https://monokai.pro.
    Add this file to pygments/styles/ and add
    'monokai_pro': 'monokai_pro::MonokaiProStyle'
    to the STYLE_MAP in pygments/styles/__init__.py

    --StealthyNiffler
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class MonokaiProStyle(Style):
    """
    This style mimics the Monokai Pro color scheme.
    """

    background_color = "#363537"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      "#f7f1ff", # class:  ''
        Whitespace:                "",        # class: 'w'
        Error:                     "#fc618d bg:#1e0010", # class: 'err'
        Other:                     "",        # class 'x'

        Comment:                   "#69676c", # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   "#5ad4e6", # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         "#fc618d", # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              "",        # class: 'kt'

        Operator:                  "#fc618d", # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               "#f7f1ff", # class: 'p'

        Name:                      "#f7f1ff", # class: 'n'
        Name.Attribute:            "#7bd88f", # class: 'na' - to be revised
        Name.Builtin:              "",        # class: 'nb'
        Name.Builtin.Pseudo:       "",        # class: 'bp'
        Name.Class:                "#7bd88f", # class: 'nc' - to be revised
        Name.Constant:             "#5ad4e6", # class: 'no' - to be revised
        Name.Decorator:            "#7bd88f", # class: 'nd' - to be revised
        Name.Entity:               "",        # class: 'ni'
        Name.Exception:            "#7bd88f", # class: 'ne'
        Name.Function:             "#7bd88f", # class: 'nf'
        Name.Property:             "",        # class: 'py'
        Name.Label:                "",        # class: 'nl'
        Name.Namespace:            "",        # class: 'nn' - to be revised
        Name.Other:                "#7bd88f", # class: 'nx'
        Name.Tag:                  "#fc618d", # class: 'nt' - like a keyword
        Name.Variable:             "",        # class: 'nv' - to be revised
        Name.Variable.Class:       "",        # class: 'vc' - to be revised
        Name.Variable.Global:      "",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "",        # class: 'vi' - to be revised

        Number:                    "#948ae3", # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   "#948ae3", # class: 'l'
        Literal.Date:              "#fce566", # class: 'ld'

        String:                    "#fce566", # class: 's'
        String.Backtick:           "",        # class: 'sb'
        String.Char:               "",        # class: 'sc'
        String.Doc:                "",        # class: 'sd' - like a comment
        String.Double:             "",        # class: 's2'
        String.Escape:             "#948ae3", # class: 'se'
        String.Heredoc:            "",        # class: 'sh'
        String.Interpol:           "",        # class: 'si'
        String.Other:              "",        # class: 'sx'
        String.Regex:              "",        # class: 'sr'
        String.Single:             "",        # class: 's1'
        String.Symbol:             "",        # class: 'ss'

        Generic:                   "",        # class: 'g'
        Generic.Deleted:           "#fc618d", # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Error:             "",        # class: 'gr'
        Generic.Heading:           "",        # class: 'gh'
        Generic.Inserted:          "#7bd88f", # class: 'gi'
        Generic.Output:            "",        # class: 'go'
        Generic.Prompt:            "",        # class: 'gp'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        "#69676c", # class: 'gu'
        Generic.Traceback:         "",        # class: 'gt'
    }
