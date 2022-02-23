class Utils:
    def format_info_lines(self, info_lines):
        result = ""

        for line in info_lines:
            if result != "":
                result += "\n"
            
            result += line

        return result

    def get_width_in_screen(self, text):
        length = 0
        for line in text.splitlines():
            line_length = len(line)
            if length < line_length:
                length = line_length
        return length
    
    def normalize(self, text):
        length = self.get_width_in_screen(text)
        output = ""

        for line in text.splitlines():
            while len(line) < length:
                line += " "

            if output != "":
                output += "\n"
            output += line
        return output

    def add_info_to_ascii(self, ascii, info_text):
        result = ""
        info_lines = info_text.splitlines()
        info_length = len(info_lines)

        ascii_lines = ascii.splitlines()
        ascii_length = len(ascii_lines)

        i_ascii = 0
        i_info = 0
        padding = self.get_width_in_screen(ascii)

        limit = max(ascii_length, info_length)

        for _ in range(limit):
            if result != "":
                result += "\n"

            has_ascci_in_line = False

            if i_ascii < ascii_length:
                result += ascii_lines[i_ascii]
                i_ascii += 1
                has_ascci_in_line = True
            if i_info < info_length:
                if has_ascci_in_line is False:
                    result += " " * padding
                result += info_lines[i_info]
                i_info += 1
        return result


    def add_padding_to_text(self, text, x, y):
        result = ""
        lines = text.splitlines()

        for l in lines:
            if result != "":
                result += "\n"
            else:
                for _ in range(y):
                    result += "\n"

            lr_padding = " " * x
            result += lr_padding + l + lr_padding
        return result
