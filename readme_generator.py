#!/usr/bin/env python
from setup import name, version
from inspect import getfullargspec, signature
import os, json

IGNORED_METHODS = []

slogan = "Simple, compressed Lorem Ipsum generator. Get a different output each time."

about_text = """This module provides a single function `lorem` \
that produces Lorem Ipsum. py_simple_lorem.py contains a large \
amount of Lorem Ipsum stored in a compressed format."""

installation_message = """Available on pip - `pip install py_simple_lorem`"""

command_line_desc = """Command line usage is simple. \
Run py_simple_lorem.py without arguments for one paragraph\
 or pass an integer for the appropriate number of paragraphs."""

module_desc = """Module usage is simple. Import lorem \
from py_simple_lorem.py and call `lorem(COUNT)` to get \
a string containing *COUNT* number of paragraphs."""

images = {
    "lorem": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_lorem/main/lorem.png?token=GHSAT0AAAAAAB2FJULABRGTLEV6KYXQVZVMY2QVMAA",
}


class MD_Generator:
    def __init__(
        self,
        title=None,
        footnote_title="Notes:",
        footnote_heading_level=2,
        numbered_toc=False,
    ):
        self.title = title
        self.slogan = None
        self.images = []
        self.footnote_title = footnote_title
        self.footnote_heading_level = footnote_heading_level
        self._footnotes = []
        self._footnote_index = 1
        self.body = ""
        self.quote_depth = 0

        self.toc_uid_format = "mark{}"
        self.toc_uid = 0
        self.toc_contents = ""
        self.toc_depth = 0
        self.toc_indicies = {}

        self.numbered_toc = numbered_toc

        self.home_mark_name = self.toc_uid_format.format(self._get_toc_uid())
        self.home_mark = f'<a name="{self.home_mark_name}"></a>'
        self.toc_marks = {0: self.home_mark_name, 1: self.home_mark_name}
        self.last_mark = self.home_mark_name

    def add_image(self, image):
        self.images.append(image)

    def set_slogan(self, slogan):
        self.slogan = slogan

    def _get_toc_uid(self):
        self.toc_uid += 1
        return self.toc_uid - 1

    def increase_toc_depth(self):
        self.toc_depth += 1
        self.toc_indicies[self.toc_depth] = 0
        self.toc_marks[self.toc_depth] = self.last_mark

    def decrease_toc_depth(self):
        if self.toc_depth == 0:
            raise ValueError("toc depth already at 0.")
        self.toc_depth -= 1

    def add_toc(self, title, end="\n"):
        mark_name = self.toc_uid_format.format(self._get_toc_uid())
        self.last_mark = mark_name
        self.body += (
            f'<a name="{mark_name}"></a>[^](#{self.toc_marks[self.toc_depth]}){end}'
        )
        if self.toc_depth in self.toc_indicies:
            index = self.toc_indicies[self.toc_depth]
        else:
            self.toc_indicies[self.toc_depth] = index = 0
        val = index if self.numbered_toc else "-"
        self.toc_contents += "\t" * self.toc_depth + f"{val} [{title}](#{mark_name})\n"
        self.toc_indicies[self.toc_depth] = index + 1

    def assemble(self):
        # Add home marker
        out = ""
        if self.title:
            out = f"# {self.title}"
        out += f"{self.home_mark}\n\n"
        if self.slogan:
            out += f"***{self.slogan}***\n\n"
        if self.images:
            for t, i in self.images:
                out += f"![{t}]({i})\n\n"

        out += "---\n\n"
        if self.toc_contents:
            out += self.toc_contents + "\n"
        out += "---\n\n"
        out += self.body
        if self._footnotes:
            for n in range(self._footnote_index):
                out += f"[^{n+1}]: {self._footnotes[n]}."
        return out

    def insert_footnote(self, text):
        self.body += f"[^{self._footnote_index}]"
        self._footnotes.append(text)
        self._footnote_index += 1

    def save(self, path):
        with open(path, "w+") as f:
            f.write(self.assemble())

    def add_bold(self, text, end="\n\n"):
        self.body += f"**{text}**{end}"

    def add_italic(self, text, end="\n"):
        self.body += f"*{text}*{end}"

    def add_bold_italic(self, text, end="\n"):
        self.body += f"*{text}*{end}"

    def add_break(self):
        self.body += "<br>"

    def _add_heading(self, text, level=1, end="\n", add_toc=True):
        if not level or level < 0 or level > 6:
            raise ValueError(f"Invalid heading level - {level}")
        self.body += self.get_prefix() + "#" * level + f" {text}"
        if add_toc:
            self.add_toc(text)
        self.body += end

    def add_heading_1(self, text, **kwargs):
        self._add_heading(text, 1, **kwargs)

    def add_heading_2(self, text, **kwargs):
        self._add_heading(text, 2, **kwargs)

    def add_heading_3(self, text, **kwargs):
        self._add_heading(text, 3, **kwargs)

    def add_heading_4(self, text, **kwargs):
        self._add_heading(text, 4, **kwargs)

    def add_heading_5(self, text, **kwargs):
        self._add_heading(text, 5, **kwargs)

    def add_heading_6(self, text, **kwargs):
        self._add_heading(text, 6, **kwargs)

    def add_paragraph(self, text, end="\n\n"):
        self.body += f"{self.get_prefix()}{text}{end}"

    def get_prefix(self):
        return "> " * self.quote_depth

    def add_blockquote(self, text, end="\n\n"):
        self.quote_depth += 1
        self.add_paragraph(f"{text}", end)
        self.quote_depth -= 1

    def add_multi_blockquote(self, texts):
        i = 0
        end = len(texts) - 1
        for t in texts:
            self.add_blockquote(t, end="\n")
            if not i == end:
                self.body += ">\n"
            i += 1

    def add_to_unordered_list(self, text, indent=0):
        self.body += "\t" * indent + f"- {text}"

    def add_unordered_list(self, texts, indent=0):
        for t in texts:
            self.add_to_unordered_list(t, indent)

    def add_to_ordered_list(self, index, text, indent=0):
        self.body += "\t" * indent + f"{index}. {text}"

    def add_ordered_list(self, texts, indent=0):
        i = 1
        for t in texts:
            self.add_to_ordered_list(i, t, indent)
            i += 1

    def add_code_block(self, text, lang="", end="\n"):
        p = self.get_prefix()
        self.body += f"{p}```{lang}\n{text}\n{p}```{end}"

    def add_horizontal_rule(self):
        self.body += f"{self.get_prefix()}---\n\n"

    def add_link(self, link, text=None, tooltip=None):
        if not text:
            text = link
        if tooltip:
            self.body += f'[{text}]({link} "{tooltip}")'
        else:
            self.body += f"[{text}]({link})"


def generate_readme(version):
    print("Generating Readme")
    gen = MD_Generator(title=f"{name} {version}", footnote_heading_level=3)

    def handle_class_list(widgets):
        gen.increase_toc_depth()
        for w in widgets:
            gen.add_heading_3(w.__name__, end="", add_toc=False)
            gen.add_toc(w.__name__)
            gen.quote_depth += 1
            if w.__doc__:  # Add docstring
                gen.add_paragraph(f"**{w.__doc__}**", end=f"\n{gen.get_prefix()}\n")
                # gen.add_heading_5(w.__doc__, line="\n")
            if hasattr(w, "__desc__"):  # Only print desc if it isn't inherited
                desc_inherited = False
                for b in w.__bases__:
                    if hasattr(b, "__desc__"):
                        if b.__desc__ == w.__desc__:
                            desc_inherited = True
                            break
                if not desc_inherited:
                    gen.add_paragraph(w.__desc__, end="\n")

            classstring = f"class {w.__name__}("
            if len(w.__bases__) == 1:
                b = w.__bases__[0]
                classstring += b.__name__
            else:
                last = len(w.__bases__) - 1
                i = 0
                for b in w.__bases__:
                    classstring += b.__name__
                    if not i == last:
                        classstring += ", "
                    i += 1
            classstring += "):\n"
            sig = str(signature(w)).strip('"')
            sig = sig[:1] + "self, " + sig[1:]
            classstring = classstring + "\tdef __init__" + sig + ":\n\t\t...\n"
            methods = [
                m
                for m in dir(w)
                if (m.startswith("_") is False)
                and callable(getattr(w, m))
                and (not m in IGNORED_METHODS)
            ]
            if methods:
                for m in methods:
                    meth = getattr(w, m)
                    val = "..."
                    if hasattr(meth, "__doc__"):
                        if meth.__doc__:
                            val = f'"""{meth.__doc__}"""'
                    classstring += f"\tdef {m}{str(signature(meth))}:\n\t\t{val}\n"

            formatted_classstring = ""
            for l in classstring.splitlines():
                formatted_classstring += gen.get_prefix() + l + "\n"
            gen.add_code_block(formatted_classstring.strip(), lang="py")
            gen.quote_depth -= 1
        gen.decrease_toc_depth()

    def handle_function_list(functions):
        gen.increase_toc_depth()
        for f in functions:
            gen.add_heading_3(f.__name__, end="", add_toc=False)
            gen.add_toc(f.__name__)
            gen.quote_depth += 1
            gen.add_paragraph(f"**{f.__doc__}**", end=f"\n{gen.get_prefix()}\n")
            name = f.__name__
            funcstring = f"def {name}{str(signature(f))}:\n{gen.get_prefix()}\t..."
            gen.add_code_block(funcstring, lang="py")
            gen.quote_depth -= 1
        gen.decrease_toc_depth()

    ##########################################################
    gen.set_slogan(slogan)
    for i in images:
        gen.add_image((i, images[i]))

    gen.add_heading_1("About")
    gen.add_paragraph(about_text)
    gen.increase_toc_depth()
    gen.add_heading_2("Installation")
    gen.add_paragraph(installation_message)
    gen.decrease_toc_depth()

    gen.add_heading_1("Command Line Usage")
    gen.add_paragraph(command_line_desc)

    gen.add_heading_1("Module Usage")
    gen.add_paragraph(module_desc)

    print(out := gen.assemble())
    path = os.path.abspath("README.md")
    with open(path, "w+") as f:
        f.write(out)


if __name__ == "__main__":
    generate_readme(version)
