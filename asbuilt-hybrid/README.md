# asbuilt-hybrid

The **asbuilt-hybrid** repository scaffolds a hybrid workflow that connects machine-learning-based point cloud understanding with downstream geometric reconstruction and Industry Foundation Classes (IFC) export. The goal is to take raw scans—such as the outputs of RandLA-Net semantic segmentation—and transform them into BIM-ready assets that support quantity take-off.

## Pipeline Overview

1. **Machine Learning (ML)**  
   Modules under `asbuilt_hybrid/ml/` cover data ingestion, pre-processing, inference, and post-processing tasks. This stage consumes point cloud scans, applies pretrained models (for example, RandLA-Net checkpoints), and yields per-point semantic predictions.

2. **Geometry Processing**  
   Modules in `asbuilt_hybrid/geometry/` provide hooks for grouping points by class, fitting parametric representations (slabs, beams, columns, shear walls), and reconstructing watertight meshes suitable for BIM ingestion.

3. **IFC Export & Quantities**  
   Modules in `asbuilt_hybrid/ifc/` coordinate the translation from reconstructed geometry to IFC entities. They are responsible for mapping semantic labels to IFC classes, assembling element properties, exporting compliant IFC files, and computing downstream quantity take-offs.

## Getting Started

1. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

   or with `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. Explore the placeholder modules to implement dataset adapters, RandLA-Net integration, geometric fitting routines, and IFC export logic tailored to your project requirements.

3. Use the Click-based CLI (`asbuilt_hybrid/cli.py`) as the orchestration layer for chaining the stages above into an automated pipeline.

## Next Steps

* Integrate the RandLA-Net preprocessing scripts to populate the ML stage.
* Implement geometric fitting algorithms that translate semantic clusters into parametric BIM elements.
* Wire up IfcOpenShell-based exporters to produce IFC files and compute reliable quantities for slabs, beams, columns, and shear walls.
