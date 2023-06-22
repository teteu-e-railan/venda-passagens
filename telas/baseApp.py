from typing import Type
import customtkinter as ctk


class MyApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My Single Page Application")
        self.geometry("564x300")

        # Dictionary to store the pages
        self.pages: dict[Type[ctk.CTkFrame], ctk.CTkFrame] = {}

        self.show_page(HomePage)  # Show the initial page

    def show_page(self, page_class: Type[ctk.CTkFrame]):
        # Hide the current page (if any)
        if hasattr(self, "current_page"):
            self.current_page.pack_forget()

        try:
            # Get stored page in dictionary
            page = self.pages[page_class]
        except KeyError:
            # Create a new instance of the requested page class
            page = page_class(self)
            # Store the page in the dictionary for future reference
            self.pages[page_class] = page

        # Pack the page and make it visible
        page.pack(side="top", fill="both", expand=True)
        self.current_page = page


class HomePage(ctk.CTkFrame):
    def __init__(self, master: MyApp):
        super().__init__(master)

        # Create widgets for the home page
        label = ctk.CTkLabel(self, text="Welcome to the Home Page!", font=("Arial", 24))
        label.pack(pady=50)

        button = ctk.CTkButton(
            self,
            text="Go to About Page",
            command=lambda: self.master.show_page(AboutPage),
        )
        button.pack()


class AboutPage(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create widgets for the about page
        label = ctk.CTkLabel(self, text="This is the About Page", font=("Arial", 24))
        label.pack(pady=50)

        button = ctk.CTkButton(
            self,
            text="Go to Home Page",
            command=lambda: self.master.show_page(HomePage),
        )
        button.pack()


app = MyApp()
app.mainloop()
