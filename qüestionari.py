import flet as ft 

def main(page:ft.Page):
    def button_clicked(e):
        page.clean()
        name=input_name.value
        age=int(input_date_of_birth.value)
        text_nom=ft.Text(value=f"nom: {name}",size=50,color="yellow")
        if age >= (18):
            text_edat=ft.Text(value=f"you're {age}, you're allowed to pass to the website",size=50,color="green")
        else: 
            text_edat=ft.Text(value=f"you're {age}, you're not allowed to pass to the website",size=50,color="red")

        
        page.add(
            ft.Row(
                controls=[text_nom],
                alignment="center"
            ),
            ft.Row(
                controls=[text_edat],
                alignment="center"
            )
        )
    titulo=ft.Text(value="Qüestionari",size=40,color="blue")
    input_name=ft.TextField(label="Name")
    input_last_name=ft.TextField(label="Last name")
    input_date_of_birth=ft.TextField(label="Age")
    input_street=ft.TextField(label="Street")
    input_house_number=ft.TextField(label="House number")
    input_mail=ft.TextField(label="Mail")
    input_phone=ft.TextField(label="Phone")
    send_button=ft.ElevatedButton(text="Submit",on_click=button_clicked,color="yellow",bgcolor="blue")
    page.add(
        ft.Row(
            controls=[titulo],
            alignment="center"
        ),
        ft.Row(
            controls=[input_name,input_last_name,input_date_of_birth],
            alignment="center"
        ),
        ft.Row(
            controls=[input_street,input_house_number],   
            alignment="center"
        ),
        ft.Row(
            controls=[send_button],
            alignment="center"
        )    
    )
ft.app(target=main)

