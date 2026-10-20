from pathlib import Path

import allure
import pytest
from PIL import Image, ImageChops
from playwright.sync_api import Page


def compare_screenshots(page: Page, image_name: str):
    baseline_path = Path("visual_baselines") / f"{image_name}.png"
    actual_path = Path("test-results") / f"{image_name}_actual.png"
    diff_path = Path("test-results") / f"{image_name}_diff.png"

    actual_path.parent.mkdir(parents=True, exist_ok=True)

    page.screenshot(
        path=str(actual_path),
        full_page=True,
        animations="disabled"
    )

    assert baseline_path.exists(), f"Missing baseline: {baseline_path}"

    with Image.open(baseline_path) as baseline, Image.open(actual_path) as actual:
        assert baseline.size == actual.size, (
            f"Screenshot dimensions do not match: "
            f"baseline={baseline.size}, actual={actual.size}"
        )

        difference = ImageChops.difference(
            baseline.convert("RGB"),
            actual.convert("RGB")
        )

        if difference.getbbox() is not None:
            difference.save(diff_path)

            allure.attach.file(
                str(baseline_path),
                name="Visual Baseline",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach.file(
                str(actual_path),
                name="Actual Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach.file(
                str(diff_path),
                name="Visual Difference",
                attachment_type=allure.attachment_type.PNG
            )

            pytest.fail(f"Visual regression detected: {image_name}")