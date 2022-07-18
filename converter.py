
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

    separate_headers = good_last_line_headers.split("\n")
    good_item_headers = ""
    for header in separate_headers:
        separate_split_headers = header.split(":")
        good_item_headers = good_item_headers + separate_split_headers[0] + (quote + ": " + quote + "".join(separate_split_headers[1:])).replace(f"{quote}: {quote} ", f"{quote}: {quote}") + "\n"

    good_item_headers = good_item_headers[:-1]

    return good_item_headers