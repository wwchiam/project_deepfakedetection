import streamlit as st
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.models import load_model
import altair as alt
import plotly.express as px

# Page Title and Config
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Global CSS Styling with Background Image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://raw.githubusercontent.com/wwchiam/project_deepfakedetection/main/background_v2.jpg');
        background-size: cover;
        background-position: center;
        font-family: Arial, sans-serif;
        color: #ffffff;
    }
    
    /* Container for Tab Content */
    .tab-content {
        background-color: rgba(0, 0, 0, 0.6);  /* Semi-transparent black background */
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }

    /* Title Section */
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .sub-title {
        font-size: 24px;
        font-weight: 400;
        color: #ffffff;
        text-align: center;
        margin-bottom: 40px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }

    /* Section Headers */
    .section-header {
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }

    /* Adjusted Tab Styling */
    .stTabs div[role="tablist"] {
        justify-content: center !important;
        gap: 20px !important;
    }
    .stTabs [role="tab"] {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        padding: 10px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background-color: #4a90e2;
        color: #ffffff;
    }

    /* File Uploader Styling */
    .stFileUploader label {
        font-size: 18px;
        color: #ffffff;
        font-weight: bold;
    }

    /* Result Styling */
    .result {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }
    </style>
    """, unsafe_allow_html=True
)

# Title Section
st.markdown('<div class="title">Deepfake Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Empowering trust in digital media</div>', unsafe_allow_html=True)

# Load ResNet50 Model
model = ResNet50(weights="imagenet")

# Preprocess Image for Prediction
def preprocess_image(image_file, target_size=(224, 224)):
    """Preprocess the image for model prediction."""
    try:
        image = load_img(image_file, target_size=target_size)
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        return preprocess_input(image_array)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Report Fake Image
def report_fake_image():
    """Simulate reporting a deepfake image."""
    st.success("Thank you for reporting. Your input will help improve our system.")

# Main Functionality
def main():
    # Tab Layout
    tabs = st.tabs(["About", "Usage", "Detection", "Technology", "Contact Us"])
    
    with tabs[0]:  # About Tab
        st.markdown(
            """
            <div class="tab-content">
                <div class="section-header">About the Platform</div>
                <p>Welcome to our <b>Deepfake Detection System</b>, your trusted tool for identifying manipulated media.</p>
                <p>In an age where manipulated media is becoming alarmingly common, our Deepfake Detection platform empowers users to verify the authenticity of images with just a simple upload. 
                This tool is designed to safeguard public trust, prevent misinformation, and protect against the malicious use of deepfake technology on social media.</p>
                
            <div class="section-header">Why It Matters?</div>
                <ul>
                <li>Over 8 million deepfake attempts are shared weekly on social media.</li>
                <li>Deepfakes fuel misinformation, invade privacy, and undermine trust.</li>
                </ul>
    
            <div class="section-header">How can we help</div>
                <li><b>Detect & Verify</b>: Quickly identify manipulated media using cutting-edge deep learning techniques.</li>
                <li><b>Report Deepfakes</b>: Contribute to combating misinformation by reporting suspicious content directly through the platform.</li>
                <li><b>Stay Informed</b>: Access resources and guides to understand and navigate the challenges of deepfake technology.</li>
            </div>
            
            """, 
            unsafe_allow_html=True
        )

    # Usage Tab
    with tabs[1]: 
        st.markdown(
            """
            <div class="tab-content">
                <div class="section-header">Usage Statistic</div>
                <p>Thinking...</p>
            </div>
            
            """, 
            unsafe_allow_html=True
        )
         

    # Detection Tab
   # Detection Tab
    with tabs[2]:
        # Overall container with a slightly transparent background, rounded corners, and padding
        st.markdown(
            """
            <div class="tab-content" style="background-color: rgba(0, 0, 0, 0.5); padding: 30px; border-radius: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);">
                <div class="section-header" style="color: white; font-size: 24px; font-weight: bold; margin-bottom: 20px;">Upload an Image for Detection</div>
                <p style="color: white; font-size: 16px; margin-bottom: 20px;">Upload an image to check if it is a deepfake. Adjust the sensitivity threshold for more control over the detection results.</p>
            """, 
            unsafe_allow_html=True
        )
        
        # Create two columns for left (image upload) and right (result)
        col1, col2 = st.columns([1, 2])  # Left column for image upload, right for result
        
        with col1:  # Left column for image upload
            # File Uploader (Streamlit Widget)
            uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
            
        with col2:  # Right column for results (initially empty)
            # Sensitivity Slider (Streamlit Widget)
            st.markdown(
                """
                <div style="margin-bottom: 20px;">
                    <p style="color: white; font-size: 16px;">Adjust the sensitivity:</p>
                </div>
                """, unsafe_allow_html=True
            )
            sensitivity = st.slider(
                "Select Detection Sensitivity", 
                min_value=0.1, 
                max_value=0.9, 
                value=0.5665,  # Default threshold
                step=0.05, 
                help="Adjust the sensitivity of the deepfake detection model. Lower sensitivity may result in fewer false positives."
            )
            
            # Style the 'Detect Deepfake' button with a sleek red color
            st.markdown(
                """
                <style>
                    .stButton>button {
                        background-color: #e74c3c; /* McKinsey-style red */
                        color: white;
                        font-size: 18px;
                        border-radius: 20px;
                        border: none;
                        padding: 12px 25px;
                        cursor: pointer;
                        font-weight: bold;
                    }
                    .stButton>button:hover {
                        background-color: #c0392b;
                    }
                </style>
                """, unsafe_allow_html=True
            )
            
            # Detect Button 
            detect_button = st.button("Detect Deepfake", key="detect_button")
            
        # Displaying the results (inside a well-designed container)
        with st.container():
            if uploaded_file and detect_button:
                # Processing the uploaded file
                image_array = preprocess_image(uploaded_file)
                if image_array is not None:
                    with st.spinner("Analyzing the image..."):
                        try:
                            # Use the loaded model to make predictions
                            prediction = model.predict(image_array)
                            # Extract the top predicted class and the corresponding probability
                            predicted_class = np.argmax(prediction[0])
                            predicted_prob = prediction[0][predicted_class]
        
                            # Display the uploaded image in a visually appealing manner
                            with col1:
                                st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
                            # Display results (probability and classification) in a sleek card on the right
                            with col2:
                                st.markdown(
                                    f"<div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);'><h3 style='color: white;'>Probability of Fake Image: {predicted_prob * 100:.2f}%</h3></div>",
                                    unsafe_allow_html=True
                                )
        
                                # Determine if the image is fake based on the threshold
                                result = 'Fake' if predicted_prob > sensitivity else 'Real'
                                st.markdown(
                                    f"<h2 style='color: white;'>This image is classified as <span style='color: #e74c3c;'>{result}</span>.</h2>",
                                    unsafe_allow_html=True
                                )
        
                        except Exception as e:
                            st.error(f"Error during prediction: {e}")
                else:
                    st.warning("Please upload a valid image.")
            else:
                st.warning("Please upload an image and click 'Detect Deepfake'.")
            
        # Closing the divs properly
        st.markdown("</div></div></div>", unsafe_allow_html=True)



    # Technology Tab
    with tabs[3]: 
        st.markdown(
            """
            <div class="tab-content">
                <div class="section-header">Powered by ResNet50</div>
                <p>Our deepfake detection system is powered by <b>ResNet50</b>, a cutting-edge deep learning model known for its remarkable accuracy in image classification tasks.
                By fine-tuning this model, we have adapted it to detect deepfake images with high reliability. 
                ResNet50 achieves an impressive balance between performance and efficiency, making it a top choice for tasks that require quick and accurate predictions.</p>
                
            <div class="section-header">Model Performance</div>
                <p>These metrics represent the model's ability to accurately identify real vs. fake images, while minimizing false positives and false negatives.</p>
                <ul>
                    <li>Accuracy: 79% </li>
                    <li>Recall: 92% </li>
                    <li>Precision: 73% </li>
                    <li>F1-Score: 81% </li>
                </ul>
        
            <div class="section-header">Model Evaluation</div>
            <div style="text-align: left;">
                <ul>
                <li><b>Confusion Matrix</b>: Shows the model's predictions against actual labels, illustrating its accuracy.</li>
                </ul>
                <img src="https://raw.githubusercontent.com/wwchiam/project_deepfakedetection/main/improved_resnet50_confusion_matrix.png" alt="Confusion Matrix" width="400" />
                <br>
            </div>
                
            <div style="text-align: left;">
                <ul>
                <br>
                <li><b>Learning Curve</b>: Tracks the model's training progress over time, ensuring it converges toward optimal performance.</li>
                </ul>
                <img src="https://raw.githubusercontent.com/wwchiam/project_deepfakedetection/main/improved_resnet50_loss_plot.png" alt="Loss Plot" width="400" />
            </div>
            </div>
            """, 
            unsafe_allow_html=True
        )


    # Contact Us Tab
    with tabs[4]: 
        st.markdown(
            """
            <div class="tab-content">
                <div class="section-header">Contact Us</div>
                <p>For inquiries or support, please contact us at:</p>
                <p>📧 23054196@siswa.um.edu.com"</p>
            </div>
            
            """, 
            unsafe_allow_html=True
        )



# Run the main function
if __name__ == "__main__":
    main()
