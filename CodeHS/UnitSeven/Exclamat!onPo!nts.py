def exclamations(text):
    for i, char in enumerate(text):
        if char == "i":
            tempText = text[0:i]
            secondTempText = text[i + 1:]
            text = tempText + "!" + secondTempText

    return text