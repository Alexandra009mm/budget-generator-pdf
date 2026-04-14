from fpdf import FPDF # Import FPDF to create the PDF document
from datetime import datetime # Import datetime to get current date and time for unique filenames
import os # Import os to handle folders and directories (like creating the 'budgets' folder)

# --- WELCOME BANNER ---
# Visual header to make the program look professional in the terminal
print("\n" + "="*50)
print("       ✨ PROJECT BUDGET GENERATOR ✨")
print(f"       Date: {datetime.now().strftime('%b %d, %Y')}")
print("="*50)
print("Please enter the project details below:\n")

# Main loop variable: as long as 'a' is "yes", the program will keep asking for new budgets
a = "yes"
while a == "yes":

    # --- 1. DATA COLLECTION ---
    # Gathering user input for the project details
    name_proyect = input("Enter the proyect name: ")
    hours = int(input("Enter the estimated hours to complete the project: "))
    cost_per_hour = float(input("Enter the value for the hours of work (usd): "))
    delivery_time = input("Enter estimated delivery time: ")

    # Calculating the final price
    total_cost = hours * cost_per_hour

    # --- 2. FILE NAMING & DIRECTORY SETUP ---
    # clear_name: replaces spaces with underscores to avoid errors in filenames
    clear_name = name_proyect.replace(" ","_")
    # date_time: generates a timestamp so files don't overwrite each other (Example: 14-04-2026_14-30)
    date_time =  datetime.now().strftime("%d-%m-%Y_%H-%M")
    pdf_file = f"Budget_{clear_name}_{date_time}.pdf"

    # Directory Check: This block checks if the 'budgets' folder exists. If not, it creates it.
    if not os.path.exists("budgets"):
        os.makedirs("budgets")

    # Path variable: tells the program to save the file INSIDE the 'budgets' folder
    pdf_file_path = f"budgets/{pdf_file}"

    # --- 3. PDF GENERATION ---
    pdf = FPDF()
    pdf.add_page() # Adds the first page to our document

    # Background Image: We use a try/except block just in case the 'Template.png' is missing
    # Important: The image must be added FIRST so the text goes ON TOP of it.
    try:
        pdf.image("Template.png", 0, 0) # (0,0) starts at the top-left corner
    except:
        print("Warning: 'Template.png' was not found. The PDF will be generated blank.")

    # Font Settings: You must set a font before adding text, otherwise FPDF will crash
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(50, 50, 50) # Sets text color to dark grey (RGB format)

    # pdf.text(x, y, "text"): adds content at specific coordinates
    # We use f-strings here to automatically convert numbers (int/float) into printable text
    pdf.text(115, 145, f"{name_proyect}")
    pdf.text(115, 160, f"{hours}")
    pdf.text(115, 175, f"${cost_per_hour}")
    pdf.text(115, 190, f"{delivery_time}")
    pdf.text(115, 205, f"${total_cost:.2f}") # :.2f ensures it always shows 2 decimals

    # Final Output: Saves the PDF using the full path (folder + filename)
    pdf.output(pdf_file_path)

    print(f"\nBudget generated successfully!")
    print(f"File saved as: {pdf_file_path}")

    # --- 4. VALIDATION LOOP ---
    # This nested loop forces the user to type exactly "yes" or "no"
    keep_on = True
    while keep_on == True:
        a = input("Do you want to add another budget? yes/no: ").strip().lower()

        if a == "no":
            keep_on = False # Stops the validation loop
            a = "no"        # Will stop the main loop as well
        elif a not in ("yes","no"):
            # If the user types anything else, we show an error and stay inside the loop
            print("Invalid input. Please type 'yes' or 'no'.")
        else:
            keep_on = False # User typed "yes", so we exit this loop to restart the main one