"""
Forth — Exercism Python Track

A minimal evaluator for a subset of the Forth stack-based programming language.

Supported built-in words
------------------------
Arithmetic (pop two, push one result):
    +   addition
    -   subtraction
    *   multiplication
    /   integer division

Stack manipulation:
    DUP   duplicate top item
    DROP  remove top item
    SWAP  exchange top two items
    OVER  copy second item to top

User-defined words
------------------
    : word-name definition ;

    Creates a new word.  The definition is a sequence of numbers and/or
    existing words.  Words are case-insensitive.  Redefinition is allowed
    and shadows the previous meaning.

Numbers
-------
    Signed integers (e.g. 42, -7).

Error handling
--------------
    StackUnderflowError  — not enough items on the stack for an operation
    ZeroDivisionError    — division by zero
    ValueError           — undefined word or illegal operation
"""


class StackUnderflowError(Exception):
    """Raised when an operation needs more stack items than are available."""
    pass


def evaluate(input_data):
    """Evaluate a sequence of Forth statements and return the final stack.

    Args:
        input_data (list[str]): Each string is one line of Forth code.

    Returns:
        list[int]: The stack after all statements have been executed.

    Implementation overview
    -----------------------
    1. Maintain a stack (list of ints) and a dictionary of user-defined
       words.  The dictionary maps a lowercase word name to a list of
       "compiled" tokens (ints for literals, strings for built-ins).
    2. Tokenise each line by whitespace.
    3. When a token is a number, push it onto the stack.
    4. When a token is a user-defined word, execute its compiled definition.
    5. When a token is a built-in word, perform the operation directly.
    6. When a token is ':', enter compilation mode until ';' is found.
       The definition is resolved immediately (user words are inlined,
       numbers are converted to ints, everything else is lower-cased).
    """

    # -----------------------------------------------------------------------
    # Runtime state
    # -----------------------------------------------------------------------
    stack = []
    words = {}          # lowercase word name -> list of compiled tokens

    # -----------------------------------------------------------------------
    # Helper: check whether a token is a signed integer literal.
    # -----------------------------------------------------------------------
    def is_number(token):
        """Return True if token is a valid signed integer literal."""
        stripped = token.lstrip('-')
        # A lone '-' is not a number; there must be at least one digit.
        return stripped and stripped.isdigit()

    # -----------------------------------------------------------------------
    # Helper: verify the stack has at least n items before popping.
    # -----------------------------------------------------------------------
    def require(n):
        """Raise StackUnderflowError if fewer than n items are on the stack."""
        if len(stack) < n:
            raise StackUnderflowError("Insufficient number of items in stack")

    # -----------------------------------------------------------------------
    # Helper: execute a single compiled token.
    #
    # A compiled token is either:
    #   • an int  → push onto stack
    #   • a str   → built-in operation (already lower-cased)
    # -----------------------------------------------------------------------
    def execute_token(token):
        """Execute one compiled token, modifying the stack in place."""
        # If the token is an integer literal, push it.
        if isinstance(token, int):
            stack.append(token)
            return

        # If the token is a user-defined word, recursively execute its
        # compiled definition.  Because definitions are resolved at compile
        # time, this will never encounter another user-defined word name
        # (they have already been inlined).
        if token in words:
            for sub_token in words[token]:
                execute_token(sub_token)
            return

        # -------------------------------------------------------------------
        # Built-in arithmetic
        # -------------------------------------------------------------------
        if token == '+':
            require(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif token == '-':
            require(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif token == '*':
            require(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        elif token == '/':
            require(2)
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)

        # -------------------------------------------------------------------
        # Built-in stack manipulation
        # -------------------------------------------------------------------
        elif token == 'dup':
            require(1)
            stack.append(stack[-1])

        elif token == 'drop':
            require(1)
            stack.pop()

        elif token == 'swap':
            require(2)
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif token == 'over':
            require(2)
            stack.append(stack[-2])

        # -------------------------------------------------------------------
        # Anything else is unknown.
        # -------------------------------------------------------------------
        else:
            raise ValueError("undefined operation")

    # -----------------------------------------------------------------------
    # Helper: compile a raw definition token list into executable tokens.
    #
    # At compile time we resolve every token:
    #   • numbers      → int literals
    #   • user words   → inline their *current* compiled definition
    #   • built-ins    → lower-cased strings
    #
    # This gives Forth-like semantics: redefining a word later does NOT
    # affect words that were already compiled with the old meaning.
    # -----------------------------------------------------------------------
    def compile_definition(raw_tokens):
        """Convert a list of raw tokens into compiled tokens."""
        compiled = []
        for t in raw_tokens:
            if is_number(t):
                compiled.append(int(t))
            else:
                t_lower = t.lower()
                if t_lower in words:
                    # Inline the current definition of this user word.
                    compiled.extend(words[t_lower])
                else:
                    # Assume it is (or will be) a built-in word.
                    compiled.append(t_lower)
        return compiled

    # -----------------------------------------------------------------------
    # Main loop: process every line of input.
    # -----------------------------------------------------------------------
    for line in input_data:
        tokens = line.split()
        i = 0
        while i < len(tokens):
            token = tokens[i]

            # ---------------------------------------------------------------
            # Compilation mode:  : word-name definition ... ;
            # ---------------------------------------------------------------
            if token == ':':
                i += 1

                # The word name must exist and must not be a number.
                if i >= len(tokens):
                    raise ValueError("undefined operation")
                word_name = tokens[i].lower()
                if is_number(word_name):
                    raise ValueError("illegal operation")
                i += 1

                # Collect tokens until the terminating ';'.
                definition = []
                while i < len(tokens) and tokens[i] != ';':
                    definition.append(tokens[i])
                    i += 1

                # Missing ';' is an error.
                if i >= len(tokens):
                    raise ValueError("undefined operation")
                i += 1  # skip ';'

                # Compile and store the new word.
                words[word_name] = compile_definition(definition)

            # ---------------------------------------------------------------
            # Normal execution mode.
            # ---------------------------------------------------------------
            else:
                if is_number(token):
                    stack.append(int(token))
                else:
                    # Lower-case before looking up (case-insensitive).
                    execute_token(token.lower())
                i += 1

    return stack