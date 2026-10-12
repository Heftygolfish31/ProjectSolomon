class StringTools:
    def replace(string_to_modify, index, string_to_replace):
        return string_to_modify[:index] + string_to_replace + string_to_modify[index+1:]

class Decorations:
    DIVIDER = "#@>~-             -~<@#"