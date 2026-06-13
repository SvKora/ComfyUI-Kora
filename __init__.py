from .ideogram_mask_build import Ideogram_mask_build_Kora

NODE_CLASS_MAPPINGS = {
    "Ideogram_mask_build_Kora": Ideogram_mask_build_Kora
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ideogram_mask_build_Kora": "Ideogram Mask Builder (Kora)"
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]