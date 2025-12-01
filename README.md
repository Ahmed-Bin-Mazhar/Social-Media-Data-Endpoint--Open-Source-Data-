# Social Media Disaster Data Repository

This repository contains **open-source datasets** collected from publicly available sources that capture social media activity and disaster-related information. The project focuses on **scraping textual data from these datasets and creating API endpoints** for easy access and analysis.

> Note: Not all datasets listed are directly used in this project. They are included for reference and to assist researchers in locating relevant datasets.

## Datasets Included (Reference)

| File Name | Description |
|-----------|-------------|
| `countries-countries-fb-social-connectedness-index-october-2021.tsv` | Facebook Social Connectedness Index for countries (Oct 2021). |
| `crisismmd_datasplit_agreed_label.zip` | CrisisMMD dataset with agreed labels for multimodal social media posts. |
| `crisismmd_datasplit_all.zip` | Full CrisisMMD dataset with all labeled posts. |
| `CrisisMMD_raw_tweets_ids.tar.gz` | Raw tweet IDs from CrisisMMD dataset. |
| `CrisisMMD_v1.0.tar.gz` | Version 1.0 of the CrisisMMD multimodal social media dataset. |
| `CrisisMMD_v2.0.tar.gz` | Version 2.0 of the CrisisMMD multimodal social media dataset. |
| `CrisisNLP_labeled_data_crowdflower_v2.zip` | Labeled social media posts collected via CrowdFlower for NLP tasks. |
| `CrisisNLP_volunteers_labeled_data.zip` | Labeled posts from volunteers for NLP research. |
| `FloodsInPakistan-tweets.csv.zip` | Tweets related to flood events in Pakistan. |
| `FloodsInPakistan2022-tweets.csv.zip` | Tweets specifically from Pakistan flood events in 2022. |
| `gadm1_nuts3_counties-fb-social-connectedness-index-october-2021.zip` | County-level Facebook Social Connectedness Index dataset. |
| `HumAID_data_all_combined.tar.gz` | Complete HumAID dataset for humanitarian aid social media posts. |
| `HumAID_data_events_set1_47K.tar.gz` | First subset of HumAID event-labeled data. |
| `HumAID_data_events_set2_29K.tar.gz` | Second subset of HumAID event-labeled data. |
| `HumAID_data_event_type.tar.gz` | Event-type-specific labeled data from HumAID. |
| `OOV_Dict.zip` | Dictionary of out-of-vocabulary words for NLP tasks. |
| `PakistanFloodsAppeal-tweets.csv.zip` | Tweets related to humanitarian appeals during Pakistan floods. |
| `us-counties-countries-fb-social-connectedness-index-october-2021.tsv` | US county-level Facebook Social Connectedness Index data. |
| `us-counties-us-counties-fb-social-connectedness-index-october-2021.zip` | Social connectedness index across US counties. |
| `us-zip-code-us-zip-code-fb-social-connectedness-index-october-2021.zip` | Social connectedness index across US ZIP codes. |

## Source & License

All datasets are **open-source** and have been collected from publicly available repositories online. They are intended for research, analysis, and educational purposes. Please refer to the respective dataset providers for specific licensing details.

## Usage

These datasets and endpoints can be used for:

- Social media analytics during disaster events  
- Crisis communication studies  
- Disaster risk assessment and early warning systems  
- NLP, sentiment analysis, and multimodal AI research  
- Humanitarian aid coordination and response studies  

## API Functionality

This project includes a FastAPI service that allows you to:

- Check service status:

- - Endpoint: /status

- - Returns whether the API service is currently online or offline.

- Toggle service online/offline:

- - Endpoint: /toggle

- - Switches the API status between online and offline. Useful for dashboards or automated wake-up on platforms like Render.

- Stream disaster data:

- - Endpoint: /data

- - Streams rows of the disaster CSV dataset as a JSON array, one row at a time.

- - Supports optional filtering by:

- - - id → fetch specific posts

- - - lang → fetch posts in a specific language

- NaN-safe JSON: All missing values (NaN or Inf) are converted to null in the output JSON.

### Example: Accessing an Endpoint

```python
import requests

# Check status
status = requests.get("http://localhost:8000/status").json()
print(status)  # {"status": "online"}

# Toggle service
toggle = requests.post("http://localhost:8000/toggle").json()
print(toggle)  # {"new_status": "online"}

# Fetch disaster data (streamed)
response = requests.get("http://localhost:8000/data", stream=True)
for line in response.iter_lines():
    if line:
        print(line)  # Each line is a JSON object

```

## How to Run Locally

### 1. Clone the repository

```python
git clone https://github.com/your-username/social-media-disaster-api.git
cd social-media-disaster-api

```
### 2. Create a virtual environment and install dependencies
```python
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

```
### 3. Start the FastAPI server
```python
uvicorn main:app --reload

```
### 4. Open Terminal
Open http://127.0.0.1:8000/docs to access Swagger UI for interactive API documentation.
```python
http://127.0.0.1:8000/docs
```


## References

- Erokhin & Komendantova, *Social media data for disaster risk management and research*, 2024【9†source】  
- Akbar et al., *Crisis Communication Effectiveness in Disaster Management*, 2025【10†source】  
- Cantini et al., *Prompt-based LLMs for disaster monitoring*, 2025【11†source】  
- Xiao et al., *Social Media-Enabled Flood Disaster Informatics*, 2025【12†source】  
- NDMA Live Disaster Intelligence Dashboard, 2025【13†source】  

## Citation

If you use these datasets or endpoints, please cite the original sources appropriately.

