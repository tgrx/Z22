def make_headers(dictionary):

    if "Date" in dictionary:
        date_string = dictionary["Date"]
        dictionary["Date"] = date_string.strftime("%a, %e %b %Y %H:%M:%S GMT")
    result_1 = "\n".join(f"{key}: {value}" for key, value in sorted(dictionary.items()))

    return result_1
