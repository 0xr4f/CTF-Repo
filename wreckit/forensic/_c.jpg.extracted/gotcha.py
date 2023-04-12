from PIL import Image

# Load the input image
input_image = Image.open('output.jpg')

# Get the size of the image
width, height = input_image.size

# Define the color range to replace
red_range = (200, 0, 0) # (R, G, B) values of the lower bound of red shade
white_color = (255, 255, 255) # (R, G, B) values of the replacement color

# Process the pixels to change red shades to white
for x in range(width):
    for y in range(height):
        # Get the color of the current pixel
        current_color = input_image.getpixel((x, y))

        # Check if the pixel color is within the red range
        if current_color[0] >= red_range[0] and current_color[1] <= red_range[1] and current_color[2] <= red_range[2]:
            # Set the pixel to white
            input_image.putpixel((x, y), white_color)

# Save the output image
input_image.save('got.jpg')
