To install Flask, which is necessary for running GuardFrame, you can add an additional step to the instructions after setting up the virtual environment. Here’s how you can modify the guide:

### Step-by-Step Guide

1. **Clone the Repository:**
   Start by cloning the GuardFrame repository from GitHub to your local machine. Open your terminal (command prompt) and run the following command:
   ```
   git clone https://github.com/induwara2020/GuardFrame.git
   ```

2. **Navigate to the Project Directory:**
   Change into the project directory that you just cloned:
   ```
   cd guardframe
   ```

3. **Set Up a Virtual Environment (Optional but Recommended):**
   It's a good practice to create and activate a virtual environment to manage dependencies. This step ensures that the project's dependencies are isolated from your global Python environment.
   - On macOS/Linux:
     ```
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install Dependencies:**
   Install the required Python packages specified in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

5. **Install Flask:**
   Flask is required to run the GuardFrame application. Install it using pip:
   ```
   pip install Flask
   ```

6. **Run the Flask Application:**
   Start the Flask application by running the following command:
   ```
   python app.py
   ```
   This command starts the server, and you should see output indicating that the server is running.

7. **Open the Application in Your Browser:**
   Once the server is running, open your web browser and go to the following URL:
   ```
   http://127.0.0.1:5000/
   ```
   This will open the GuardFrame application interface in your browser.

### Using GuardFrame

Once you have the application open in your browser, follow these steps to encrypt or decrypt text using the Caesar cipher:

- **Enter Text:** Type or paste the text you want to encrypt or decrypt into the "Enter Text" field on the GuardFrame web interface.
  
- **Choose Operation:** Select whether you want to "Encrypt" or "Decrypt" the text from the dropdown menu provided.
  
- **Enter Key:** Specify a key between 1 and 25. This key determines the shift applied during the encryption or decryption process.
  
- **Submit:** Click the "Submit" button to process your text with the selected operation and key. The result will be displayed in the "Result" textarea below.

### Additional Information

- **Caesar Cipher Details:** For more details on how the Caesar cipher works, you can refer to the Caesar cipher Wikipedia page or any other reliable source on cryptography.

By following these steps, you should be able to successfully install Flask and run GuardFrame on your local machine.
