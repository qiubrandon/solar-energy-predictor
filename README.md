# Solar Energy Predictor

Welcome to the **Solar Energy Predictor** project! Its not very flashy nor does it work super well, but it can be helpful for solar farmers, if they want to predict solar irradiance (GHI). 🚀

---

## **Setup Instructions**

### **1. Download Solar Data**
To train the model, you'll need to obtain a solar dataset from the **NREL Solar Data repository**. Save this file in your project directory.

### **2. Create a `config.py` File**
In the root directory, create a `config.py` file to store the following configuration variables:

```
PATH = ""         # Path to your solar data CSV file
KEY = ""          # API key for WeatherAPI
URL = ""          # URL endpoint for WeatherAPI
MODEL_PATH = ""   # Path to save or load the trained model
```
### **3. Install Dependencies**
Ensure you have Python installed. Then, install the required dependencies:

```
pip install -r requirements.txt
```
### **4. Run Tests**
Before diving in, test the setup to ensure the code is functioning as expected:
```bash
pytest
```
Note: Test should pass, that means that the model is trained. Please check your weather api/data/dataset otherwise.

### **5. Start the Server**
To start the FastAPI server and access the prediction API:

```bash
uvicorn app:app --reload
Visit http://127.0.0.1:8000/ in your browser to use the web interface.
```

### **6. Use the Trained Model**
If you already have a trained model, you can use it to make predictions. Place your model in the path specified in MODEL_PATH, and the server will load it for inference.

### **Known Issues**
Some features may not work as expected.
Testing is incomplete, and certain edge cases might not be handled.
The model’s performance depends on the quality of the dataset and preprocessing.
If you encounter problems, feel free to explore and tweak the code—it’s a great opportunity to contribute!

### Contributing
This project is open for collaboration. If you have suggestions or fixes, feel free to fork the repo and submit a pull request.

### Contact
Questions or feedback? Reach out to the project owner. Let’s build something amazing together! 🌞







