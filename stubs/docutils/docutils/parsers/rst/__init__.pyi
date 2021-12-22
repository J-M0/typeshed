from typing import Any, ClassVar, Tuple
from typing_extensions import Literal

from docutils import parsers
from docutils.parsers.rst import states

class Parser(parsers.Parser):
    supported: ClassVar[Tuple[str, ...]]
    config_section: ClassVar[str]
    config_section_dependencies: ClassVar[Tuple[str, ...]]
    initial_state: Literal["Body", "RFC2822Body"]
    state_classes: Any
    inliner: Any
    def __init__(self, rfc2822: bool = ..., inliner: Any | None = ...) -> None: ...
    def get_transforms(self) -> list: ...
    def parse(self, inputstring: str, document) -> None: ...
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class DirectiveError(Exception):
    level: Any
    msg: str
    def __init__(self, level: int, message: str) -> None: ...

class Directive:
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: ClassVar[dict[str, Any] | None]
    has_content: ClassVar[bool]
    name: str
    arguments: list[Any]
    options: dict[str, Any]
    content: list[str]
    lineno: int
    content_offset: int
    block_text: str
    state: states.RSTState
    state_machine: states.RSTStateMachine
    def __init__(
        self,
        name: str,
        arguments: list[Any],
        options: dict[str, Any],
        content: list[str],
        lineno: int,
        content_offset: int,
        block_text: str,
        state: states.RSTState,
        state_machine: states.RSTStateMachine,
    ) -> None: ...
    def run(self): ...
    def directive_error(self, level: int, message: str) -> DirectiveError: ...
    def debug(self, message: str) -> DirectiveError: ...
    def info(self, message: str) -> DirectiveError: ...
    def warning(self, message: str) -> DirectiveError: ...
    def error(self, message: str) -> DirectiveError: ...
    def severe(self, message: str) -> DirectiveError: ...
    def assert_has_content(self) -> None: ...
    def __getattr__(self, name: str) -> Any: ...  # incomplete

def convert_directive_function(directive_fn): ...
