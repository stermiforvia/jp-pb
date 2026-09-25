from datetime import datetime

class VocabMan:

    def validate_vocabulary(self, word, reading, meaning):

        if not word:
            return False

        if not reading:
            return False

        if not meaning:
            return False

        return True

    def create_vocabulary_entry(self, word, reading, meaning):

        created_date = datetime.now()

        vocabulary_entry = {
            "Word": word,
            "Reading": reading,
            "Meaning": meaning,
            "CreatedDate": created_date
        }

        return vocabulary_entry
