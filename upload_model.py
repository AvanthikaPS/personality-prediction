from huggingface_hub import HfApi

api = HfApi()

api.upload_file(
    path_or_fileobj="model.joblib",   # your model file
    path_in_repo="model.joblib",      # name on HuggingFace
    repo_id="AvanthikaPS/personality-predictor-model"
)
