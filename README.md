# ComfyUI Ideogram Mask Builder (Kora)

Advanced custom node for ComfyUI. A complete mini-editor built directly into the node interface for drawing masks, sketches, and generating Ideogram prompts.

## Features
* **Integrated Sketching:** Draw sketches directly on the node with customizable brush size, blur, and opacity.
* **Eyedropper Tool:** Pick colors directly from your image using `Alt + Click`.
* **Hotkeys:** Quick access to tools (e.g., press `S` to add a sketch, `B` to add mask for box, `[ ]` to change brush size, `H` to hide boxes,).
* **Independent Styling:** Fully isolated CSS to prevent conflicts with other UI extensions.

## Acknowledgements & Credits
This custom node is a highly modified and enhanced fork of the original Ideogram 4 Prompt Builder created by **[Kijai](https://github.com/kijai)**. 

Massive thanks to Kijai for providing the foundational Python logic and the brilliant Bounding Box UI framework! 

**Changes in the Kora version include:**
* Completely independent CSS architecture to prevent UI conflicts.
* Integrated Sketch Canvas with opacity and blur controls.
* Custom Eyedropper tool (Alt + Click).
* Hotkey optimizations for faster workflow.

This project is licensed under the GNU General Public License v3.0, in accordance with the original source code.