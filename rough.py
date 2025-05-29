import tkinter as tk
from PIL import Image, ImageTk


# Create the Tkinter window
root = tk.Tk()

# Open an image using PIL (ensure you replace 'image.png' with your actual image path)
image = Image.open("image.png")

# Convert the image to a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()
