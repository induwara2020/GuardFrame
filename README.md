How to Run GuardFrame
Welcome to GuardFrame, a simple and powerful tool for encrypting and decrypting text using the Caesar cipher. Follow these steps to run the application on your local machine:

Step-by-Step Guide
Clone the Repository: Start by cloning the GuardFrame repository from GitHub to your local machine. Open your terminal and run:

git clone https://github.com/induwara2020/GuardFrame.git
Navigate to the Project Directory: Change into the project directory:

cd guardframe
Set Up a Virtual Environment (Optional but Recommended): Create and activate a virtual environment to manage dependencies:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies: Install the required Python packages using pip:

pip install -r requirements.txt
Run the Flask Application: Start the Flask application by running:

python app.py
This will start the server, and you should see output indicating that the server is running.

Open the Application in Your Browser: Open your web browser and go to:

http://127.0.0.1:5000/
You should see the GuardFrame application interface.

Using GuardFrame
Enter Text: Type or paste the text you want to encrypt or decrypt into the "Enter Text" field.

Choose Operation: Select whether you want to "Encrypt" or "Decrypt" the text from the dropdown menu.

Enter Key: Specify a key between 1 and 25. This key determines the shift applied during the encryption or decryption process.

Submit: Click the "Submit" button to process your text. The result will be displayed in the "Result" textarea.

Additional Information
For more details on how the Caesar cipher works, you can check out the Caesar cipher Wikipedia page.
Thank you for using GuardFrame!
