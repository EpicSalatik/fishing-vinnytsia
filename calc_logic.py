def calculate_score(temp, press, wind, fish_name):
    """
    Розраховує шанс клювання від 1 до 10 залежно від погоди та виду риби.
    """
    score = 5  # Базовий бал
    
    # 1. Логіка за температурою
    if temp < 5 or temp > 30:
        score -= 3
    elif 15 <= temp <= 22:
        score += 2
        
    # 2. Логіка за тиском (ідеально 745-755 мм)
    if 745 <= press <= 755:
        score += 2
    elif press < 735 or press > 765:
        score -= 2
        
    # 3. Логіка за вітром (сильний вітер - це погано)
    if wind > 8:
        score -= 3
    elif wind < 3:
        score += 1

    # 4. СПЕЦИФІКАЦІЯ ПО ВИДАХ РИБ (Південний Буг)
    fish_name = fish_name.lower()
    
    if "щука" in fish_name:
        if temp < 15: score += 1  # Щука любить прохолоду
    elif "окунь" in fish_name:
        if 18 <= temp <= 24: score += 1
    elif "короп" in fish_name or "карась" in fish_name:
        if temp > 20: score += 1  # Теплолюбні
    elif "судак" in fish_name:
        if press > 750: score += 1 # Судак любить стабільний високий тиск
    elif "рідкісна" in fish_name:
        # Для Вирезуба та Марени умови складніші
        score -= 1 
    
    # Обмежуємо результат від 1 до 10
    if score > 10: score = 10
    if score < 1: score = 1
    
    return score