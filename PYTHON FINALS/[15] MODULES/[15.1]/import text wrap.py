# Example 1
import textwrap

note = (
    "Python modules organize reusable functions and classes into separate"
    " files so large projects stay clean, readable, and easy to maintain."
)
print(textwrap.fill(note, width=45))

# Example 2
import textwrap


def get_help_text():
     return textwrap.dedent("""
            Commands:
              add    Create a new item
              list   Show all items
        """).strip()


print(get_help_text()) 

# Example 3

import textwrap

summary = "Line 1 of summary\nLine 2 of summary"
print(textwrap.indent(summary, prefix="  | "))