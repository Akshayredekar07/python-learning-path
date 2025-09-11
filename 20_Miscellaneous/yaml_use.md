
## **1. What is YAML?**

* **YAML** = "YAML Ain’t Markup Language".
* It’s a **human-readable configuration format** (like JSON but cleaner).
* Commonly used in **ML/DL projects** for:

  * Storing **hyperparameters**
  * Defining **experiment configurations**
  * Logging results
  * Managing **data paths, environment, and model settings**



# 2. Installing & Importing in Python

```bash
pip install pyyaml
```

```python
import yaml
```



# 3. Basic YAML Syntax

✅ Key–value pairs:

```yaml
learning_rate: 0.01
batch_size: 32
```

✅ Lists:

```yaml
layers:
  - 64
  - 128
  - 256
```

✅ Nested dicts:

```yaml
model:
  type: "neural_network"
  hidden_units: [64, 128, 256]
```

✅ Comments:

```yaml
# This is a comment
```

✅ Multi-line strings:

```yaml
description: |
  This is a sample experiment
  with multi-line notes.
```



# 4. Using YAML in Python

### Load YAML (dict form):

```python
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print(config["learning_rate"])
```

### Dump to YAML:

```python
data = {"lr": 0.01, "batch_size": 32}
with open("output.yaml", "w") as f:
    yaml.dump(data, f)
```



# 5. Why YAML for ML Projects?

Instead of **hardcoding** hyperparameters, we:

* Store them in a YAML file.
* Load at runtime → easy to change experiments.
* Enables **reproducibility**.



# 6. Entities to Define in YAML for ML Projects

Here’s a **typical schema** for ML configs:

```yaml
experiment:
  name: "image_classification_v1"
  seed: 42

data:
  train_path: "data/train.csv"
  test_path: "data/test.csv"
  validation_split: 0.2
  augmentations:
    - flip
    - rotate
    - normalize

model:
  type: "resnet50"
  input_dim: 224
  num_classes: 10
  pretrained: true

training:
  batch_size: 64
  epochs: 50
  optimizer: "adam"
  learning_rate: 0.001
  weight_decay: 0.0001
  scheduler:
    type: "step_lr"
    step_size: 10
    gamma: 0.5

logging:
  log_dir: "logs/"
  checkpoint_dir: "checkpoints/"
  save_every: 5

evaluation:
  metrics: ["accuracy", "f1_score"]
```

### Entities you **should define**:

1. **Experiment Info** → seed, experiment name
2. **Data** → paths, splits, augmentations
3. **Model** → architecture, input/output dims, pretrained or not
4. **Training Config** → epochs, batch size, optimizer, scheduler
5. **Logging/Checkpoints** → save locations, frequency
6. **Evaluation** → metrics, validation setup
7. **Deployment (optional)** → model serving config (API host, port, model version)



# 7. Example Case Studies



### ✅ Case Study 1: Deep Learning Image Classification

**config.yaml**

```yaml
experiment:
  name: "cifar10_resnet"
  seed: 123

data:
  dataset: "CIFAR10"
  root: "./data"
  batch_size: 128

model:
  type: "resnet18"
  num_classes: 10

training:
  optimizer: "sgd"
  learning_rate: 0.01
  momentum: 0.9
  epochs: 100

logging:
  checkpoint_dir: "./checkpoints/resnet_cifar"
  tensorboard: true
```

**train.py**

```python
import yaml
import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models

with open("config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

# Data
transform = transforms.Compose([transforms.ToTensor()])
train_loader = torch.utils.data.DataLoader(
    datasets.CIFAR10(cfg["data"]["root"], train=True, download=True, transform=transform),
    batch_size=cfg["data"]["batch_size"],
    shuffle=True
)

# Model
model = getattr(models, cfg["model"]["type"])(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, cfg["model"]["num_classes"])

# Optimizer
optimizer = optim.SGD(model.parameters(), 
                      lr=cfg["training"]["learning_rate"], 
                      momentum=cfg["training"]["momentum"])
```

👉 This makes the experiment fully **configurable from YAML**.



### ✅ Case Study 2: NLP Text Classification

**config.yaml**

```yaml
experiment:
  name: "bert_sentiment"
  seed: 42

data:
  train_file: "data/train.csv"
  test_file: "data/test.csv"
  text_column: "review"
  label_column: "sentiment"

model:
  type: "bert-base-uncased"
  max_length: 256

training:
  batch_size: 32
  epochs: 5
  learning_rate: 2e-5

logging:
  wandb: true
  project: "sentiment-analysis"
```

👉 This YAML feeds into a HuggingFace training pipeline (`Trainer`), making it easy to switch model or dataset by editing YAML.



### ✅ Case Study 3: MLOps Pipeline (Data + Train + Deploy)

**config.yaml**

```yaml
pipeline:
  steps:
    - data_preprocessing
    - feature_engineering
    - training
    - evaluation
    - deployment

data:
  raw_path: "s3://bucket/data/raw/"
  processed_path: "s3://bucket/data/processed/"
  target_column: "price"

model:
  type: "xgboost"
  max_depth: 6
  learning_rate: 0.1
  n_estimators: 500

deployment:
  api:
    host: "0.0.0.0"
    port: 8080
    model_path: "models/xgb_latest.pkl"
```

👉 This YAML could control a **Prefect/Airflow ML pipeline**, making the workflow reproducible.



# 8. Best Practices for YAML in ML

* Keep **separate YAMLs per environment** (dev.yaml, prod.yaml).
* Use **default.yaml + override.yaml** for shared configs.
* Keep YAML under **version control (Git)** for reproducibility.
* Store experiment logs (configs + metrics) in tools like **MLflow, WandB**.
* Use **OmegaConf / Hydra** (advanced Python libraries) for dynamic YAML configs.



9. Summary

* YAML is perfect for **experiment configs** in ML.
* Define **data, model, training, logging, evaluation** in YAML.
* Load YAML → make pipeline flexible and reproducible.
* Case studies (Image, NLP, MLOps) show **real-world usage**.


