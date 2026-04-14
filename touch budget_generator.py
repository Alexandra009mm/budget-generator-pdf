from fpdf import FPDF
from datetime import datetime
import os


print("\n" + "="*50)
print("       ✨ PROJECT BUDGET GENERATOR ✨")
print(f"       Date: {datetime.now().strftime('%b %d, %Y')}")
print("="*50)
print("Please enter the project details below:\n")

a = "yes"
while a == "yes":

    name_proyect = input("Enter the proyect name: ")
    hours = int(input("Enter the estimated hours to complete the project: "))
    cost_per_hour = float(input("Enter the value for the hours of work (usd): "))
    delivery_time = input("Enter estimated delivery time: ")

    total_cost = hours * cost_per_hour

    clear_name = name_proyect.replace(" ","_")
    date_time =  datetime.now().strftime("%d-%m-%Y_%H-%M")
    pdf_file = f"Budget_{clear_name}_{date_time}.pdf"



    # Crear la carpeta 'budgets' si no existe
    if not os.path.exists("budgets"):
        os.makedirs("budgets")

    # Cambiar la ruta del archivo para que se guarde adentro
    pdf_file_path = f"budgets/{pdf_file}"


    pdf = FPDF()

    pdf.add_page()


    try:
        pdf.image("Template.png", 0, 0) 
    except:
        print("Warning: 'Template.png' was not found. The PDF will be generated blank.")

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(50, 50, 50)

    pdf.text(115,145, f"{name_proyect}")
    pdf.text(115,160, f"{hours}")
    pdf.text(115,175, f"${cost_per_hour}")
    pdf.text(115,190, f"{delivery_time}")
    pdf.text(115,205, f"${total_cost:.2f}")


    pdf.output(pdf_file_path)

    print(f"\nBudget generated successfully!")
    print(f"File saved as: {pdf_file_path}")

    keep_on = True
    while keep_on == True:
        a = input("do you add another budget? yes/no: ").strip().lower()

        if a == "no":
            keep_on = False
            a = "no"

        elif a  not in ("yes","no"):
            print("Invalid input. Please type 'yes' or 'no'.")
            
        else:
            keep_on = False