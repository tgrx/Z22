def get_headers(http_answer):
    http_answer_list = http_answer.split("\n")
    http_headres = http_answer_list[1 : http_answer_list.index("")]
    return dict(elm.split(": ") for elm in http_headres)
