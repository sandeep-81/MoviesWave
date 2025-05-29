try:
    from PIL import Image, ImageTk
    print("PIL imports are working.")
except ImportError as e:
    print(f"Error importing PIL: {e}")
