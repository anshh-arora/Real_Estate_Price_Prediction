# Real Estate Price Prediction: Bangalore House Dataset

## Overview
This project aims to predict house prices in Bangalore using the Bangalore House Dataset. The dataset includes information about various features of houses such as size, number of bedrooms (BHK), and number of bathrooms. The goal is to build a machine learning model that can accurately predict the price of a house based on these features.

## Dataset
The dataset used for this project includes the following columns:
- **Size**: The size of the house in square feet.
- **BHK**: Number of bedrooms (BHK - Bedroom, Hall, Kitchen).
- **Bathroom**: Number of bathrooms.
  
### Target Variable
- **Price**: The price of the house in Indian Rupees (INR).

## Project Structure
This repository contains the following directories:
- **[real_estate_price_prediction](./real_estate_price_prediction)**: Complete project code and files.
- **[models](./models)**: Contains saved machine learning models.
- **[client](./client)**: HTML, CSS, and JavaScript files for the client-side web interface.
- **[server](./server)**: Python files for the Flask server.
  
## Project Files
- **[server.py](./server/server.py)**: Main Flask server file that handles requests and serves predictions.
- **[util.py](./server/util.py)**: Utility functions used in the server.
- **[client/index.html](./client/index.html)**: HTML file for the client-side web interface.
- **[client/style.css](./client/style.css)**: CSS file for styling the web interface.
- **[client/script.js](./client/script.js)**: JavaScript file for client-side functionality.

## Usage
1. **Setting Up the Environment**:
   - Ensure you have Python installed on your machine.
   - Install the required Python packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Flask Server**:
   - Navigate to the `server` directory:
     ```bash
     cd server
     ```
   - Run the Flask server:
     ```bash
     python server.py
     ```
   - The server will start running locally at `http://localhost:8080`.

3. **Accessing the Web Interface**:
   - Open your web browser and go to `http://localhost:8080`.
   - You can now interact with the web interface to predict house prices.

## Models
This project includes pre-trained machine learning models for predicting house prices. These models are stored in the `models` directory.

## Contact Information
For any inquiries or feedback regarding this project, please feel free to contact:
- Email: ansharora.cs@gmail.com
- LinkedIn: [Connect with me on LinkedIn](https://www.linkedin.com/in/ansh-arora-data-scientist)
- Kaggle: [Follow me on Kaggle](https://www.kaggle.com/ansh1529)

---

**Disclaimer**: This project is for educational purposes and should not be used for real-world applications without proper validation and testing. The developers are not liable for any misuse or misinterpretation of the results.

---

Feel free to customize this README file further to include additional information or details specific to your project.
