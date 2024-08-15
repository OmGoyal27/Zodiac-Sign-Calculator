def findZodiacSign(date: int, month: int) -> list:
    if month == 1:
        if date < 20:
            return ["Capricorn", "Responsible, disciplined, patient, and ambitious."]
        else:
            return ["Aquarius", "Innovative, open-minded, humanitarian, and eccentric."]
        

    if month == 2:
        if date < 19:
            return ["Aquarius", "Innovative, open-minded, humanitarian, and eccentric."]
        else:
            return ["Pisces", "Compassionate, artistic, intuitive, and empathetic."]
        

    if month == 3:
        if date < 21:
            return ["Pisces", "Compassionate, artistic, intuitive, and empathetic."]
        else:
            return ["Aries", "Eager, dynamic, quick, and competitive."]
        

    if month == 4:
        if date < 20:
            return ["Aries", "Eager, dynamic, quick, and competitive."]
        else:
            return ["Taurus", "Strong, dependable, sensual, and creative."]
        

    if month == 5:
        if date < 21:
            return ["Taurus", "Strong, dependable, sensual, and creative."]
        else:
            return ["Gemini" ,"Versatile, expressive, curious, and kind."]
        

    if month == 6:
        if date < 21:
            return ["Gemini" ,"Versatile, expressive, curious, and kind."]
        else:
            return ["Cancer", "Intuitive, sentimental, compassionate, and protective."]
        

    if month == 7:
        if date < 23:
            return ["Cancer", "Intuitive, sentimental, compassionate, and protective."]
        else:
            return ["Leo", "Dramatic, outgoing, fiery, and self-assured."]
        

    if month == 8:
        if date < 23:
            return ["Leo", "Dramatic, outgoing, fiery, and self-assured."]
        else:
            return ["Virgo", "Practical, loyal, gentle, and analytical."]
        

    if month == 9:
        if date < 23:
            return ["Virgo", "Practical, loyal, gentle, and analytical."]
        else:
            return ["Libra", "Social, fair-minded, diplomatic, and gracious."]
        

    if month == 10:
        if date < 23:
            return ["Libra", "Social, fair-minded, diplomatic, and gracious."]
        else:
            return ["Scorpio", "Passionate, stubborn, resourceful, and brave."]
        

    if month == 11:
        if date < 22:
            return ["Scorpio", "Passionate, stubborn, resourceful, and brave."]
        else:
            return ["Sagittarius", "Optimistic, adventurous, independent, and philosophical."]
        

    if month == 12:
        if date < 22:
            return ["Sagittarius", "Optimistic, adventurous, independent, and philosophical."]
        else:
            return ["Capricorn", "Responsible, disciplined, patient, and ambitious."]