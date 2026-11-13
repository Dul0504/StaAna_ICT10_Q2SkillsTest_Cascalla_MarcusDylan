# Periodic Table Information Finder
# Skills Test - 2nd Quarter

from pyscript import document

# Dictionary of non-metals
# format -> "Symbol": ("Element Name", "Atomic Number", "Atomic Mass")
non_metals = {
    "H": ("Hydrogen", "1", "1.008"),
    "He": ("Helium", "2", "4.0026"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "Ne": ("Neon", "10", "20.180"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45"),
    "Ar": ("Argon", "18", "39.948"),
    "Se": ("Selenium", "34", "78.971"),
    "Br": ("Bromine", "35", "79.904"),
    "Kr": ("Krypton", "36", "83.798"),
    "I": ("Iodine", "53", "126.904"),
    "Xe": ("Xenon", "54", "131.293"),
    "Rn": ("Radon", "86", "222"),
}


def element_checker(e):
    # this runs when the Check Details button gets clicked

    # grab the result box so we can write stuff in it
    result_box = document.getElementById("result")

    # clear out the old result first
    result_box.innerHTML = ""

    # get what the user typed, remove extra spaces,
    # then title() so "cl" or "CL" still becomes "Cl"
    element1 = document.getElementById("element_name").value.strip().title()

    # look the symbol up in the dictionary
    # if it's not there, we just use the "not found" tuple instead
    result = non_metals.get(element1, ("Element not found", "-", "-"))

    # if the symbol isn't in the dictionary, show the message and stop here
    if result[0] == "Element not found":
        result_box.innerHTML = (
            "<b>Sorry!</b> That element does not exist "
            "in the non-metals list."
        )
        return

    # otherwise show all the details
    result_box.innerHTML = f"""
        <b>Symbol:</b> {element1}<br>
        <b>Element:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}<br>
    """
