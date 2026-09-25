from python.vocabulary_management.vocabulary_management import VocabMan
from python.data_management.data_management import DataMan

class UI:

    def input_vocabulary(self):

        word = input("Enter Word: ")
        reading = input("Enter Reading: ")
        meaning = input("Enter Meaning: ")

        vocab_man = VocabMan()

        if vocab_man.validate_vocabulary(
            word,
            reading,
            meaning
        ):

            vocabulary_entry = (
                vocab_man.create_vocabulary_entry(
                    word,
                    reading,
                    meaning
                )
            )

            data_man = DataMan()

            result = data_man.store_vocabulary(
                vocabulary_entry["Word"],
                vocabulary_entry["Reading"],
                vocabulary_entry["Meaning"],
                vocabulary_entry["CreatedDate"]
            )

            print(result)

        else:

            print("Invalid vocabulary data.")