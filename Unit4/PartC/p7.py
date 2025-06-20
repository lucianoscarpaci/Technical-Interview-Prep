def identify_repeated_themes(scenes):
    theme_count = {}

    # Count the occurrences of each theme
    for scene in scenes:
        theme = scene["theme"]
        if theme in theme_count:
            theme_count[theme] += 1
        else:
            theme_count[theme] = 1

    # Extract themes that appear more than once
    repeated_themes = [theme for theme, count in theme_count.items() if count > 1]

    return repeated_themes
