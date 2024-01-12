from classes import Name
import pickle


class Note:
    '''class represents a single note with text'''

    def __init__(self, author, title, body):
        self.author = Name(author)
        self.title = title
        self.body = body

    def save_note(self):
        return {
            'author': self.author.value,
            'title': self.title,
            'body': self.body
        }

    @classmethod
    def notes_dict(cls, notes):
        return cls(notes['author'], notes['title'], notes['body'])

    def __str__(self):
        return f"\nAuthor: {self.author}\nTitle: {self.title}\nNote: {self.body}"


class Notebook:
    '''class manages a list of notes'''

    def __init__(self):
        self.notes = {}

    def add_note(self, note):
        self.notes[note.title] = note

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]

    def find_note(self, search_query):
        return [note for note in self.notes.values() if search_query.lower() in note.title.lower() or search_query.lower() in note.author.value.lower()]

    def edit_note(self, title, new_body):
        if title in self.notes:
            self.notes[title].body = new_body
