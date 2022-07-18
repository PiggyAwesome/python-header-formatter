
def convert(headers :str):
    no_emptylines = headers.replace("\n\n", "")
    is_double_quote = no_emptylines.find("\"")
    if is_double_quote == -1:
        quote = "\""
    else:
        quote = "'"
    quoted_headers = quote + no_emptylines.replace("\n", f"{quote},\n{quote}")
    if quoted_headers[-1] != "\n":
        good_last_line_headers = quoted_headers + f"{quote}"
    else:
        good_last_line_headers = quoted_headers[:-2]
    return good_last_line_headers