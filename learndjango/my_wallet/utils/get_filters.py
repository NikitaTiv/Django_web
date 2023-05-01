def get_filters() -> list[tuple]:
    return [
        ('-time_create', 'время добавления (по убыванию)'),
        ('time_create', 'время добавления (по возрастанию)'),
        ('description', 'имя (по возрастанию)'),
        ('-description', ' имя (по убыванию)'),
    ]
