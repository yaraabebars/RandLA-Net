"""Command-line entry points for the asbuilt-hybrid workflow."""

from __future__ import annotations

import click


@click.group()
def main():
    """Entry point for orchestrating the ML → Geometry → IFC pipeline."""


@main.command()
@click.argument("scan_path")
@click.option("--model-path", required=True, help="Path to the pretrained RandLA-Net checkpoint.")
@click.option("--output-dir", required=True, help="Directory for pipeline outputs.")
def run(scan_path: str, model_path: str, output_dir: str):
    """Placeholder for executing the end-to-end pipeline."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
