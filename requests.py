import requests
from bs4 import BeautifulSoup

# Read inputs from a file
with open("S:\python\lasan.txt", 'r') as file:
    input_data = file.readlines()

# URL of the website where you want to submit the form
url = 'file:///S:/webdevlopment/2056sujalsinhgohel/login.html'  # Replace with the actual website URL

# Loop through each input from the file
for line in input_data:
    # Assuming each line in the file contains one input separated by a delimiter like comma
    # Modify this part based on your file structure
    inputs = line.strip().split(',')  # Modify the delimiter if necessary

    # Prepare the data to be sent to the website form
    form_data = {
        'username': inputs[0],  # Replace 'input_field_1' with the actual field name
        'a': inputs[1],  # Replace 'input_field_2' with the actual field name
        # Add more fields as needed
    }

    # Make a POST request to submit the form data
    response = requests.post(url, data=form_data)

    # Parse the response HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and print the desired output from the website
    # Replace 'output_element' with the actual element/class/id of the output you want to capture
    output = soup.find('div', class_='output_element')  # Modify this based on the actual HTML structure

    if output:
        # Print the output content
        print(output.text)

        # Write the output to a file
        with open('output.txt', 'a') as output_file:
            output_file.write(output.text + '\n')
    else:
        print("Output not found on the page.")
