class AssetStore:
    def __init__(self):
        self.categories = ["3d_models", "textures", "audio_packs", "scripts"]
        self.cached_assets = {}

    def fetch_store_catalog(self, category="3d_models"):
        # Облачен каталог за активи с възможност за филтриране
        catalog = [
            {"id": 101, "name": "Cyberpunk Street Block", "category": "3d_models", "format": "gltf", "size": "3.8MB"},
            {"id": 102, "name": "Modular Sci-Fi Facade", "category": "3d_models", "format": "obj", "size": "1.2MB"},
            {"id": 103, "name": "Retro 8-Bit Synth Audio", "category": "audio_packs", "format": "mp3", "size": "500KB"}
        ]
        return [item for item in catalog if item["category"] == category]

    def download_and_cache(self, asset_id):
        # Механизъм за сваляне на директни линкове в локалната папка на приложението
        return True
