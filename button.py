# Define a class for creating buttons
class Button():
    # Define the initialization function for the Button class
    def __init__(self, image, pos, text_input, font, base_colour, highlight_colour):
        # Assign instance variables
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_colour, self.highlight_colour = base_colour, highlight_colour
        self.text_input = text_input
        # Render the button's text using the specified font and base colour
        self.text = self.font.render(self.text_input, True, self.base_colour)
        # If an image was not provided, use the rendered text as the button's image
        if self.image is None:
            self.image = self.text
        # Create the rectangle for the button
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        # Create the rectangle for the button's text
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # Created a function to update the button's appearance on the screen
    def update(self, screen):
        # If an image was provided, display it onto the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)
        # Display the button's text onto the screen
        screen.blit(self.text, self.text_rect)

    # created a function to check if the button has been clicked
    def checkForInput(self, position):
        # Check if the position of the click is within the boundaries of the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        # Return False if the click is not within the boundaries of the button
        return False

    # Create a function to change the colour of the button when the mouse is hovering over it
    def changeColour(self, position):
        # Check if the mouse is hovering over the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            # Change the colour of the button's text to the hovering colour
            self.text = self.font.render(self.text_input, True, self.highlight_colour)
        else:
            # Change the colour of the button's text back to the base colour
            self.text = self.font.render(self.text_input, True, self.base_colour)
