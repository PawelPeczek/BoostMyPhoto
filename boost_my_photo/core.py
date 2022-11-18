import logging

import click
import torch
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline

from boost_my_photo.constants import MODEL_ID, REVISION, RGB_MODE, MAX_IMAGE_SIZE


@click.command()
@click.option(
    "--image-path", type=str, required=True, help="Path to image to be transformed."
)
@click.option(
    "--text-prompt",
    type=str,
    required=True,
    help="Text description of changes to the image.",
)
@click.option(
    "--output-path", type=str, required=True, help="Location of output image."
)
@click.option(
    "--transformation-strength",
    type=float,
    required=False,
    default=0.75,
    help="Value in range (0.0; 1.0) describing how much to transform input image.",
)
@click.option(
    "--prompt-importance",
    type=float,
    required=False,
    default=7.5,
    help="Value in range (1.0, ...) describing how important is text prompt for output image.",
)
@click.option(
    "--device",
    type=str,
    required=False,
    default="cpu",
    help="Device to execute computations. Use cpu or cuda:X",
)
def boost_photo(
    image_path: str,
    text_prompt: str,
    output_path: str,
    transformation_strength: float,
    prompt_importance: float,
    device: str,
) -> None:
    target_device = torch.device(device)
    torch_dtype = torch.float16
    if "cpu" in device:
        logging.warning("Running the tool on CPU may be slower.")
        torch_dtype = torch.float32
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_ID,
        revision=REVISION,
        torch_dtype=torch_dtype,
    ).to(target_device)
    image = Image.open(image_path).convert(RGB_MODE)
    image.thumbnail(MAX_IMAGE_SIZE)
    output_images = pipe(
        prompt=text_prompt,
        init_image=image,
        strength=transformation_strength,
        guidance_scale=prompt_importance,
    ).images
    output_images[0].save(output_path)


if __name__ == "__main__":
    boost_photo()
