class MemeBuilder:
    def __init__(self):
        self.meme = None

    def create_new_meme(self):
        self.meme = {
            "info": {
                "colors": [],
                "objects": []
            },
            "tags": [],
            "text": "",
            "updated_by": "",
            "url": ""
        }
        return self

    def create_default_meme(self, meme_id, created_by="olga"):
        self.meme = {
            "id": meme_id,
            "info": {
                "colors": ["green"],
                "objects": ["picture", "text"]
            },
            "tags": ["fun", "grinch"],
            "text": "Grinch",
            "updated_by": created_by,
            "url": "https://encrypted-tbn0"
        }
        return self

    def with_colors(self, colors=[]):
        self.meme["info"]["colors"] = colors
        return self

    def with_objects(self, objs=[]):
        self.meme["info"]["objects"] = objs
        return self

    def with_tags(self, tags=[]):
        self.meme["tags"] = tags
        return self

    def with_text(self, text):
        self.meme["text"] = text
        return self

    def with_updated_by(self, updated_by):
        self.meme["updated_by"] = updated_by
        return self

    def with_url(self, url):
        self.meme["url"] = url
        return self

    def build(self):
        return self.meme
