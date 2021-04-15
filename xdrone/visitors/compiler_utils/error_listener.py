from antlr4.error.ErrorListener import ErrorListener


class ParserErrorListener(ErrorListener):
    def __init__(self):
        self.syntax_errors = []

    def get_error_string(self):
        error_string = ""
        for line, column, msg in self.syntax_errors:
            error_string += str(line) + ":" + str(column) + ": syntax error, " + str(msg) + "\n"
        return error_string

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.syntax_errors.append((line, column, msg))
