def my_function(real_name, optional_display_name=None) -> None:

    optional_display_name = optional_display_name or real_name
    print(optional_display_name)


my_function("John")

my_function("Mike", "anonymous123")
