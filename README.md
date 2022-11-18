# BoostMyPhoto
Simple tool for photo boosting with Stable Diffusion.

## How the tool works?
User provides a photo, as well as text prompt describing on how to change it. Additionally, user
can define `transformation_strength` - value in range `(0.0; 1.0)` to determine how much to
transform image, as well as `prompt_importance` - the higher the value is (more distant from `1.0`) -
the more important the text input is for generating the output image.

### Example result

## Installation
```bash
pip install git+https://github.com/PawelPeczek/BoostMyPhoto.git
```

## Usage example

### Prerequisites
Once the tool is installed at your computer, you must log in into HuggingFace:
```bash
huggingface-cli login
```
And it is also required to navigate into
[runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) to accept
their usage terms and conditions.

### Command
```bash
boost_my_photo \
  --image_path /path/to/your/image.jpg \
  --text-prompt "Description on what to do with the picture" \
  --transformation_strength 0.75 \
  --prompt_importance 7.5 \
  --device [cpu, cuda:0] \
  --output_path /path/to/your/output_image.jpg
```
