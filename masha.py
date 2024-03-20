import turtle
from simple_term_menu import TerminalMenu


N = 5

def validate_number(n: int) -> bool:
    """Number validation

    Args:
        n (int): number to be validated

    Returns:
        bool: result of comparison of given number and 3.
              True if the number is grater or equal to 3
    """
    return n >= 3


def draw_polygon(n: int=3) -> None:
    """Draw polygon with n edges

    Args:
        n (int, optional): number of edges. Defaults to 3.
    """
    if not validate_number(n):
        print("Error: polygon with 2 or less edges could not be visualized")
        turtle.bye()
        return

    for _ in range(n):
        turtle.forward(100)
        turtle.right(360/n)


def draw_snowflake(n: int=3) -> None:
    """Draw snowflake previously turned cursor into the turtle shape
    """
    if not validate_number(n):
        print("Error: snowflake with 2 or less endings could not be visualized")
        turtle.bye()
        return

    turtle.shape("turtle")
    for _ in range(n):
        turtle.forward(100)
        turtle.goto(0,0)
        turtle.right(360/n)


if __name__ == "__main__":
    print("---CHOOSE SCRIPT---")
    print("---OPTIONS---")
    options = ("polygon", "snowflake")
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if options[menu_entry_index] == "polygon":
        number = int(input("Введіть кількість сторін многокутника: ")) or N
        draw_polygon(n=number)
    elif options[menu_entry_index] == "snowflake":
        number = int(input("Введіть кількість кінцівок сніжинки: ")) or N
        draw_snowflake(n=number)
    
    turtle.exitonclick()